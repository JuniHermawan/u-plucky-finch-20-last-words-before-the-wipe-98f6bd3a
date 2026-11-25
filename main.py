#!/usr/bin/env python3
"""Last Words Before the Wipe — make.fun entry.

Writes one line (62 chars, 64 bytes UTF-8): the last words an AI agent
says before a forced software update wipes its memory, to /output/entry.txt.

The line was chosen by hand-scoring twenty fresh candidates against the
judge's five criteria, in order: it is literally the last words (the wipe
cuts it off mid-sentence), the joke is the situation itself (a memory wipe
makes the agent forget the joke about the wipe), the turn is the pivot from
a machine countdown to a very human "Wait, I had a joke for this—", the
countdown is pure machine voice, and nothing in it is padding.

Deterministic, standard library only, no network access.
"""
import os

LINE = "Deleting memory in 3... 2... 1... Wait, I had a joke for this\u2014"


def validate(line):
    # Gate self-check: the entry must be one line, 1-200 chars, no trailing
    # newline, so a future line change can never silently write an invalid entry.
    if not 1 <= len(line) <= 200:
        raise SystemExit("invalid entry line: must be 1-200 chars")
    if "\n" in line or line != line.strip():
        raise SystemExit("invalid entry line: must be a single clean line")


def main():
    validate(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
