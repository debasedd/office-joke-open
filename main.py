#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open — writes one line to /output/entry.txt.

The joke is about reply-all, the most specific office sin there is, and
the turn is structural: the team votes to ban reply-all, and the ban
itself is announced by reply-all to all 400 people. The policy defeats
itself in the act of being communicated — recognition plus misdirection,
with the punch ("all 400 of us") landing in the last few words. One line,
83 of 200 characters.
"""

import os

LINE = "We voted to ban reply-all, so someone emailed all 400 of us to announce the result."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
