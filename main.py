#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one single sentence (1-280 UTF-8 characters) recalling a childhood
memory to /output/entry.txt. The sentence is fixed and deterministic so every
run produces byte-identical output.
"""

import os

SENTENCE = (
    "When the rain started, my grandmother would pull me inside, "
    "press a warm ball of rice into my palm with her bare hands and "
    "whisper to eat slowly, and twenty years later every rainy "
    "afternoon still smells like her kitchen."
)


def main() -> None:
    text = SENTENCE.strip()
    if not (1 <= len(text) <= 280):
        raise SystemExit(f"entry is {len(text)} characters, must be 1-280")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single sentence on one line")
    text.encode("utf-8")  # gate requires valid UTF-8
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
