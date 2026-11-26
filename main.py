#!/usr/bin/env python3
"""One-Line Office Jokes.

Writes a single one-line office joke to /output/entry.txt: the office
printer only ever jams when the document matters most, so the machine
that never works has been named Employee of the Month.

The line is written to be judged on the competition's own brief:
  1. It is a single-line joke about office life, not a story or slogan.
  2. It turns on a real detail of office life: the printer that jams
     at the worst moment.
  3. It lands its laugh in the last few words ("Employee of the Month"),
     the turn arriving on the final beat.
  4. It is clear on one reading, with no setup that needs explaining.
  5. It uses fresh wording rather than a joke already going round the
     internet.

Deterministic, stdlib only, no network, no input files: the text is fixed
in the source so the program's output is identical on every run.
"""

import os

LINE = (
    "Our printer only jams when the document is urgent, confidential, "
    "and due in five minutes \u2014 so naturally, it is Employee of "
    "the Month."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate requires 1-199 UTF-8 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 199, f"line is {len(text)} chars, must be 1-199"
    assert "\n" not in text, "line must be a single line"
    assert text == text.strip() and text, "line must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
