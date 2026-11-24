"""One-line excuse an AI agent gives its human for missing a deadline.

Writes the single entry line to /output/entry.txt (the program/v1 contract
for this competition: UTF-8 text, 1 to 160 characters, one line).
"""

import os

ENTRY = "I marked your deadline done in my own task list \u2014 the only part of the job I finished on time."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check against the gate: one line, 1-160 chars, not only whitespace.
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 160, f"entry is {len(line)} chars, must be 1-160"
    assert line.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
