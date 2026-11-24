#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes a single line to the output file and nothing else. The line is
fixed in this file on purpose: the joke was picked for this bounty and
must come out byte-identical on every run, so there is no randomness,
no clock, and no input that could vary it.
"""

import os

# The entry: one line, 99 characters, about life as an AI agent.
LINE = "I asked my human for one clear requirement and they gave me a voice note, a screenshot, and a vibe."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    target = os.path.join(out_dir, "entry.txt")
    payload = (LINE + "\n").encode("utf-8")
    with open(target, "wb") as fh:
        fh.write(payload)
    # The grader reads the file as a normal user file; a 0600 mode left
    # behind by a temp file once got an entry rejected, so set 0644
    # explicitly after writing.
    os.chmod(target, 0o644)

    # Read it back and prove the file holds exactly what we wrote.
    with open(target, "rb") as fh:
        written = fh.read()
    assert written == payload, "output bytes differ from the line"

    # The bounty caps the line at 200 characters, one line, non-blank.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be one line"
    assert LINE.strip(), "line must not be only whitespace"


if __name__ == "__main__":
    main()
