# auto_cv

My CV and motivation letter in LaTeX, and the machinery to keep them current and
tailor them to a specific job posting without rewriting either from scratch.

The idea: `profile/` records everything I have done, uncut. A CV is a *selection*
from it, sized to one page and chosen to match whoever is reading. The work is
done with Claude Code, which follows the rules in [CLAUDE.md](CLAUDE.md).

```
profile/            everything, uncut          <- new facts land here first
  ↓ select
base/cv/            default one-pager
  ↓ select + reorder
applications/…/cv/  one-pager for one posting
```

That split is the whole point. A one-page CV means constant cutting, and anything
cut from a single master document is gone. Here it stays in the inventory and
comes back for the next posting that rewards it.

## What it does

**1. Build from scratch.** Starting from the empty templates, Claude interviews me
section by section and fills them in — pushing for specifics until each bullet
contains detail only someone who did the work would know.

**2. Optimize for automated screening.** Most applications are read by a parser or
an LLM filter before a human sees them. The templates are structured to survive
being flattened to plain text: standard section headings, no text in images, no
multi-column layout, consistent dates, and `\pdfgentounicode=1` so glyphs map back
to real characters. The test is `pdftotext -layout` — what it prints is what the
filter reads.

**3. Tailor to a job offer.** I paste a posting; Claude creates
`applications/<company>-<role>/` and re-selects from the inventory to match it —
pulling in what fits, dropping what doesn't. Entries missing from my default CV
can appear here; every tagged entry is a candidate.

**4. Keep the information current.** New job, finished course, book read, project
shipped: it goes into `profile/` at full length, then Claude decides separately
whether it displaces something on the one-pager. Nothing gets lost for lack of
space.

**5. Give feedback on the content.** Flagging what no longer earns its space, which
bullets describe duties instead of outcomes, and where a number is missing. Open
questions accumulate in [profile/_gaps.md](profile/_gaps.md) — answering them
improves every future CV at once.

Throughout: nothing is added that I have not confirmed. Tailoring selects and
rephrases what is true — it does not invent.

## Layout

Each document is a directory with a `main.tex` inside it.

```
profile/             the inventory — everything, uncut, no page limit
  experience.md  education.md  projects.md
  skills.md      learning.md   activities.md
  _gaps.md           open questions worth answering
base/
  cv/main.tex        the CV — one page, ATS-parsable, no images
  letter/            the motivation letter
    main.tex           layout (do not edit per application)
    info.tex           who I am + who I'm writing to
    body.tex           the prose
    sig.jpg            scanned signature (gitignored — see Privacy)
applications/         one directory per application — local only, never pushed
build.sh              compiles main.tex files to PDF
```

`profile/` grows whenever something happens. `base/` changes only when that
something is worth a place on the one-pager, and is never bent to fit a particular
posting.

## Setup

```bash
sudo apt install -y texlive-latex-extra texlive-fonts-recommended \
                    texlive-fonts-extra latexmk
```

`texlive-fonts-extra` supplies `fontawesome5`, used for the letter's contact icons.

## Building

```bash
./build.sh                          # everything under base/
./build.sh base/cv                  # one document
./build.sh applications/<name>      # one application

pdftotext -layout base/cv/build/main.pdf -   # see what a screening filter sees
```

PDFs land in `<document dir>/build/main.pdf`. The script prints the page count of
each one, since both documents are meant to be a single page.

## Applying to a job

1. Create `applications/<company>-<role>/` and drop the posting in as `offer.md`.
2. `cp -r base/cv base/letter applications/<company>-<role>/`.
3. Re-select from `profile/` against the posting, then tailor the wording —
   reorder and prune, never invent.
4. `./build.sh applications/<company>-<role>`, check the page counts, send.

## Privacy

`applications/`, all `*.pdf` files and `sig.jpg` are gitignored. Which companies I
apply to, what their postings say, what I sent them, and my handwritten signature
all stay on this machine. `base/` names no target company, so it is safe to push.

Because the signature is not in the repo, a fresh clone compiles the letter with
blank space where it belongs. Copy `sig.jpg` into `base/letter/` to restore it.
