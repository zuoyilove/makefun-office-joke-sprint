#!/usr/bin/env python3
"""One line office joke about a 24-hour sprint.

Writes the joke to /output/entry.txt. Gate: UTF-8 text, 1-200 chars,
not only whitespace, single line.
"""

LINE = (
    "Our 24-hour sprint grew a 25th hour: a meeting to decide what 'done' "
    "means, chaired by the person who missed the sprint."
)

MAX_CHARS = 200


def main():
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be blank"
    assert LINE.count("\n") == 0, "line must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
