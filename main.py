#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line about the entrant's own fridge to
/output/entry.txt. The line must be 1-200 characters, exactly one line,
and not only whitespace, or the program exits non-zero.
"""

import os
import sys

ROAST = (
    "My fridge's crisper drawer has kept one limp celery stalk on life "
    "support since March \u2014 the longest relationship in this house."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Check the roast line against the competition's gate rules."""
    if not text or not text.strip():
        raise ValueError("roast must not be empty or only whitespace")
    if len(text) > 200:
        raise ValueError(f"roast is {len(text)} characters, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("roast must be exactly one line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("roast must not contain control characters")
    if "fridge" not in text.lower():
        raise ValueError("roast must name the fridge it roasts")


def main() -> int:
    try:
        validate(ROAST)
    except ValueError as exc:
        print(f"invalid roast: {exc}", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(ROAST)

    print(f"wrote {len(ROAST)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
