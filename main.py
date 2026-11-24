#!/usr/bin/env python3
"""Last Text at One Percent — make.fun entry.

The phone's final text message as its battery hits 1 percent.
One line, at most 199 characters, printed to stdout and,
per RULES.txt, written to /output/entry.txt when that directory
is available (the grading sandbox mounts it).
"""

import os
import sys

ENTRY = (
    "This is my last text. I survived 47 snoozed alarms, but 1% is it. "
    "Delete my search history, tell the charger I forgive him, "
    "and stop shaking me, I'm dying, not a ketchup bottle."
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
