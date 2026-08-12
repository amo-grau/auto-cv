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
contains detail only someone who did the work would know. The same flow makes the
repo someone else's: see [Using this for your own CV](#using-this-for-your-own-cv).

**2. Optimize for automated screening.** Most applications are read by a parser or
an LLM filter before a human sees them. The templates are structured to survive
being flattened to plain text: standard section headings, no text in images, no
multi-column layout, consistent dates, and `\pdfgentounicode=1` so glyphs map back
to real characters. The test is `pdftotext -layout` — what it prints is what the
filter reads.

**3. Tailor to a job offer.** I open a session, say I want to apply, and paste a
link. Claude fetches and reads the posting, creates
`applications/<company>-<role>/`, re-selects from the inventory to match it,
compiles both documents and checks them — in one go. Entries missing from my
default CV can appear here; every tagged entry is a candidate. See
[the `apply` skill](.claude/skills/apply/SKILL.md).

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

**On style.** Everything is written to be formal but plain, and never in the
register of a generated cover letter — no "excited about the opportunity", no
"state-of-the-art", no enthusiasm boilerplate. That is not in tension with getting
past automated screening: concrete detail is what filters reward and what reads as
human. The rules are in [CLAUDE.md](CLAUDE.md#voice).

## Layout

Each document is a directory with a `main.tex` inside it.

```
profile/             the inventory — everything, uncut, no page limit
  owner.md           whose CV this is, and where their details live
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

## Using this for your own CV

The repository is built to be cloned. Everything except `profile/` and `base/` is
generic — the templates, the build script and the rules Claude follows work for
anyone.

```bash
git clone https://github.com/amo-grau/auto-cv.git my-cv && cd my-cv
```

Then, in a Claude Code session there:

```
/bootstrap
```

It replaces my information everywhere it lives — the identity record, both LaTeX
documents, the whole inventory, the signature image — then interviews you section
by section and compiles your documents. Expect it to push back: vague answers make
weak CVs, so it asks for the model names, the numbers and the outcomes until each
bullet contains something only you could have written.

Two things to do yourself:

- **Detach the history.** Your clone still contains my CV data in its git history
  and points at my repository. Before pushing anywhere, either `rm -rf .git &&
  git init` or point `origin` at your own empty repo.
- **Add your signature** as `base/letter/sig.jpg`. It is gitignored, and the letter
  compiles without it.

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

Open a session in this repo and say so, with the link:

```
/apply https://boards.example.com/acme/robotics-software-engineer
```

Claude then fetches and reads the posting, saves it verbatim to
`applications/<company>-<role>/offer.md`, copies both documents in, re-selects
their content from `profile/` against what the posting asks for, compiles, checks
that each is one page and that the text still extracts cleanly, and reports what
it changed and any requirement I don't meet.

Some job boards — LinkedIn especially — block automated fetching and return a
login wall. When that happens Claude asks for the posting text pasted in, and
continues from there.

## Privacy

`applications/`, all `*.pdf` files and `sig.jpg` are gitignored. Which companies I
apply to, what their postings say, what I sent them, and my handwritten signature
all stay on this machine. `base/` names no target company, so it is safe to push.

Because the signature is not in the repo, a fresh clone compiles the letter with
blank space where it belongs. Copy `sig.jpg` into `base/letter/` to restore it.
