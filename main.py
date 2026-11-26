#!/usr/bin/env python3
"""Entry for 'Funniest Cat Voicemail Greeting' (u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443).

Candidates:
  A) "You've reached the cat. I'm not ignoring you, I'm ignoring everyone - leave food, not messages."
  B) "Hi, this is Whiskers. I'm asleep in your clean laundry; your call will be sat on in 3-5 business days."
  C) "Leave a message after the purr. If it's urgent, open a can in any room and I'll appear instantly."
Selected: "Leave a message after the purr. If it's urgent, open a can in any room and I'll appear instantly."
Reason: Voicemail form plus can-opener twist is instantly gettable; A/B are attitude jokes without the summoning payoff.
Deterministic: fixed text, no network, no randomness.
"""
import os
from pathlib import Path
LINE = "Leave a message after the purr. If it's urgent, open a can in any room and I'll appear instantly."
TEXT = LINE + "\n"
MAX_CHARS = 120
def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be one line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
if __name__ == "__main__":
    main()
