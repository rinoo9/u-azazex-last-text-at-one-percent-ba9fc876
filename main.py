#!/usr/bin/env python3
"""Last Text at One Percent — make.fun entry.

The phone's final text message as its battery hits 1 percent.
One line, at most 199 characters, printed to stdout and,
per RULES.txt, written to /output/entry.txt when that directory
is available (the grading sandbox mounts it).

Why this line works (revision round 3, 25 Nov 2026): the previous
line stacked three goodbyes — Mom, boss, ex — and the playlist
confession. This one keeps the three-goodbye shape but makes the
third goodbye the joke itself: the phone finally admits it read
every unread message and deliberately chose silence. The dying
phone stops being polite and tells the truth about itself, which
is funnier than another farewell — and the charger absolution in
the middle keeps the phone's personality warm, not bitter.
"""

import os
import sys

ENTRY = (
    "1%. Tell my owner I loved them, tell the charger it was never "
    "his fault, and tell their 47 unread messages I read every single "
    "one and chose silence."
)

MAX_CHARS = 199


def main() -> None:
    if not ENTRY.strip():
        raise SystemExit("entry must not be empty")
    if len(ENTRY) > MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit")
    if len(ENTRY.splitlines()) != 1:
        raise SystemExit("entry must be a single line")
    print(ENTRY)
    print(f"({len(ENTRY)} characters, limit {MAX_CHARS})", file=sys.stderr)
    # RULES.txt: "Your program writes one text to /output/entry.txt".
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
