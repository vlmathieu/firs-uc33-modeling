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

## c. Python 3.12 or 3.13

*Section revised on 2026-09-18. The emailed version described a checkbox that the
current Windows installer no longer has.*

Two ways, both fine. Pick **one**, and do not install the other on top: two Pythons on
one machine is the cause of most of the questions asked so far. If a Python is already
installed (Anaconda from another course, for instance), keep it and skip this step.
The handbook says [how to check](../01-handbook/python/02-install.md) and
[which to choose](../01-handbook/python/02-install.md#choose-one-path).

**Path A — python.org.** <https://www.python.org/downloads/>

> **Windows.** The download is now the *Python Install Manager*, not the classic
> installer. Run it, then in a terminal type `py install 3.12`. It puts `python` and
> `py` on your PATH by itself: **there is no longer a checkbox to tick.** If you use
> the classic *Windows installer (64-bit)* from a release page instead, that one
> still has the **"Add python.exe to PATH"** box on its first screen; tick it.

> **macOS.** Install it anyway: the Python shipped with the system is old and reserved
> for macOS's own use. After the installer, open *Applications › Python 3.12* and
> double-click **Install Certificates.command**. The command is `python3`, not
> `python`.

> **Linux.** Prefer Path B: the distribution's Python belongs to the system and refuses
> to install packages.

**Path B — Miniforge.** <https://conda-forge.org/download/>

conda, the conda-forge channel, and environments. The better choice if you will need
spatial packages (GeoPandas, GDAL) this year, and the one to take on Linux. Install
with the defaults, then in a terminal:

```
conda create -n uc33 python=3.12 pandas matplotlib
conda activate uc33
```

Windows users open *Miniforge Prompt* from the Start menu first and run
`conda init powershell` once. Details, and what `(uc33)` in the prompt means, in the
[handbook](../01-handbook/python/02-install.md#path-b-miniforge).

## d. VS Code

<https://code.visualstudio.com/Download>

Then **four extensions**, through the Extensions icon in the sidebar
(`Ctrl+Shift+X` on Windows, `Cmd+Shift+X` on macOS):

| Extension | Publisher |
|---|---|
| **Python** | Microsoft |
| **Jupyter** | Microsoft |
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

On macOS with Path A, `python3 --version`. On Path B, `conda activate uc33` first.

**Each must return a version number.** If one answers `command not found` (macOS) or
`is not recognized as an internal or external command` (Windows), then either the
program is not installed, **or** it is installed but the terminal cannot find it. For
Python, the handbook's [chapter 2](../01-handbook/python/02-install.md) walks through
it; on Windows, try `py --version` before concluding anything.

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
