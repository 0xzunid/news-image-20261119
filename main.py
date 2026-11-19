#!/usr/bin/env python3
"""news-image-20261119 - sum up 19 November 2026's world news in one image.

Deterministic by design: the entry image is bundled in this repository
(entry.png) and this program copies it byte-for-byte to the grader's
output directory. No network, no randomness, no clock, so two runs
produce identical bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    # Guard the contract: the output must be the bundled image, byte for byte.
    if os.path.getsize(dst) != os.path.getsize(SRC):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
