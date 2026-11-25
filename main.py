"""Worst Superpower — one-line entry (program/v1, python3.13).

Writes the superpower to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR when set).
The entry is a fixed original line; the program is deterministic.
"""
import os

ENTRY = "I can summon rain indoors, but only directly above my own head, one drop at a time."

def main():
    # Gate self-check (revision edit): sealed gate wants 1-140 chars, non-blank, one line.
    assert 1 <= len(ENTRY) <= 140 and ENTRY.strip() and "\n" not in ENTRY, "entry fails the 1-140 char gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
