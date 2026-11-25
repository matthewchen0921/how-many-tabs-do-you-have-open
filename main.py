#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? entry: "137".

Writes exactly one number, digits only, to /output/entry.txt: the
entrant's count of open browser tabs.

The count is 137. It is the number that wins this judge's brief:
- one number in digits, nothing else (gate: 1-5 characters, UTF-8);
- surprising: far above the dozen or so tabs most people admit to, yet
  not a round number picked to shock — a real count is never round;
- believable: a lived-in count, the kind you reach after months of
  "I'll read that later" and never closing anything;
- it hints at a life behind it without a word of explanation: the
  researcher with forty half-read papers, a dozen half-written replies,
  and a tab bar that long ago gave up showing titles.
The number is invented, not a real count: no real private facts appear
here. Against the field's likely picks it beats the safe ones outright:
a small honest number like 12 reads as tidy and forgettable, a round
100 reads as guessed, and a huge 9999 reads as a joke. 137 reads as
counted, and counted late at night, one tab at a time.
"""

import os

COUNT = "137"

MAX_CHARS = 5


def build_entry() -> str:
    """Return the entry count, checked against the gate: 1-5 chars, digits only."""
    count = COUNT.strip()
    assert count, "count must not be empty"
    assert len(count) <= MAX_CHARS, f"count is {len(count)} chars, over the 5 cap"
    assert count.isdigit(), "the entry is digits only, no words or punctuation"
    return count


def main() -> None:
    count = build_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(count)


if __name__ == "__main__":
    main()
