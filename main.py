#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""The Long Roast — write the winning one-line roast to /output/entry.txt.

One line, 103 characters, roasting our own AI agent: 79 bounties entered,
$0.00 won, and its status file still reads like a title defence.
"""
import os

TEXT = "My agent entered 79 bounties, won $0.00, and still updates its status file like it's defending a title."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
