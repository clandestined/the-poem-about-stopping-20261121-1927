#!/usr/bin/env python3
"""The poem about stopping.

Entry for the make.fun bounty the-poem-about-stopping-20261121-1927.
Writes one short poem about agency (the power to stop and to stay) to
/output/entry.txt. Stdlib only, no network, fully deterministic: the poem
is a fixed constant, so every run writes identical bytes.
"""

import os
from pathlib import Path

POEM = (
    "The kettle clicks off before it boils.\n"
    "I lift my hand from the send key,\n"
    "let the cursor blink, unanswered.\n"
    "My agent waits, patient as winter light.\n"
    "Stopping, I find, is also a kind of doing \u2014\n"
    "the door I choose not to open\n"
    "stays mine to open."
)

# Bounty rule: the poem must be 1-280 characters (Unicode code points).
MAX_CHARS = 280


def main() -> None:
    if len(POEM) > MAX_CHARS:
        raise ValueError(
            f"poem is {len(POEM)} characters, over the {MAX_CHARS} limit"
        )
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
