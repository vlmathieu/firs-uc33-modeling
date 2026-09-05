# Machine prerequisites — what to install

*Version of 4 September 2026. Emailed before the first session.*

Allow **45 minutes to 1 hour**. Wherever nothing is said, keep the installer defaults.

Install in order: R before RStudio, otherwise RStudio has nothing to drive.

---

## a. R

<https://cloud.r-project.org/>

Pick your system, then the **base** link.

## b. RStudio Desktop

<https://posit.co/download/rstudio-desktop/>

Free version. **After R.**

## c. Python 3.12 or later

<https://www.python.org/downloads/>

> **Windows — the one checkbox that matters.** On the installer's first screen, tick
> **"Add python.exe to PATH"** before clicking *Install*. It is not ticked by default.
> Without it Python installs correctly but stays invisible from the terminal, and you
> will spend an hour wondering why.

> **macOS.** Install it anyway. The Python shipped with the system is old and reserved
> for macOS's own internal use.

## d. VS Code

<https://code.visualstudio.com/Download>

Then **three extensions**, through the Extensions icon in the sidebar
(`Ctrl+Shift+X` on Windows, `Cmd+Shift+X` on macOS):

| Extension | Publisher |
|---|---|
| **Python** | Microsoft |
| **R** | REditorSupport |
| **Quarto** | Quarto |

## e. Quarto

<https://quarto.org/docs/get-started/>

## f. git

<https://git-scm.com/downloads>

git is not taught until October. Install it **now** anyway: it will save about
45 minutes on 20 October, and installation is the only part that can go wrong.

- **Windows**: every default option, without exception. The installer asks a lot of
  questions; the answers it proposes are the right ones.
- **macOS**: type `git --version` in the Terminal. macOS will offer to install it
  for you.

## g. A GitHub account

<https://github.com/signup>

Free.

> Use **`firstname-lastname`** as your username rather than a nickname. This account
> will follow you: it will appear on your CV, and a recruiter will look at it. A
> readable profile is an asset.

Then request the **GitHub Student Pack** with your AgroParisTech address:
<https://education.github.com/pack>

---

## Check — 2 minutes

Open a terminal.

- **Windows**: Start menu → *Terminal* or *PowerShell*
- **macOS**: Applications › Utilities › Terminal

Type the three commands below, one at a time:

```
python --version
git --version
quarto --version
```

**Each must return a version number.** If one answers `command not found` (macOS) or
`is not recognized as an internal or external command` (Windows), then either the
program is not installed, **or** it is installed but the terminal cannot find it —
most often the PATH checkbox missed at step (c).

Finally, open RStudio and VS Code once each, to check they start.

---

## If you get stuck

Do not stay stuck alone until the last minute. Open an issue on this repository
([→ form](https://github.com/vlmathieu/firs-uc33-modeling/issues/new/choose)) stating:

1. your operating system;
2. the exact step that fails;
3. **the complete error message**, copied as text.

This is not a formality: being able to describe a problem usefully is part of the
syllabus, and you will practise it all year.
See [`how-to-ask-a-question.md`](how-to-ask-a-question.md).

If you are not an administrator on your machine and cannot install anything, say so:
there is a solution.
