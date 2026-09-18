# Key concepts

*Fifteen minutes. Everything else in this handbook uses these words.*

If you are new to programming, read this chapter twice: once now, once after chapter 4.
Each term below has a French equivalent in the
[glossary](https://github.com/vlmathieu/firs-uc33-modeling/blob/main/02-reference/glossary-en-fr.md).

## The one idea

A package is never installed "on your computer". It is installed into one specific
Python, and only that Python can use it.

Almost every Python problem raised in this course unit so far comes down to that
sentence. Keep it in mind while reading the rest.

## Program, interpreter, script

A **program** is a file containing instructions. Your computer cannot read Python
directly: it needs a translator.

The **interpreter** is that translator. It is itself a program, a file on your disk
called `python.exe` on Windows and `python3` on macOS and Linux. When you "run Python",
you start that file, and it reads your instructions one line at a time and carries
them out.

A **script** is a text file, extension `.py`, containing Python instructions from top
to bottom. You give it to the interpreter, the interpreter executes it, then stops.
`python my_script.py` means: "interpreter, execute this file".

One machine can hold several interpreters. Each is a separate file in a separate
folder and knows nothing about the others. This is normal, and it is where most of the
confusion comes from. Chapter 2 explains how they get there.

## Module, package, library

A **module** is one `.py` file that you load into your own code with `import`.
`import math` loads the module `math`, which comes with Python.

A **package** is a folder of modules distributed together under one name. `pandas` is
a package: `import pandas` gives you hundreds of modules at once.

A **library** is the informal word for either. People say "the pandas library" and
"the pandas package" and mean the same thing. R uses the same two words, with one
trap: in R, `library()` *loads* a package, it does not install it.

The **standard library** is the set of modules that comes with every Python: `math`,
`csv`, `pathlib`, `json`, `datetime` and a few hundred more. They need no installation.
Anything else, pandas included, is a **third-party package** and has to be installed.

## Install versus import

Two different operations, done in different places and at different frequencies.

| | What it does | Where | How often |
|---|---|---|---|
| install | copies the package files onto your disk, inside one interpreter's folder | the terminal | once per interpreter |
| import | loads an installed package into the running session | the script, the console, the notebook | every session |

`ModuleNotFoundError: No module named 'pandas'` is an import failing. It means: the
interpreter running this line looked in its own folder and found no pandas there. It
does not mean pandas is absent from your machine. It may be installed into another
interpreter.

## pip and conda

A **package manager** is the tool that installs packages. Python has two in common
use.

**pip** comes with every Python from python.org. It downloads packages from **PyPI**
(the Python Package Index, <https://pypi.org>), a public repository of about 600 000
packages. Its command is `python -m pip install <name>`.

**conda** comes with Anaconda, Miniconda and Miniforge. It downloads from **channels**,
the main one being **conda-forge**. conda can install Python itself, and things that
are not Python at all: R, GDAL, compilers. Its command is `conda install <name>`.

The two do not know about each other. Mixing them inside one interpreter is possible
but is the classic way to break one. Chapter 4 gives the rule.

## Environment

An **environment** is one interpreter plus the packages installed into it, taken as a
unit. Every interpreter on your machine is, in that sense, an environment.

The word is used more precisely for environments you create on purpose, so that two
projects can have different versions of the same package without conflict. conda
does this with `conda create`; plain Python does it with `venv`. In this course unit
one environment is enough. You need to recognise the word because error messages,
tutorials and VS Code use it constantly.

An environment is **activated** when the terminal has been told to use it: typing
`python` then runs that environment's interpreter rather than another. The name of the
active environment usually appears in brackets at the start of the prompt:
`(uc33) C:\Users\...>`.

## Kernel

A **kernel** is an interpreter running in the background, waiting for instructions,
and keeping in memory everything it has computed so far. Notebooks use kernels. When
you run a cell, the notebook sends the cell's code to the kernel, and the kernel sends
back the result.

The kernel is one specific interpreter. In VS Code, selecting a kernel for a notebook
and selecting an interpreter for scripts are two different settings, and they can
disagree. Chapter 5 shows how to check.

Because a kernel keeps everything in memory, it can hold a variable your file no
longer defines, or an old version of a package you have just updated. *Restart
kernel* empties it. Do that more often than feels necessary.

## Terminal, console, REPL

The **terminal** is the window where you type commands to the operating system:
`cd`, `ls`, `python`, `git`. Its prompt ends in `$`, `%` or `>`. The
[terminal cheatsheet](https://github.com/vlmathieu/firs-uc33-modeling/blob/main/02-reference/terminal-cheatsheet.md)
covers it.

The **Python console**, also called the **REPL** (read, evaluate, print, loop), is
what you get after typing `python` in the terminal: a prompt `>>>` where you type
Python, one line at a time. `exit()` leaves it.

The two are easy to confuse, and confusing them produces two classic errors:

| You typed | Where | What happens |
|---|---|---|
| `python -m pip install pandas` | at `>>>` | `SyntaxError`: that is a terminal command, not Python |
| `import pandas` | at `$` or `>` | `command not found`: that is Python, not a terminal command |

Look at the prompt before typing. `>>>` means Python; anything else means the
terminal.

## PATH

When you type `python` in a terminal, the terminal does not search your disk. It goes
through a short list of folders, in order, and runs the first `python` it finds. That
list is the **PATH**.

Two consequences:

- `command not found` (macOS, Linux) or `is not recognized as an internal or external
  command` (Windows) means no folder on the PATH contains that program. Either it is
  not installed, or it is installed somewhere the PATH does not list.
- If two Pythons are on the PATH, the first one wins, silently. Chapter 3 shows how to
  find out which one that is.

## Extension

VS Code on its own knows nothing about Python. An **extension** is an add-on that
teaches it a language. The **Python** extension (publisher: Microsoft) adds the
interpreter selector, the run button, error underlining. The **Jupyter** extension
adds notebooks. Both must be installed, enabled and up to date. An extension that is
disabled is a common cause of "VS Code picked the wrong Python" (chapter 3).

## Traceback

When Python hits an error it prints a **traceback**: the chain of function calls that
led there, oldest at the top, the failing line at the bottom, then the error message.
Chapter 7 shows how to read it. For now: the message is at the bottom, but the file
paths in the middle tell you which interpreter ran the code, which is often all you
need to know.

## Summary table

| Term | One line |
|---|---|
| interpreter | the program that executes Python; several can coexist |
| script | a `.py` file executed top to bottom |
| module, package, library | reusable code you `import`; a package is a folder of modules |
| standard library | the packages that ship with Python |
| install / import | copy onto disk once / load into the session every time |
| pip, conda | the two package managers |
| PyPI, conda-forge | where each one downloads from |
| environment | one interpreter and its packages, as a unit |
| kernel | an interpreter running behind a notebook, holding state |
| terminal, console | operating system prompt / Python prompt `>>>` |
| PATH | the list of folders the terminal searches for commands |
| extension | what teaches VS Code a language |
| traceback | the error report; read the paths, not only the last line |

## Complementary readings

- *Python Modules and Packages*, Real Python —
  <https://realpython.com/python-modules-packages/>. Longer than needed, clear on the
  module/package distinction.
- *Installing Python Modules*, official documentation —
  <https://docs.python.org/3/installing/>. Short, and it states the "one Python, one
  set of packages" rule in its own words.
- *Python environments*, xkcd 1987 — <https://xkcd.com/1987/>. A drawing of the
  problem this handbook solves. Funnier once you have lived it.
- Glossary of this course unit —
  <https://github.com/vlmathieu/firs-uc33-modeling/blob/main/02-reference/glossary-en-fr.md>.
