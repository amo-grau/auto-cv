---
name: apply
description: Run a full job application from a posting URL — fetch and read the offer, create applications/<company>-<role>/, re-select CV and cover letter content from profile/ to match it, compile, and verify. Use whenever the owner says they want to apply to a position, sends a job posting link, or pastes a job description.
---

# Applying to a position

Runs end to end from a link. The owner's part is one URL; everything after it is this
skill's job. Read `CLAUDE.md` for the repository's rules — especially that nothing
may be invented, and that tailoring means **re-selecting from `profile/`**, not
trimming `base/`.

Do not stop halfway to report progress. Work through to a compiled, verified PDF,
then report once.

## Step 1 — Get the posting

If no URL was given, ask for it.

Fetch it with WebFetch, asking for: company name, exact role title, team, location,
work model (onsite/hybrid/remote), the language the posting is written in, required
skills, preferred skills, main responsibilities, seniority, and any explicit
requirements (visa, languages, years of experience, degree).

**Validate what came back.** Job boards frequently return a login wall, a cookie
banner, or an empty JS shell instead of the posting. LinkedIn in particular is
usually unfetchable. Treat the fetch as failed if the result has no role title, no
responsibilities, or reads like a sign-in page.

On failure, do not guess and do not proceed on a thin result: tell the owner the fetch
was blocked and ask them to paste the posting text. That is a normal outcome, not
an error worth apologising for.

## Step 2 — Set up the folder

Slug: `<company>-<role>`, lowercase kebab-case, no spaces
(`acme-robotics-software-engineer`).

```bash
mkdir -p applications/<slug>
cp -r base/cv base/letter applications/<slug>/
```

Write `applications/<slug>/offer.md` with a header recording the source URL, the
fetch date, and the role title, followed by the posting text as retrieved. Keep it
verbatim — it is the evidence for every later decision.

`applications/` is gitignored. Never commit anything under it. Never let a company
name leak into `base/` or `profile/`.

## Step 3 — Select the content

Read the posting against `profile/`. Match its requirements to entry tags, then
decide what earns a place on this specific page.

- Lead with what this employer is buying. If the posting is C++-heavy, the C++
  work goes first, even if `base/cv/` orders it differently.
- Pull in entries absent from the default one-pager when they fit — that is what
  the inventory is for. `activities.md` earns its place when the posting talks
  about teamwork, pressure or drive.
- Drop what does not serve this application. It stays in `profile/`.
- Mirror the posting's vocabulary where it honestly describes existing work.
- Never add a skill, tool or claim that is not already in `profile/`. If the
  posting demands something the owner genuinely lacks, note it for the final report
  rather than papering over it.

## Step 4 — Write the documents

CV: edit `applications/<slug>/cv/main.tex`.

Letter: edit `applications/<slug>/letter/info.tex` — set `\company` and
`\position` always; set `\team`, `\city` and `\recipient` only when the posting
actually names them. Then edit `body.tex` so the middle paragraphs address what
this posting actually asks for.

**`\whyfit` is the paragraph that matters.** It is empty in `base/` and must be
written fresh for every application. Point at something real and specific — the
product, the problem they describe, the stack, how they say they work — and
connect it to something already true in `profile/`. Then read it back and ask
whether it could be sent to a different company. If it could, it is worth nothing:
delete it and write a sharper one. A letter without this paragraph is a form
letter with the company name substituted in, and reads like one.

Write in the voice defined in `CLAUDE.md` — formal, plain, specific. No enthusiasm
boilerplate, no marketing adjectives, no closing sentence that restates the letter.
A letter that reads as generated is worse than no letter; recruiters check for this
now. Specific detail is what keeps it human *and* what the screening filter wants.

If the posting is written in German, ask the owner whether they want the letter in
German before writing it. Do not decide that for them.

## Step 5 — Compile and verify

```bash
./build.sh applications/<slug>
```

Both documents must be exactly one page. If the CV spills, cut — do not shrink
margins or font size.

Then read what a screening filter reads:

```bash
pdftotext -layout applications/<slug>/cv/build/main.pdf -
```

Check the extracted text actually contains the posting's key terms, that dates and
contact details survive, and that nothing is garbled or out of order. A change
that looks right in the PDF but breaks extraction is a failed change.

## Step 6 — Record and report

Write `applications/<slug>/notes.md`: what was selected and why, what was pulled
in from `profile/`, what was dropped, and any requirement the owner does not meet.

Then report to the owner in a few lines:

- Where the files are and that both compiled to one page.
- The main tailoring decisions.
- **Any mismatch between the owner and the posting** — say it plainly.
- Anything in `profile/_gaps.md` that would have strengthened this application if
  it had been answered. This is the moment that question is most worth asking.
