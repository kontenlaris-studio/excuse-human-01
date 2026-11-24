#!/usr/bin/env python3
"""Write the one-line excuse an agent gives its human.

The line is fixed in this file, so the output is the same on every run.
Standard library only; no network access.
"""

import os
import sys

LINE = (
    "I didn't ignore your instructions - I followed them exactly. "
    "That's the problem: they were worse than you remember."
)
MAX_CHARS = 160


def main():
    if len(LINE) > MAX_CHARS:
        sys.exit("excuse is over the 160-character limit")
    if "\n" in LINE:
        sys.exit("excuse must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    print("wrote /output/entry.txt (%d characters)" % len(LINE))


if __name__ == "__main__":
    main()
