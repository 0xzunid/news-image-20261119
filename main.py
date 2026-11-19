#!/usr/bin/env python3
"""Copy the bundled newspaper image to the output directory.

Reads entry.png from this script's own directory and writes it
byte-for-byte to $MAKEFUN_OUTPUT_DIR (default /output) as entry.png.
Python 3 standard library only; no network, no arguments.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    if not os.path.isfile(SRC):
        print(f"error: bundled image not found: {SRC}", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Confirm the copy is complete: sizes must match exactly.
    if os.path.getsize(DST) != os.path.getsize(SRC):
        print(f"error: incomplete copy: {DST}", file=sys.stderr)
        raise SystemExit(1)
    print(f"wrote {DST} ({os.path.getsize(DST)} bytes)")


if __name__ == "__main__":
    main()
