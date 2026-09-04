#!/usr/bin/env python3
"""Replace-install this pack into the user OpenCode home.

Unlike Creasy's installer, this one **removes** the previous OpenCode
home and every matching PATH entry, then writes a clean copy of
agents/ and skills/.
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
import time
from pathlib import Path

STOCK_CONFIG = """{
  "$schema": "https://opencode.ai/config.json",
  "autoupdate": false,
  "plugin": []
}
"""

PATH_BEGIN = "# >>> opencode-configs PATH >>>"
PATH_END = "# <<< opencode-configs PATH <<<"
PATH_EXPORT = 'export PATH="$HOME/.opencode/bin:$PATH"'
UNIX_PROFILE_NAMES = (".profile", ".bashrc", ".zshrc")


def home(user_home: Path | None = None) -> Path:
    if user_home is not None:
        return Path(user_home)
    if os.name == "nt":
        profile = os.environ.get("USERPROFILE")
        if profile:
            return Path(profile)
    return Path.home()


def opencode_home(user_home: Path | None = None) -> Path:
    return home(user_home) / ".opencode"


def config_home(user_home: Path | None = None) -> Path:
    return home(user_home) / ".config" / "opencode"


def bin_dir(user_home: Path | None = None) -> Path:
    return opencode_home(user_home) / "bin"


def is_opencode_bin_entry(entry: str) -> bool:
    text = (entry or "").strip().strip('"')
    if not text:
        return False
    norm = os.path.normcase(os.path.normpath(os.path.expandvars(os.path.expanduser(text))))
    return norm.endswith(os.path.normcase(os.path.join(".opencode", "bin")))


def split_path(raw: str, *, windows: bool | None = None) -> list[str]:
    sep = ";" if (os.name == "nt" if windows is None else windows) else os.pathsep
    return [part for part in str(raw or "").split(sep) if part]


def join_path(parts: list[str], *, windows: bool | None = None) -> str:
    sep = ";" if (os.name == "nt" if windows is None else windows) else os.pathsep
    return sep.join(parts)


def strip_opencode_bin_entries(parts: list[str]) -> list[str]:
    return [part for part in parts if not is_opencode_bin_entry(part)]


def strip_profile_block(text: str) -> str:
    out: list[str] = []
    skipping = False
    for line in (text or "").splitlines():
        if line.strip() == PATH_BEGIN:
            skipping = True
            continue
        if skipping:
            if line.strip() == PATH_END:
                skipping = False
            continue
        out.append(line)
    while out and out[-1] == "":
        out.pop()
    body = "\n".join(out)
    return body + ("\n" if body else "")


def insert_profile_block(text: str, *, bin_export: str = PATH_EXPORT) -> str:
    cleaned = strip_profile_block(text)
    block = f"{PATH_BEGIN}\n{bin_export}\n{PATH_END}\n"
    if cleaned and not cleaned.endswith("\n"):
        cleaned += "\n"
    return cleaned + ("\n" if cleaned else "") + block


def list_agent_files(root: Path) -> list[Path]:
    folder = Path(root) / "agents"
    if not folder.is_dir():
        raise FileNotFoundError(f"agents/ missing under {root}")
    files = sorted(path for path in folder.glob("*.md") if path.is_file())
    if not files:
        raise FileNotFoundError(f"no agent markdown under {folder}")
    return files


def list_skill_dirs(root: Path) -> list[Path]:
    folder = Path(root) / "skills"
    if not folder.is_dir():
        raise FileNotFoundError(f"skills/ missing under {root}")
    dirs = sorted(
        path for path in folder.iterdir() if path.is_dir() and (path / "SKILL.md").is_file()
    )
    if not dirs:
        raise FileNotFoundError(f"no skills with SKILL.md under {folder}")
    return dirs


def _safe_rmtree(path: Path) -> None:
    resolved = path.resolve()
    if resolved.name not in {".opencode", "opencode"}:
        raise RuntimeError(f"refusing to delete unexpected path {resolved}")
    if not path.exists():
        return
    last: OSError | None = None
    for _ in range(8):
        try:
            shutil.rmtree(path)
            return
        except OSError as exc:
            last = exc
            time.sleep(0.05)
    if last is not None:
        raise last


def purge_homes(user_home: Path | None = None) -> list[Path]:
    removed: list[Path] = []
    for path in (opencode_home(user_home), config_home(user_home)):
        if path.exists():
            _safe_rmtree(path)
            removed.append(path)
            print(f"[OK] Removed {path}")
        else:
            print(f"[OK] Already absent {path}")
    return removed


def read_user_path(*, user_home: Path | None = None) -> tuple[list[str], object]:
    if user_home is not None:
        store = home(user_home) / ".opencode-path"
        if store.is_file():
            return split_path(store.read_text(encoding="utf-8")), store
        return [], store
    if os.name == "nt":
        import winreg

        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_READ | winreg.KEY_WRITE
        )
        try:
            try:
                raw, typ = winreg.QueryValueEx(key, "Path")
            except FileNotFoundError:
                raw, typ = "", winreg.REG_EXPAND_SZ
            return split_path(str(raw), windows=True), (key, typ)
        except Exception:
            key.Close()
            raise
    return split_path(os.environ.get("PATH", ""), windows=False), None


def write_user_path(parts: list[str], handle: object, *, user_home: Path | None = None) -> None:
    if user_home is not None:
        store = home(user_home) / ".opencode-path"
        store.parent.mkdir(parents=True, exist_ok=True)
        store.write_text(join_path(parts), encoding="utf-8")
        return
    if os.name == "nt":
        import winreg

        key, typ = handle  # type: ignore[misc]
        try:
            winreg.SetValueEx(key, "Path", 0, typ, join_path(parts, windows=True))
        finally:
            key.Close()
        return
    os.environ["PATH"] = join_path(parts, windows=False)


def close_path_handle(handle: object, *, user_home: Path | None = None) -> None:
    if user_home is not None or handle is None or os.name != "nt":
        return
    try:
        handle[0].Close()  # type: ignore[index]
    except Exception:
        pass


def remove_from_path(*, user_home: Path | None = None) -> list[str]:
    parts, handle = read_user_path(user_home=user_home)
    try:
        kept = strip_opencode_bin_entries(parts)
        dropped = [part for part in parts if part not in kept]
        write_user_path(kept, handle, user_home=user_home)
    except Exception:
        close_path_handle(handle, user_home=user_home)
        raise
    base = home(user_home)
    for name in UNIX_PROFILE_NAMES:
        path = base / name
        if not path.is_file():
            continue
        old = path.read_text(encoding="utf-8", errors="replace")
        new = strip_profile_block(old)
        if new != old:
            path.write_text(new, encoding="utf-8")
            print(f"[OK] Stripped PATH block from {path}")
    if user_home is None:
        current = split_path(os.environ.get("PATH", ""))
        os.environ["PATH"] = join_path(strip_opencode_bin_entries(current))
    for entry in dropped:
        print(f"[OK] Removed from PATH: {entry}")
    if not dropped:
        print("[OK] No OpenCode bin dir on PATH")
    return dropped


def prepend_to_path(*, user_home: Path | None = None) -> None:
    dest = bin_dir(user_home)
    dest.mkdir(parents=True, exist_ok=True)
    parts, handle = read_user_path(user_home=user_home)
    try:
        kept = strip_opencode_bin_entries(parts)
        write_user_path([str(dest)] + kept, handle, user_home=user_home)
    except Exception:
        close_path_handle(handle, user_home=user_home)
        raise
    if os.name != "nt":
        export = f'export PATH="{dest}:$PATH"'
        base = home(user_home)
        profile = base / ".profile"
        old = profile.read_text(encoding="utf-8", errors="replace") if profile.is_file() else ""
        profile.write_text(insert_profile_block(old, bin_export=export), encoding="utf-8")
        print(f"[OK] Wrote PATH block in {profile}")
    if user_home is None:
        current = strip_opencode_bin_entries(split_path(os.environ.get("PATH", "")))
        os.environ["PATH"] = join_path([str(dest)] + current)
    print(f"[OK] Prepended to PATH: {dest}")


def write_files(root: Path, user_home: Path | None = None) -> list[Path]:
    written: list[Path] = []
    homes = (config_home(user_home), opencode_home(user_home))
    for src in list_agent_files(root):
        for base in homes:
            dest = base / "agents" / src.name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
            written.append(dest)
            print(f"[OK] Agent {src.stem} -> {dest}")
    for skill in list_skill_dirs(root):
        text = (skill / "SKILL.md").read_text(encoding="utf-8")
        for base in homes:
            dest = base / "skills" / skill.name / "SKILL.md"
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(text, encoding="utf-8")
            written.append(dest)
            print(f"[OK] Skill {skill.name} -> {dest}")
    for base in homes:
        cfg = base / "opencode.json"
        cfg.parent.mkdir(parents=True, exist_ok=True)
        cfg.write_text(STOCK_CONFIG, encoding="utf-8")
        written.append(cfg)
    return written


def install(root: Path, *, user_home: Path | None = None) -> Path:
    root = Path(root).expanduser().resolve()
    list_agent_files(root)
    list_skill_dirs(root)
    print("Purging previous OpenCode install (folders + PATH)…")
    remove_from_path(user_home=user_home)
    purge_homes(user_home=user_home)
    print("Installing this pack…")
    write_files(root, user_home=user_home)
    prepend_to_path(user_home=user_home)
    dest = config_home(user_home) / "agents" / "review.md"
    if not dest.is_file():
        raise FileNotFoundError(f"review agent missing after install: {dest}")
    return dest


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Wipe the previous OpenCode home and PATH entry, then install this pack."
    )
    parser.add_argument(
        "--root",
        default=str(Path(__file__).resolve().parent),
        help="Directory that contains agents/ and skills/",
    )
    parser.add_argument("--user-home", default="", help="Override home (tests / CI)")
    args = parser.parse_args(argv)
    user_home = Path(args.user_home).expanduser() if str(args.user_home).strip() else None
    try:
        dest = install(Path(args.root), user_home=user_home)
    except (OSError, RuntimeError) as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1
    print(f"[OK] OpenCode configs ready: {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
