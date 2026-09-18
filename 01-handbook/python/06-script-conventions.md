# Writing a script

*Twenty minutes. The syntax you need for this course unit, and the conventions the
repository follows.*

This is not a Python course. It is the minimum to read and write the scripts used in
the labs, plus the rules that keep them running on someone else's machine. For the
language itself, see the readings at the end; for R equivalents of every line, the
[R / Python / Julia sheet](https://github.com/vlmathieu/firs-uc33-modeling/blob/main/02-reference/r-python-julia-equivalents.md).

## The shape of a script

Every script in this course unit has the same four sections, in this order. The lab 1
solution, unabridged:

```python
# ---------------------------------------------------------------
# 01_import.py -- extract France's roundwood trade from the raw file
# ---------------------------------------------------------------

# --- Dependencies ---
from pathlib import Path
import pandas as pd

# --- Parameters ---
ROOT    = Path(__file__).resolve().parents[1]   # project root
COUNTRY = "France"

# --- Body ---
trade = pd.read_csv(ROOT / "data" / "raw" / "comtrade_fr_roundwood_clean.csv")

# partnerDesc == "World" is the all-partners aggregate.
france = trade[(trade.reporterDesc == COUNTRY) & (trade.partnerDesc != "World")]

# --- Output ---
france.to_csv(ROOT / "data" / "processed" / "trade_france.csv", index=False)
```

| Section | Holds | Why separate |
|---|---|---|
| header | file name, one line on what it does, inputs and outputs if not obvious | the reader decides in five seconds whether this is the file they want |
| Dependencies | every `import`, and nothing else | a reader sees at once what must be installed; Python resolves names before running anything |
| Parameters | values someone might want to change: paths, a country, a year, a threshold | change one line at the top, not a value buried at line 80 |
| Body | the work | |
| Output | what is written to disk | the reader knows what files this script produces without running it |

A script must run from an empty session, top to bottom, with ▷ or `python
src/01_import.py` from the project root. If it only works after you ran three other
things in a console, it is not finished.

## Indentation is the syntax

Python has no braces. A block is whatever is indented under the line ending in a colon:

```python
for year in [2020, 2021, 2022]:
    subset = trade[trade.year == year]
    print(year, len(subset))
print("done")            # back at column 0: outside the loop
```

Four spaces per level. VS Code inserts them when you press Tab in a `.py` file, so you
never type spaces. Two errors come from this:

- `IndentationError: expected an indented block`: a line ends in `:` and the next one
  is not indented;
- `IndentationError: unindent does not match any outer indentation level`, or
  `TabError`: tabs and spaces mixed, usually from pasting code from a web page. Select
  all, *Convert Indentation to Spaces* from the command palette.

## Names

| Thing | Style | Example |
|---|---|---|
| variables, functions, files | `snake_case` | `trade_france`, `clean_units()`, `01_import.py` |
| parameters at the top of a script | `UPPER_CASE` | `ROOT`, `COUNTRY`, `MIN_YEAR` |
| packages you import | lowercase, with the usual alias | `import pandas as pd`, `import numpy as np` |

No accents, no spaces, no hyphens inside a name (`trade-france` is a subtraction).
Start with a letter, not a digit, inside Python; script *files* may start with a digit
for ordering, and they do here.

Do not name a file after a package. A script called `pandas.py`, `csv.py`,
`random.py` or `test.py` in your project shadows the real module: `import pandas` then
loads your file, and the error message (`AttributeError: module 'pandas' has no
attribute 'read_csv'`) says nothing about why. Same for a folder named `pandas/`.

## Imports

At the top, one per line, standard library first, then third-party:

```python
from pathlib import Path        # standard library
import pandas as pd             # third-party
import matplotlib.pyplot as plt
```

`import pandas as pd` loads the package and gives it a short name; you then write
`pd.read_csv`. `from pathlib import Path` takes one name out of a module so you can
write `Path` alone. Never `from pandas import *`: it dumps hundreds of names into your
script and nobody, including you, can tell where `concat` came from.

The alias conventions (`pd`, `np`, `plt`) are universal. Use them: every example on
the internet does.

## Paths

Use `pathlib.Path`, build paths with `/`, and compute everything from the project root:

```python
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]      # the script is in src/, root is one up
raw = ROOT / "data" / "raw" / "trade.csv"
out = ROOT / "data" / "processed" / "trade_clean.csv"

raw.exists()          # True or False: check before reading
out.parent.mkdir(parents=True, exist_ok=True)   # create the folder if needed
```

`/` between a `Path` and a string joins them with the right separator for the system.
Forward slashes in a string literal also work on Windows: `"data/raw/trade.csv"` is
fine everywhere. Backslashes are not: `"data\raw\trade.csv"` contains `\r` and `\t`,
which are a carriage return and a tab. If you must paste a Windows path, prefix it
with `r` for *raw*: `r"C:\Users\me\file.csv"`. Then delete it, because absolute paths
are not allowed in scripts in this course unit.

Two things to never write:

- `os.chdir(...)`, Python's `setwd()`. It changes the working directory for everything
  that follows and makes the script depend on where it was started from;
- an absolute path, `C:/Users/julie/...` or `/home/aitor/...`. It works on one
  machine, yours, and the point of a script is that it works on others.

`Path(__file__)` only exists when running a file. In a console or a notebook use
`Path.cwd()`, after checking that `cwd` is the project root (chapter 5).

## Strings

Single or double quotes, no difference; pick double, the repository does. Text inside
a string with `{}` and an `f` prefix inserts variables:

```python
country = "France"
year = 2022
print(f"{country}, {year}: {len(france)} rows")
```

Multiplying, dividing or comparing a string that looks like a number does not work:
`"12" + 1` is a `TypeError`. `int("12")` and `float("12.5")` convert. pandas reads a
column as text when one cell in it is not a number, and that is the most common reason
a numeric column refuses arithmetic (lab 2).

## Blocks you will meet

```python
if len(france) == 0:                 # == compares; = assigns
    raise ValueError("no rows for France")
elif len(france) < 100:
    print("few rows, check the filter")
else:
    print("ok")

for col in ["qty", "netWgt"]:        # loop over a list
    print(col, trade[col].isna().sum())

def to_tonnes(kg):                   # a function: def, name, arguments, colon, indent
    """Convert kilograms to tonnes."""
    return kg / 1000

trade["net_t"] = to_tonnes(trade["netWgt"])   # applied to the whole column at once
```

The last line is the pattern that matters most for data work. Write operations on
whole columns, not loops over rows. `trade["netWgt"] / 1000` is one line and runs in
compiled code; a `for` loop doing the same thing row by row is ten lines and a hundred
times slower. Reach for a loop only when the thing you loop over is a list of files, of
years, of column names, not the rows of a table.

`True`, `False`, `None`: capitalised. Test for `None` with `is None`, not `== None`.
Test for missing values in pandas with `.isna()`, because `NaN == NaN` is `False`.

## Lines that go on

Python ends a statement at the end of the line, except inside brackets. So long
expressions break naturally inside parentheses:

```python
france = trade[
    (trade.reporterDesc == COUNTRY)
    & (trade.partnerDesc != "World")
    & (trade.year >= MIN_YEAR)
]
```

No backslash needed. Keep lines under about 90 characters; VS Code shows a ruler if you
ask it to.

## Comments

`#` to the end of the line. Say why, not what: `# partnerDesc == "World" is the
all-partners aggregate` tells the reader something the code does not. `# filter the
data frame` above a line that visibly filters a data frame tells them nothing.

A function gets a one-line docstring, a string right after `def`, as `to_tonnes` above.
`help(to_tonnes)` prints it.

## Encoding

Save files as UTF-8; VS Code does by default (bottom right of the status bar says
`UTF-8`). Python source is UTF-8, so accents in comments and strings are fine. Data
files are another matter: a CSV exported from Excel in France is often `latin-1` or
`cp1252`, and `read_csv` then fails with `UnicodeDecodeError`. The fix is
`pd.read_csv(path, encoding="latin-1")`, and a line in the README saying so.

## Syntax errors you will make

| Message | Cause |
|---|---|
| `SyntaxError: expected ':'` | missing colon after `if`, `for`, `def`, `else` |
| `SyntaxError: '(' was never closed` | unbalanced brackets; VS Code highlights the pair, count them |
| `SyntaxError: invalid syntax` pointing at `=` | `=` where `==` was meant, inside a condition |
| `SyntaxError: Missing parentheses in call to 'print'` | Python 2 code, `print "x"`; write `print("x")` |
| `SyntaxError: unterminated string literal` | a quote opened and not closed, often because of an apostrophe inside `'...'` |
| `IndentationError` | see above |

A `SyntaxError` is reported before anything runs, and the caret `^` points at or
just after the problem. Often the real mistake is on the line above.

## Complementary readings

- *PEP 8, Style Guide for Python Code* — <https://peps.python.org/pep-0008/>. The
  conventions above come from here. Skim the sections on naming and imports.
- *pathlib*, official documentation —
  <https://docs.python.org/3/library/pathlib.html>. Everything `Path` can do.
- *Python's pathlib module: taming the file system*, Real Python —
  <https://realpython.com/python-pathlib/>. The friendlier version of the above.
- *10 minutes to pandas* —
  <https://pandas.pydata.org/docs/user_guide/10min.html>. The column-at-a-time way of
  thinking, in the words of the people who built it.
- *Think Python*, chapters 1 to 8 — <https://allendowney.github.io/ThinkPython/>. If
  the blocks section above went too fast.
