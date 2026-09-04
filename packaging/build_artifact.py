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
)


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
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    path = build(Path(args.root), Path(args.out))
    print(path.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
