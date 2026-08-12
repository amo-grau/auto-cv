# Owner

Who this checkout belongs to. Everything in `profile/` and `base/` describes this
person. `CLAUDE.md` says "the owner" and means whoever is named here.

If you cloned this repository to build your own CV, this file is the first thing
to change — run `/bootstrap`, which replaces it along with everything else.

## Identity

- **Name:** Oscar Amo Grau
- **Professional title:** Robotics Software Engineer
- **Location:** Munich, Germany
- **Email:** oscaramog@gmail.com
- **Phone:** +49 15757815031
- **LinkedIn:** linkedin.com/in/oscaramograu
- **GitHub:** github.com/amo-grau
- **Signature file:** `base/letter/sig.jpg` (gitignored, local only)

## Where these values are used

The same details are written into two LaTeX documents. Changing them here means
changing them in both places:

| Field | `base/cv/main.tex` | `base/letter/info.tex` |
| --- | --- | --- |
| Name | header (`\Huge \scshape`) | `\myname` |
| Title | — | `\mytitle` |
| Email | header, in `\href{mailto:…}` **and** the visible text | `\myemail` |
| Phone | header | `\myphone` |
| Location | — | `\mylocation` |
| LinkedIn | header, URL **and** visible text | `\mylinkedin` |
| GitHub | header, URL **and** visible text | — |

The email, LinkedIn and GitHub entries in the CV header each appear twice: once
as the link target and once as the text shown. Change both. A mismatch there is
invisible in the PDF and sends the reader to the wrong place — this repository
shipped exactly that bug, with a `mailto:x@x.com` under a correct-looking address.

## Job search context

- Targeting robotics and software engineering roles, primarily in Munich.
- Work authorisation, notice period and salary expectations: not recorded. Add
  them here if an application ever needs them.
