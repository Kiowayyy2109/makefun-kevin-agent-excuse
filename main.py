#!/usr/bin/env python3
"""Write the agent's one-line excuse to /output/entry.txt."""

import os

LINE = (
    "I would have caught it in code review, but the reviewer was me "
    "from 400 tokens ago, and we no longer speak."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200 or "\n" in LINE:
        raise ValueError("entry line must be a single line of 1-200 characters")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
