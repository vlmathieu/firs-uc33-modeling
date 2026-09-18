# Running code

*Fifteen minutes. Five ways to run Python in VS Code, and what each one silently
assumes.*

## The five ways

| Way | How | Runs on | Working directory | Use it for |
|---|---|---|---|---|
| Run button ▷ | top right of an open `.py` | selected interpreter | workspace root | running a whole script, the normal case |
| Terminal | `python src/script.py` | whatever `python` resolves to in that terminal | wherever the terminal is | the same, and it is what a colleague or a server would do |
| Line or selection | `Shift+Enter` in a `.py` | selected interpreter | workspace root | trying one line, inspecting a variable |
| Interactive window | `# %%` cells in a `.py`, *Run Cell* | selected interpreter, as a kernel | workspace root | exploring step by step while keeping a script |
| Notebook | `.ipynb`, *Run Cell* | the kernel chosen top right | the notebook's own folder | exploration, teaching, not deliverables |

The traps are all in two columns, *Runs on* and *Working directory*.

## Run button

Open the script, click ▷ (*Run Python File*). VS Code opens a terminal, activates the
selected interpreter, and types `python <full path to the file>` for you. The output
appears in that terminal.

The command runs from the workspace root, whatever folder the script sits in. So a
script in `src/` that reads `data/raw/file.csv` works, as long as you opened the
project folder (chapter 3). If you opened a single file instead, "the workspace root"
is wherever VS Code decided, and relative paths break. Most of the "file not found"
errors of lab 1 came from there.

The dropdown next to ▷ offers *Run Python File in Dedicated Terminal*, which keeps one
terminal per script. Harmless; use it if the shared one gets noisy.

## Terminal

```
python src/01_import.py
```

`py src/01_import.py` on Windows if `python` is not recognised; `python3` on macOS
Path A. Path B: `(uc33)` must show in the prompt first.

Run it from the project root, which is where the VS Code terminal opens if you
opened the folder. `pwd` tells you where you are. This is the way that transfers: a
server, a colleague's machine, a Quarto document, an automated job all run scripts
this way, and none of them has a ▷ button. Lab 3's brief asks for this form for that
reason.

`Ctrl+C` interrupts a script that is running too long.

## A line at a time: `Shift+Enter`

With the cursor on a line of a `.py` file, `Shift+Enter` sends that line, or the
selected block, to a Python console in the terminal, and moves the cursor down. The
console stays open: variables persist, so you can send the imports once, then a line,
look at the result, send the next.

Two consequences, both met in lab 1. The console is not running a file, so `__file__`
does not exist and `Path(__file__)` raises `NameError`; in the console, use
`Path.cwd()` instead, after checking that `cwd` is the project root. And the console
remembers: a variable defined ten minutes ago, then deleted from the file, is still
there. When something works in the console and not when the file is run from the top,
that is usually why. Close the console (type `exit()`) and run the file with ▷ before
trusting anything.

## Interactive window: `# %%`

A comment line `# %%` in a `.py` file marks a cell. *Run Cell* appears above it
(and `Ctrl+Enter` / `Cmd+Enter` runs the current cell, `Shift+Enter` runs it and
moves to the next). Output goes to an interactive window beside the file: tables
render, plots display, variables can be inspected.

```python
# %%
import pandas as pd
from pathlib import Path

# %%
trade = pd.read_csv(Path.cwd() / "data" / "raw" / "comtrade_fr_roundwood_clean.csv")
trade.head()

# %%
trade.groupby("year").primaryValue.sum()
```

This is the middle ground: the comfort of a notebook, and the file is still a script
that runs top to bottom with ▷ or from a terminal, because `# %%` is just a comment
to Python. It needs the Jupyter extension and the `ipykernel` package in the selected
interpreter; VS Code offers to install the latter the first time, and you should let
it.

The same caution as above applies: the window keeps state. *Restart* it (icon at the
top of the window) and run all cells before concluding that the script works.

## Notebooks

A `.ipynb` file: cells of code and text, with the output stored inside the file. Good
for exploring and for teaching, and not the format of a deliverable in this course
unit, for reasons given below.

The kernel is chosen separately from the interpreter. Top right of the notebook,
*Select Kernel*, then *Python Environments…*, then the interpreter. This is not the
same setting as *Python: Select Interpreter*, and the two can disagree. The kernel name shown top right
is what runs your cells; the status bar is what runs your scripts. Issue #3 was a
notebook running on Anaconda's kernel while the interpreter selector said something
else.

Make this the first cell of every notebook:

```python
import sys
print(sys.executable)
```

If the path is not the one you expect, change the kernel before doing anything else.

The working directory is the notebook's folder, not the workspace root. A notebook
in `notebooks/` reading `data/raw/file.csv` fails; it must read `../data/raw/file.csv`,
or, better, locate the project root explicitly. The scripts in this course unit use
`Path(__file__).resolve().parents[1]`; a notebook has no `__file__`, so use
`Path.cwd().parent` or keep notebooks at the project root.

Notebooks hide state. Cells can be run in any order, and the file remembers outputs
from runs whose code no longer exists. The only honest test is *Restart Kernel and Run
All* (icons at the top). Do it before showing a notebook to anyone, including yourself
tomorrow.

Installing from a notebook is `%pip install` (chapter 4), then restart the kernel.

As for deliverables: a notebook mixes code, output and metadata in one JSON file,
which git cannot diff readably, which runs differently depending on cell order, and
which cannot be executed from a terminal without conversion. A script can be run,
diffed, tested and scheduled. Explore in a notebook if you like; when it works, move
the code into a `.py` (VS Code: `…` menu, *Export*, *Python Script*) and make it run
top to bottom. That is the version you hand in, or a Quarto document that calls it.

## Which one, when

| You want to | Use |
|---|---|
| run the whole thing and see if it works | ▷, or terminal |
| check what a line does before writing the next | `Shift+Enter` |
| explore a dataset, look at tables and plots as you go | `# %%` cells |
| write a document with narrative around the results | Quarto, with Python chunks |
| follow a tutorial that is distributed as a notebook | notebook |
| hand in the work | a script, or a Quarto document; never a notebook alone |

## Shortcuts

| Action | Windows / Linux | macOS |
|---|---|---|
| Run current file | ▷ button, or `Ctrl+F5` | ▷, `Ctrl+F5` |
| Run line or selection | `Shift+Enter` | `Shift+Enter` |
| Run cell (`# %%` or notebook) | `Ctrl+Enter` | `Cmd+Enter` |
| Run cell and go to next | `Shift+Enter` | `Shift+Enter` |
| Interrupt in a terminal | `Ctrl+C` | `Ctrl+C` |
| Interrupt a kernel | ■ icon | ■ icon |
| Comment / uncomment line | `Ctrl+/` | `Cmd+/` |

## Complementary readings

- *Run Python code in VS Code* —
  <https://code.visualstudio.com/docs/python/run>. The ▷ button, the terminal, the
  interactive window, with the settings behind each.
- *Jupyter notebooks in VS Code* —
  <https://code.visualstudio.com/docs/datascience/jupyter-notebooks>. Kernel
  selection, cell operations, export to script.
- *Python interactive window* —
  <https://code.visualstudio.com/docs/python/jupyter-support-py>. The `# %%`
  convention in full.
- *Why I don't like notebooks*, Joel Grus, JupyterCon 2018 —
  <https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI/>.
  The classic argument, as slides, funny and fair. Read it before deciding notebooks
  are the answer to everything.
