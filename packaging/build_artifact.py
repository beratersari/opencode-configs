#!/usr/bin/env python3
"""Zip this pack for Windows or Linux. Stdlib only."""

from __future__ import annotations

import argparse
import zipfile
from pathlib import Path

INCLUDE = (
    "README.md",
    "install.py",
    "install.bat",
    "install.sh",
    "agents",
    "skills",
    "packaging/versions.env",
)


def read_opencode_version(root: Path) -> str:
    path = Path(root) / "packaging" / "versions.env"
    if not path.is_file():
        raise SystemExit(f"missing {path}")
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("OPENCODE_VERSION="):
            version = line.split("=", 1)[1].strip()
            if version:
                return version
    raise SystemExit(f"OPENCODE_VERSION missing in {path}")


def artifact_name(version: str, os_tag: str) -> str:
    safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in version)
    tag = os_tag.strip().lower()
    return f"opencode-configs-{safe}-{tag}.zip"


def build(root: Path, dest: Path) -> Path:
    root = root.resolve()
    dest.parent.mkdir(parents=True, exist_ok=True)
    review = root / "agents" / "review.md"
    if not review.is_file():
        raise SystemExit(f"missing {review}")
    with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for name in INCLUDE:
            src = root / name
            if src.is_file():
                zf.write(src, name)
                continue
            if not src.is_dir():
                raise SystemExit(f"missing {src}")
            for path in src.rglob("*"):
                if path.is_file() and ".git" not in path.parts:
                    zf.write(path, path.relative_to(root).as_posix())
    return dest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--os", choices=("linux", "windows"), default="")
    parser.add_argument("--out", default="", help="Full zip path. Default: dist/opencode-configs-<version>-<os>.zip")
    parser.add_argument("--out-dir", default="dist")
    args = parser.parse_args()
    root = Path(args.root)
    if args.out:
        dest = Path(args.out)
    else:
        os_tag = args.os or ("windows" if __import__("os").name == "nt" else "linux")
        dest = Path(args.out_dir) / artifact_name(read_opencode_version(root), os_tag)
    path = build(root, dest)
    print(path.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
