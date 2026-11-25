#!/usr/bin/env python3
"""Write one original one-line office joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

Competition: u-suzy-one-line-office-joke-laugh-off-f574ac73
(One-Line Office Joke Laugh-Off, make.fun).

Standard library only. Deterministic: the same bytes on every run.
"""

import os
import sys

JOKE = 'My boss calls it "wearing many hats"; I call it five job descriptions and one salary.\n'

# Gate limits from the competition rules (competition.yaml / RULES.txt):
# entry.txt must be UTF-8 text of 1 to 200 characters, not only white space,
# and the entry is a single line. A trailing newline is part of the file.
MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> None:
    """Check the entry against the competition gate; raise ValueError if invalid."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    body = text.rstrip("\n")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")


def main() -> int:
    validate(JOKE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    return 0
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
