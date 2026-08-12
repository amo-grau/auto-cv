# auto_cv

LaTeX sources for Oscar Amo Grau's CV and motivation letter, plus per-application
tailored versions.

This repository is the source of truth for both documents. They are edited here,
not anywhere else.

## Layout

Every document is a directory containing a `main.tex`.

```
base/                   master documents — the superset of everything true
  cv/main.tex
  letter/               main.tex + info.tex (variables) + body.tex (prose) + sig.jpg
applications/
  <company>-<role>/     one directory per job application
    offer.md            the job posting, pasted verbatim
    notes.md            what was changed and why
    cv/
    letter/
build.sh                latexmk wrapper
```

`applications/` is gitignored in full — it is local-only and never pushed.

The letter splits cleanly: `info.tex` holds the per-application variables
(`\company`, `\position`, `\team`, `\city`, `\recipient`) and `body.tex` holds the
prose. Tailoring a letter is mostly editing those two files.

## Workflow when a job offer arrives

1. Create `applications/<company>-<role>/` and save the posting to `offer.md`.
2. `cp -r base/cv base/letter applications/<company>-<role>/`.
3. Tailor the copies to the offer (see rules below).
4. `./build.sh applications/<company>-<role>` and check the PDFs.
5. Record the reasoning in `notes.md`.

`base/` is only edited when something genuinely changes in real life (a new job,
a new skill, a new course) — never to fit a specific posting.

## Tailoring rules

- **Never invent or inflate.** No experience, tool, employer, date, or metric that
  isn't already in `base/` or confirmed by Oscar. Tailoring means selecting,
  reordering, and rephrasing what is true — nothing else.
- Mirror the posting's own vocabulary where it honestly describes existing work
  (e.g. posting says "computer vision" and the bullet says "vision-based AI models").
- Reorder and prune bullets so the most relevant ones come first; drop the least
  relevant rather than adding new ones.
- Reorder the Skills lists to lead with what the posting asks for. Do not add a
  skill just because the posting names it.
- **The CV must stay on one page.** `build.sh` prints the page count of every PDF
  it produces — check it.
- The letter is one page. Always set `\company` and `\position`; set `\team` and
  `\recipient` only when the posting actually names them (an unset `\team` leaves
  "the team", which reads fine).
- Keep the CV ATS-parsable: no images, no multi-column layout, no text in
  graphics. `\pdfgentounicode=1` stays. (The letter's `sig.jpg` is fine — letters
  are usually read by a human.)

## Compiling

```bash
# once
sudo apt install -y texlive-latex-extra texlive-fonts-recommended \
                    texlive-fonts-extra latexmk
./build.sh                              # everything in base/
./build.sh applications/<company>-<role>
```

`texlive-fonts-extra` is needed for the letter's `fontawesome5` icons.

## What must never be published

`applications/` is gitignored in full, and so is every PDF and `sig.jpg` (the
handwritten signature). Job postings, the companies applied to, the documents
actually sent, and the signature are private and stay out of git history. Never
commit them, never move company-specific content into `base/`, and never name a
target company in `base/` — `\company`, `\city`, `\team` and `\position` are
deliberately blank there.

The letter wraps its `\includegraphics{sig.jpg}` in `\IfFileExists` so a clone
without the signature still compiles. Keep that guard.
