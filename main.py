"""The One-Line Exit: a program that writes the funniest single-line
resignation letter to /output/entry.txt.

The letter is one line, 128 characters, and reads like a real letter
a person could actually send: a named workplace detail (the 7 a.m.
standup) with a surprise turn at the end.
"""

import os

LINE = (
    "I am resigning effective Friday. The 7 a.m. standup has eaten my soul, "
    "and I'd like it back before it schedules a follow-up."
)


def main() -> None:
    # Enforce the competition gate ourselves: exactly one line,
    # 1 to 140 characters, not only whitespace, no em dash.
    assert "\n" not in LINE and 1 <= len(LINE) <= 140 and LINE.strip()
    assert "—" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
