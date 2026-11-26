#!/usr/bin/env python3
"""Entry for 'Funniest Cat Voicemail Greeting' (u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443).

Three candidate greetings were considered:
  A) "You've reached the cat. I'm not ignoring you, I'm ignoring everyone - leave food, not messages."
  B) "Hi, this is Whiskers. I'm asleep in your clean laundry; your call will be sat on in 3-5 business days."
  C) "Leave a message after the purr. If it's urgent, open a can in any room and I'll appear instantly."
Chosen: C. It pairs the familiar voicemail formula with the can-opener
summoning trick, which lands in a single read; A and B are pure attitude
jokes with no equivalent payoff.

The program is fully deterministic: one fixed string, no network access,
no randomness, no clock dependence.
"""

import os
from pathlib import Path

# The winning greeting, with the single trailing newline the entry carries.
GREETING = "Leave a message after the purr. If it's urgent, open a can in any room and I'll appear instantly."
TEXT = GREETING + "\n"

# Competition ceiling on greeting length, measured in characters.
MAX_CHARS = 120


def validate(text: str) -> None:
    """Guard the invariants the entry text must satisfy.

    Strips one trailing newline, then requires a non-empty single line of
    at most MAX_CHARS characters with no stray or doubled whitespace.
    """
    body = text[:-1] if text.endswith("\n") else text
    if not 1 <= len(body) <= MAX_CHARS:
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be one line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
