# Profile — the inventory

Everything the owner has done that could ever belong on a CV, with no page limit and
no editing for length. This is the **content source of truth**.

`base/cv/main.tex` is not the inventory. It is one rendering of it: a general
purpose one-pager. A tailored CV is a *different* selection from the same
inventory, chosen to match a specific posting.

```
profile/            everything, uncut          <- add here first, always
  ↓ select
base/cv/            default one-pager
  ↓ select + reorder
applications/…/cv/  one-pager for one posting
```

The point: nothing is ever lost because it did not fit. An entry cut from the CV
stays here and can come back for the next posting that rewards it.

## Format

One `##` heading per entry. Every entry carries:

- **When** — absolute dates, `MM.YYYY` or a year range.
- **Where** — employer/institution and location, when applicable.
- **Tags** — lowercase keywords used to match an entry against a posting. Be
  generous: tags cost nothing and are what makes selection work.
- Bullets in **full detail** — longer and more specific than any CV would fit.
  Trimming happens at render time, not here.

Write bullets so a shorter version can be derived by deletion. Put the outcome
and the number in the first clause.

## Rules

- Only what the owner has confirmed. Same truthfulness bar as everywhere else in this
  repo — an unverified detail belongs in `_gaps.md`, not in an entry.
- Never delete an entry because it is currently irrelevant. Irrelevant today is
  the right fit two postings from now.
- Never name a target company here. This directory is public.
- When something new happens, it lands here first, and only then propagates to
  `base/cv/`.

## `_gaps.md`

Open questions — entries missing the number, scope or outcome that would make
them strong. Working through that file is the cheapest way to improve every
future CV at once.
