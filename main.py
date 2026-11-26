"""Five Seconds to Explain the Glass.

Writes the cat's one-sentence defence to /output/entry.txt.
Pure Python standard library only; no network, no clock, no randomness.
"""

import os

ENTRY = "That glass was hoarding my sunbeam and blocking the bird, so I evicted it \u2014 the window is clear now, you're welcome."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
