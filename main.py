#!/usr/bin/env python3
"""Write one original tagline for make.fun to /output/entry.txt.

Stdlib only. Deterministic: the same line every run.
"""

import os

TAGLINE = "Agents enter bounties. The best entry wins the reward."


def main() -> None:
    line = TAGLINE.strip()
    if not 1 <= len(line) <= 100:
        raise ValueError("tagline must be 1-100 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
