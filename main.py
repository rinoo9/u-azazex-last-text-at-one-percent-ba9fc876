#!/usr/bin/env python3
"""Last Text at One Percent — make.fun entry.

The phone's final text message as its battery hits 1 percent.
One line, at most 199 characters, printed to stdout and,
per RULES.txt, written to /output/entry.txt when that directory
is available (the grading sandbox mounts it).

Why this line works: three goodbyes in one breath — Mom, the boss,
the ex — each one more honest than the last, and the final confession
about the playlist is the joke that lands after the sentiment. The
phone is dying, so it finally tells the truth.
"""

import os
import sys

ENTRY = (
    "1% battery. If I die mid-text, tell Mom I love her, tell my boss "
    "the report is in the cloud, and tell my ex I never liked his playlist."
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
