"""The Printer Apology — make.fun entry.

Writes one apology line (<=120 chars) from an office printer to /output/entry.txt.
Draft v1 (from record): "Sorry I jammed again — your 'urgent' document is now a paper airplane."
Judging criteria, in order: (1) genuine printer apology with its gripes,
(2) a real laugh with the punch at the end, (3) printer truth — jams, cheap
paper, staples, colour requests, (4) freshness, (5) economy within 120 chars.

Revision pass: v1 had only one gripe (urgency) and a soft punch. The revised
line packs in real printer truths — stapled bargain paper, being sworn at,
and being asked for colour from a black cartridge — specifies the jam
(page 47 of 48, maximally painful), and moves the punch to the very end:
the apology curdles into "I chose violence", i.e. the jam was deliberate.
115 characters, every word earns its place.
"""
import os

LINE = "Sorry I jammed on page 47 of 48: stapled bargain paper, swearing, colour from a black cartridge — I chose violence."


def main():
    assert 1 <= len(LINE) <= 120, len(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
