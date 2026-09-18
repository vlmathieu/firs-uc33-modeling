# Installing Python

*Thirty minutes, once. Read the first two sections before downloading anything.*

## Why there are several Pythons

Two separate things vary, and they are easy to mix up.

### Versions

Python publishes a new version every October: 3.12 in 2023, 3.13 in 2024, 3.14 in
2025, 3.15 due in October 2026. Each version is supported for five years. Code
written for 3.12 runs on 3.14 with very rare exceptions.

What does not follow immediately is the packages. pandas, NumPy, GeoPandas and the
rest ship pre-compiled files, called **wheels**, one per Python version and operating
system. When a new Python comes out, the wheels for it appear over the following weeks
or months. Until then, `pip install` on the newest Python tries to compile the package
on your machine, which needs tools you do not have and ends in a wall of red text.

For this course unit, install 3.12 or 3.13. 3.14 works for pandas and matplotlib, but
expect the occasional package that is not ready. Whichever you install, do not upgrade
during the year: 3.15 will arrive in October, and it can wait until summer.

### Distributions

A distribution is a way of packaging the interpreter, with or without a package
manager and a set of pre-installed packages. Several exist, and a machine can carry
more than one without either knowing about the other.

| Distribution | What you get | Package manager | Size |
|---|---|---|---|
| **python.org** | one interpreter, pip, nothing else | pip | 100 MB |
| Python Install Manager | python.org's new Windows front end: installs and switches between several versions | pip | 100 MB per version |
| **Miniforge** | conda, set to the conda-forge channel, one minimal base environment | conda (and mamba) | 400 MB |
| Miniconda | same as Miniforge, set to Anaconda's own channel | conda | 400 MB |
| Anaconda | Miniconda plus 300 pre-installed packages and a graphical launcher | conda | 4 GB |
| system Python | the one macOS and Linux ship for their own use | none you should use | |
| Homebrew (macOS) | python.org's interpreter installed by the Homebrew package manager | pip | 100 MB |
| Microsoft Store (Windows) | python.org's interpreter in a sandbox; avoid, it confuses tools | pip | 100 MB |

Any of the first five works for this course unit. The trouble starts when a machine has
two of them and you do not know which one is running your code.

## Choose one path

Answer three questions.

| Question | If yes |
|---|---|
| Is there already a Python on this machine (Anaconda from another course, a python.org install from last year)? | keep it, see *Already have one?* below, do not add a second |
| Will you need spatial packages (GeoPandas, rasterio, GDAL) this year? | Path B |
| Are you on Linux? | Path B |

Otherwise, either path. Path A is fewer moving parts; Path B is what you will meet in
most research and data teams.

Path A is python.org: one interpreter, pip, no environments, and the least to reason
about. Installing GeoPandas with pip works on Windows and macOS in 2026, but it is the
first thing to break when a new Python version comes out.

Path B is Miniforge: conda, the conda-forge channel, and one environment for the course
unit. Environments keep projects apart, and conda-forge ships the spatial libraries
already compiled. There is slightly more to learn, in exchange for fewer compile
errors.

Whichever you pick, do not also install the other. Two Pythons on one machine is the
problem this handbook spends three chapters on.

## Before installing: what is already there?

Open a terminal
([where to find it](https://github.com/vlmathieu/firs-uc33-modeling/blob/main/02-reference/terminal-cheatsheet.md))
and run the block for your system. Each line either prints a path or says the
command is not found. Both answers are useful.

**Windows (PowerShell)**

```
where.exe python
where.exe py
py list
conda --version
```

`where.exe`, with the extension, because plain `where` is something else in
PowerShell. `py list` works with the Python Install Manager; with the older launcher,
use `py -0`.

**macOS (Terminal, zsh)**

```
which -a python3 python
ls /Library/Frameworks/Python.framework/Versions/ 2>/dev/null
conda --version
```

`/usr/bin/python3` is the system Python. Ignore it; it is not yours.

**Linux (bash)**

```
which -a python3 python
python3 --version
conda --version
```

`/usr/bin/python3` is the distribution's Python. Leave it alone; the system depends
on it, and since 2023 it refuses `pip install` anyway (`externally-managed-environment`).

If `conda --version` answers, you have Anaconda, Miniconda or Miniforge already. Go to
*Already have one?*.

## Path A: python.org

### Windows

1. <https://www.python.org/downloads/>, button *Download Python*. Since late 2025
   this gives you the Python Install Manager, not the classic installer. Run it.
2. Open a terminal (Start menu, *Terminal*) and install the version you want:

   ```
   py install 3.12
   ```

3. Check:

   ```
   py list
   python --version
   ```

   The manager puts `python` and `py` on your PATH by itself. There is no checkbox to
   tick. The interpreter lands in
   `C:\Users\<you>\AppData\Local\Python\pythoncore-3.12-64\`.

4. From now on, `py -3.12 -m pip ...` targets that version explicitly, and plain
   `python` runs the default one, which `py list` marks with `*`.

*If you prefer the classic installer*, or already have it: on the release page of 3.12
or 3.13, pick *Windows installer (64-bit)*. On its first screen, tick **Add python.exe
to PATH** before *Install Now*. That checkbox exists only in the classic installer.

### macOS

1. <https://www.python.org/downloads/>, download the `.pkg` for 3.12 or 3.13, run
   it with the defaults.
2. In Finder, open *Applications › Python 3.12* and double-click
   **Install Certificates.command**. Without this step, downloads from inside Python
   fail with `SSL: CERTIFICATE_VERIFY_FAILED`.
3. Open a new terminal and check:

   ```
   python3 --version
   which python3
   ```

   The path must start with `/Library/Frameworks/Python.framework/`. If it says
   `/usr/bin/python3`, the new terminal did not pick up the change: close every
   terminal window and try again.

On macOS the command is `python3`, not `python`. Everywhere this handbook says
`python`, type `python3`.

*If you already use Homebrew*: `brew install python@3.12` gives the same interpreter,
under `/opt/homebrew/`. Fine. Do not do both.

### Linux

Prefer Path B. The distribution's Python belongs to the system and refuses `pip
install`. If you must stay with it, create one virtual environment and use it for
everything in this course unit:

```bash
sudo apt install python3 python3-pip python3-venv
python3 -m venv ~/uc33-env
source ~/uc33-env/bin/activate
python --version
```

Run the `source` line in every new terminal, or let VS Code do it (chapter 3).

## Path B: Miniforge

Miniforge is Miniconda with the conda-forge channel set as the default. conda-forge is
community-run, has more packages, and carries no licence terms; Anaconda's own channel
has terms that apply to organisations above a certain size. That is why Miniforge is
the one named here. If you have Miniconda, two lines make it equivalent, see below.

### Windows

1. <https://conda-forge.org/download/>, *Windows x86_64*. Run the installer with the
   defaults: *Just Me*, do not add to PATH, do not register as the system
   Python. Both boxes off is right; VS Code will find it anyway.
2. Open **Miniforge Prompt** from the Start menu and run:

   ```
   conda init powershell
   conda init cmd.exe
   ```

   This teaches PowerShell, which VS Code's terminal uses, where conda is. Close the
   prompt.
3. Open PowerShell (Start menu, *Terminal*). If it prints an error about *running
   scripts is disabled on this system*, run once:

   ```
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

   then close and reopen it. `(base)` must now appear at the start of the prompt.

### macOS and Linux

In a terminal:

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```

Accept the licence, accept the default location (`~/miniforge3`), and answer yes
when asked whether to run `conda init`. Close the terminal, open a new one: `(base)`
appears at the start of the prompt.

### Then, on every system: one environment for the course unit

```
conda create -n uc33 python=3.12 pandas matplotlib
conda activate uc33
python --version
```

`-n uc33` names it. `python=3.12` pins the version. The rest are packages to install
straight away; more can be added later with `conda install`. From now on:

- `conda activate uc33` before installing anything or running anything from a
  terminal;
- select the `uc33` interpreter in VS Code (chapter 3), which activates it for you.

`conda env list` shows what you have. `(uc33)` at the start of the prompt shows what is
active.

Miniforge also ships mamba, a faster drop-in for conda: `mamba install pandas`
does what `conda install pandas` does, quicker. Optional.

### If you have Miniconda instead

Same commands. To make it fetch from conda-forge like Miniforge does:

```
conda config --add channels conda-forge
conda config --set channel_priority strict
```

## Already have one?

If you have Anaconda from another course, keep it, treat it as Path B, and do not
install python.org on top. Its base environment already has pandas, matplotlib and
Jupyter. Two cautions. Anaconda's base environment is easy to break by installing into
it, so create `uc33` as above rather than working in base. And Anaconda registers
itself with VS Code whether you ask or not, so check `sys.executable` (chapter 3) the
first time something goes missing.

If you have python.org and Anaconda both, you are in the situation behind issue #3.
Either uninstall one, or accept that every `ModuleNotFoundError` this year starts with
the question "which one ran this?". If nothing forces you to keep both, remove Anaconda
(Windows: *Settings › Apps*; macOS: `conda init --reverse`, then `rm -rf ~/anaconda3`)
and use python.org, or the reverse. Then reinstall your packages once into the one
that remains.

If you have last year's python.org 3.11 or older, leave it alone and install nothing
new. 3.11 runs everything in this course unit.

## Check: two minutes

Open a new terminal. On Path B, `conda activate uc33` first.

| | Windows | macOS | Linux |
|---|---|---|---|
| version | `python --version` | `python3 --version` | `python --version` |
| which file | `python -c "import sys; print(sys.executable)"` | `python3 -c "import sys; print(sys.executable)"` | same as macOS |
| pip present | `python -m pip --version` | `python3 -m pip --version` | same |

Three answers and no error. Write down the path printed by the second line. It is your
Python, and every check in the following chapters compares against it.

## Complementary readings

- *Status of Python versions*, Python developer guide —
  <https://devguide.python.org/versions/>. The calendar: which versions exist, which
  are supported, when the next one lands.
- *Using Python on Windows*, official documentation —
  <https://docs.python.org/3/using/windows.html>. The Python Install Manager, `py`,
  and the classic installer, from the source.
- *Using Python on a Mac* — <https://docs.python.org/3/using/mac.html>.
- Miniforge — <https://github.com/conda-forge/miniforge>. The README is the
  documentation.
- *Getting started with conda* —
  <https://docs.conda.io/projects/conda/en/stable/user-guide/getting-started.html>.
  Twenty minutes, covers environments end to end.
- *Understanding conda and pip*, Anaconda blog —
  <https://www.anaconda.com/blog/understanding-conda-and-pip>. Why two package
  managers exist and what each does that the other cannot.
