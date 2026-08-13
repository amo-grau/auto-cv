#!/usr/bin/env python3
"""Turn `pdftotext -layout` output into text that can be pasted into a form.

A PDF stores text one visual line at a time, so copying from a viewer — or
running pdftotext — puts a line break wherever the line happened to wrap. Every
PDF behaves this way; no change to the LaTeX source prevents it.

This joins wrapped lines back into whole sentences so a paste box or an AI tool
receives running prose. Used by build.sh to write <doc>/build/main.txt next to
the PDF.

A line continues the previous one only when all of these hold:

  * the previous line ran nearly to the right margin — text only wraps when the
    line above it was full, which is what separates a wrapped sentence from a
    short section heading like "Experience",
  * the previous line does not end a sentence,
  * the previous line is not a two-column row (a wide run of spaces means a
    heading with a date or location on the right),
  * this line does not start a bullet,
  * this line does not start a "Label: value" entry, as Skills lines do.

The tests run against the original pdftotext line, not the tidied output:
tidying collapses the column gaps that the two-column test depends on.

Read from stdin, write to stdout.
"""
import re
import sys

WIDE_GAP = re.compile(r"\S {3,}\S")          # "Job title        Sep 2023"
BULLET = re.compile(r"^\s*[•–−*]\s")  # bullet or en-dash sub-bullet
LABEL = re.compile(r"^\s*[A-Z][A-Za-z0-9 /&+#.-]{1,40}:\s")
ENDS_SENTENCE = (".", ";", ":", "!", "?", ")")
FULL_LINE = 70                               # chars; the layout is ~110 wide


def continues(previous: str, line: str) -> bool:
    """Is `line` the continuation of a sentence wrapped from `previous`?"""
    previous = previous.rstrip()
    return (
        len(previous) >= FULL_LINE
        and not previous.endswith(ENDS_SENTENCE)
        and not WIDE_GAP.search(previous)
        and not BULLET.match(line)
        and not LABEL.match(line)
    )


def tidy(line: str) -> str:
    """Strip indentation and turn column gaps into a visible separator."""
    return re.sub(r" {3,}", "  |  ", line.strip())


def reflow(text: str) -> str:
    out: list[str] = []       # tidied output
    source: list[str] = []    # the pdftotext line each output line came from

    for raw in text.splitlines():
        if not raw.strip():
            if out and out[-1]:
                out.append("")
                source.append("")
            continue

        if out and out[-1] and continues(source[-1], raw):
            joined = out[-1]
            # Repair a word pdftotext split across the line break.
            if joined.endswith("-"):
                out[-1] = joined[:-1] + raw.strip()
            else:
                out[-1] = joined + " " + raw.strip()
            source[-1] = raw          # the tail is what the next line wraps from
        else:
            out.append(tidy(raw))
            source.append(raw)

    return "\n".join(out).strip() + "\n"


if __name__ == "__main__":
    sys.stdout.write(reflow(sys.stdin.read()))
