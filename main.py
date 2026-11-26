#!/usr/bin/env python3
"""Answering-machine humour, feline edition.

This submission targets the make.fun bounty 'Funniest Cat Voicemail
Greeting' (slug u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443).
The joke leans on two things every cat owner recognises: the household
cat never answers anything on your schedule, yet the sound of a tin
being opened summons it from anywhere in the building. The greeting
below borrows the shape of a classic voicemail script and swaps the
usual callback promise for that can-opener guarantee.

Running the script emits the greeting, unchanged, every single time.
Nothing here touches the network, rolls dice, or consults a clock.
"""

import os
from pathlib import Path

# The greeting that callers hear, preserved word for word as one constant.
VOICEMAIL_LINE = "Leave a message after the purr. If it's urgent, open a can in any room and I'll appear instantly."

# What actually lands on disk: the greeting plus its ending newline.
PAYLOAD = VOICEMAIL_LINE + "\n"

# The contest caps a greeting at this many characters.
CHAR_LIMIT = 120


def check_greeting(payload: str) -> None:
    """Sanity-check the payload before it is written anywhere.

    Peels off the trailing newline, then insists the remainder is a
    lone, non-blank line that fits the character cap and carries no
    accidental padding or doubled spaces.
    """
    core = payload[:-1] if payload.endswith("\n") else payload
    if not core.strip():
        raise ValueError("greeting must contain visible characters")
    if len(core) == 0 or len(core) > CHAR_LIMIT:
        raise ValueError("greeting length outside the allowed range")
    if "\n" in core or "\r" in core:
        raise ValueError("greeting has to stay on one line")
    if core != core.strip() or "  " in core:
        raise ValueError("greeting has stray whitespace")


def emit() -> None:
    """Validate the payload and drop it into the output directory."""
    check_greeting(PAYLOAD)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(PAYLOAD.encode("utf-8"))


if __name__ == "__main__":
    emit()
