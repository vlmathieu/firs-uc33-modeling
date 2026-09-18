# Installing packages

*Fifteen minutes. The chapter behind issues #2 and #3.*

## The rule

Install with the Python that will run the code. The operation is never "install
pandas"; it is "install pandas into this interpreter". Everything below is a way of
making sure the two are the same.

Two habits enforce it without thinking. Never type bare `pip`; type `python -m pip`
(`python3 -m pip` on macOS Path A). And before installing from a terminal, look at the
prompt: `(uc33)` if you are on Path B, and no `>>>`.

`python -m pip` means "run the pip that belongs to *this* python". Bare `pip` runs
whichever pip is first on the PATH, which may belong to another interpreter. The two
drift apart on machines with several Pythons, and yours has several whether you know
it or not.

## Path A: pip

In the VS Code terminal, after selecting the interpreter (chapter 3):

| | Command |
|---|---|
| Windows | `python -m pip install pandas` |
| Windows, target a specific version | `py -3.12 -m pip install pandas` |
| macOS | `python3 -m pip install pandas` |
| Linux, venv activated | `python -m pip install pandas` |

Several packages at once: `python -m pip install pandas matplotlib openpyxl`. A specific
version: `python -m pip install "pandas==2.2.3"`. At least a version:
`"pandas>=2.0"`. The quotes protect `>` from the shell.

Other verbs you will need:

```
python -m pip install --upgrade pandas     # newer version
python -m pip uninstall pandas             # remove
python -m pip list                         # everything installed in this interpreter
python -m pip show pandas                  # version, location, dependencies
```

Never `sudo pip` on macOS or Linux. It installs into the system Python, which is not
yours, and is the one way to actually damage a machine with pip.

## Path B: conda

Activate the environment first:

```
conda activate uc33
conda install pandas
```

Miniforge fetches from conda-forge by default. With Miniconda or Anaconda, say so
explicitly, `conda install -c conda-forge pandas`, or set the channel once as in
chapter 2.

Several packages: `conda install pandas matplotlib geopandas`. A version:
`conda install "pandas=2.2"` (one `=`, not two). Other verbs:

```
conda update pandas
conda remove pandas
conda list                   # everything in the active environment
conda list pandas            # one package
conda env list               # environments on this machine, * marks the active one
```

If a package is not on conda-forge, pip works inside a conda environment:

```
conda activate uc33
python -m pip install some_package
```

Two rules keep this from breaking the environment. Install with conda everything you
can first, and use pip last, only for what conda does not have. After pip has been
used in an environment, go back to `conda install` only for packages that do not
overlap with what pip brought in. If an environment does get into a mess, delete it
and recreate it (`conda env remove -n uc33`, then chapter 2 again). It takes five
minutes, and being disposable is the point of an environment.

## From a notebook

A notebook runs on a kernel, and a terminal command does not know which kernel. Install
from inside the notebook instead, in a cell:

```python
%pip install pandas
```

or, for conda environments:

```python
%conda install pandas
```

The `%` makes it a notebook command rather than Python. It installs into the kernel
that is running the cell, so there is nothing to get wrong. Then restart the kernel:
a package imported before the install stays at the old version until the process
restarts, and a package installed during a session may not be importable until it
does.

## Reading the output

pip and conda print a lot. Read from the bottom.

| Last meaningful line | Meaning |
|---|---|
| `Successfully installed pandas-2.2.3 numpy-2.1.1 ...` | done; the list is the package and what it pulled in |
| `Requirement already satisfied: pandas in ...` | already there, in this interpreter; the path tells you which |
| `WARNING: The script xyz.exe is installed in ... which is not on PATH` | done; the package also ships a command-line tool, which you will not use. Not an error. Issue #2 |
| `ERROR: No matching distribution found for pandsa` | typo in the name, or no version exists for your Python or your system |
| `ERROR: Could not find a version that satisfies the requirement` | same thing, said differently |
| `error: externally-managed-environment` | Linux system Python refusing. Use conda or a venv, chapter 2. Do not add `--break-system-packages` |
| `error: Microsoft Visual C++ 14.0 or greater is required` | no wheel for your Python version, pip tried to compile. See *When it fails* |
| `error: command 'gcc' failed` or `fatal error: xyz.h: No such file` | same on macOS or Linux |
| `PackagesNotFoundError` (conda) | not on your channels; try `-c conda-forge`, then pip |

Warnings are advice. Errors stop things. The verdict is the last block, and it is one
of `Successfully installed`, `Requirement already satisfied`, or `ERROR`.

Package names are case-insensitive to pip but write them lowercase, as the
documentation does. And the name you install is not always the name you import:

| Install | Import |
|---|---|
| `scikit-learn` | `import sklearn` |
| `pillow` | `import PIL` |
| `pyyaml` | `import yaml` |
| `opencv-python` | `import cv2` |
| `beautifulsoup4` | `import bs4` |
| `python-dateutil` | `import dateutil` |

`ModuleNotFoundError: No module named 'sklearn'` after `pip install sklearn` is a
mistake this table prevents: the real package is `scikit-learn`.

## Verify

The install said it worked. Now prove the *right* interpreter can see it:

```
python -c "import pandas; print(pandas.__version__); print(pandas.__file__)"
```

A version number, then a path. That path must sit under the interpreter you selected
in VS Code. Compare with `sys.executable` from chapter 3:

| Distribution | `sys.executable` | packages live in |
|---|---|---|
| python.org, Windows | `...\pythoncore-3.12-64\python.exe` | `...\pythoncore-3.12-64\Lib\site-packages\` |
| python.org, macOS | `.../Versions/3.12/bin/python3` | `.../Versions/3.12/lib/python3.12/site-packages/` |
| conda env, Windows | `...\miniforge3\envs\uc33\python.exe` | `...\miniforge3\envs\uc33\Lib\site-packages\` |
| conda env, macOS/Linux | `.../miniforge3/envs/uc33/bin/python` | `.../miniforge3/envs/uc33/lib/python3.12/site-packages/` |
| venv | `.../uc33-env/bin/python` | `.../uc33-env/lib/python3.12/site-packages/` |

`site-packages` is the folder. One per interpreter. If `pandas.__file__` points into a
different tree than `sys.executable`, you have two interpreters in play, and chapter 3
tells you which to fix.

## When the install fails

Three causes cover nearly all of it.

The most common is that there is no wheel for your Python: you are on the newest
version and the package has not published pre-compiled files for it yet. pip then
tries to compile from source, which needs a C compiler and usually fails. The sign is a
long log ending in `error: Microsoft Visual C++ 14.0 or greater is required`, or in
`gcc` errors. Fixes, in order: install the package from conda-forge if you are on
Path B; pin an older version that has a wheel, `python -m pip install "package<X"`;
wait a few weeks; or use a Python one version older. Open an issue with the full log
and we will tell you which.

On Linux, the cause can be a missing system library: `cannot find -lsomething` or
`fatal error: something.h: No such file or directory` in the log. The fix is a `-dev`
package from `apt`, not from pip: `sudo apt install libsomething-dev`. Issue #5 is the
R version of this and reads the same way.

The third is a typo, or the wrong name: `No matching distribution found`. Check the
spelling on <https://pypi.org>, and check the install-versus-import table above.

In all three cases, the cause is in the first `ERROR` or `error:` line of the log, not
the last. Everything after it is fallout. Chapter 7 has more on reading long logs.

## Listing what a project needs

A script that says `import pandas` without saying which pandas is not reproducible.
The minimum, and what this course unit asks for, is a `requirements.txt` at the
project root:

```
pandas>=2.0
matplotlib>=3.8
openpyxl
```

Anyone, including you on a new machine, installs everything in one line:

```
python -m pip install -r requirements.txt
```

conda's equivalent is an `environment.yml` and `conda env create -f environment.yml`.
Either is fine; write one of them and mention it in the README. Lab 1 shows where it
sits in the project layout.

## Complementary readings

- *Installing packages*, Python Packaging User Guide —
  <https://packaging.python.org/en/latest/tutorials/installing-packages/>. The
  canonical explanation of `python -m pip`, and why.
- *pip user guide* — <https://pip.pypa.io/en/stable/user_guide/>. Requirements files,
  version specifiers, what `--upgrade` does.
- *Managing packages*, conda documentation —
  <https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-pkgs.html>.
- *Using pip in an environment*, conda documentation —
  <https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html#using-pip-in-an-environment>.
  The official statement of the "conda first, pip last" rule.
- *Installing Python packages from a Jupyter notebook*, Jake VanderPlas —
  <https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/>.
  Why `!pip` in a notebook goes wrong and `%pip` does not. Older than `%pip` itself,
  which was created because of this post.
