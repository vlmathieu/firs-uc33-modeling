# Reading errors

*Fifteen minutes. An error message is information. This chapter is how to extract it.*

## A traceback, dissected

Run this from the project root with a misspelt column:

```python
import pandas as pd
from pathlib import Path

trade = pd.read_csv(Path("data/raw/comtrade_fr_roundwood_clean.csv"))
france = trade[trade.reporter_desc == "France"]
```

Python prints:

```
Traceback (most recent call last):
  File "/Users/you/uc33-lab1/src/01_import.py", line 5, in <module>
    france = trade[trade.reporter_desc == "France"]
  File "/Users/you/miniforge3/envs/uc33/lib/python3.12/site-packages/pandas/core/generic.py", line 6299, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'reporter_desc'
```

Four things to read, in this order.

The last line is the error: its type, `AttributeError`, then the message. Here the
message is complete on its own: the data frame has no column `reporter_desc`. The real
name is `reporterDesc`, and `trade.columns` would have shown it.

Then the first `File` line that is yours, `src/01_import.py, line 5`. That is where to
put the cursor. The lines below it are inside packages, and the bug is almost never
there.

Then the paths. Every `File` line names a folder, and `.../miniforge3/envs/uc33/...`
says which interpreter ran this code, more reliably than anything VS Code displays.
When a package is "installed but not found", the paths in the traceback tell you where
Python looked; compare them with where you installed and you usually have your answer.
In issue #3 every path began with `C:\ProgramData\anaconda3` while the student had
installed into python.org.

Last, the order. *Most recent call last* means the top is where execution started and
the bottom is where it died. Read bottom-up for the cause and top-down to follow how
it got there.

A traceback in a notebook or the interactive window looks the same, with more
decoration and often a few frames from IPython at the top. Skip those.

## The errors of this course unit

| Error | Says | Usually means | First move |
|---|---|---|---|
| `ModuleNotFoundError: No module named 'pandas'` | this interpreter has no pandas | installed into another interpreter, or not at all | chapter 3 three-way check, then chapter 4 |
| `ModuleNotFoundError: No module named 'sklearn'` | same | installed under a different name, or a file of yours shadows the package | chapter 4 name table; look for `sklearn.py` in your folder |
| `FileNotFoundError: [Errno 2] No such file or directory: 'data/raw/trade.csv'` | no such file *from where Python is standing* | wrong working directory, or a typo in the path | `Path.cwd()`, `Path("data/raw").exists()`, and compare with the file explorer |
| `NameError: name 'pd' is not defined` | this name was never assigned in this session | the `import` line was not run, or was run in another console | run the file from the top |
| `NameError: name '__file__' is not defined` | not running a file | `Shift+Enter` or a notebook | `Path.cwd()` there; `Path(__file__)` in the script |
| `AttributeError: 'DataFrame' object has no attribute 'X'` | no column or method called `X` | typo, wrong case, or the column has spaces | `trade.columns` |
| `KeyError: 'X'` | no key `X` | same as above, for `trade["X"]` | `trade.columns` |
| `TypeError: unsupported operand type(s) for /: 'str' and 'int'` | arithmetic on text | a numeric column read as text because one cell is not numeric | `trade.dtypes`, then find the offending cell (lab 2) |
| `ValueError: could not convert string to float: 'N/A'` | conversion met text | a missing-value marker pandas did not recognise | `na_values=`, lab 2 |
| `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9` | the file is not UTF-8 | Excel export, `latin-1` | `encoding="latin-1"` |
| `PermissionError: [Errno 13]` | cannot write the file | it is open in Excel, or the folder is read-only | close Excel |
| `IndentationError`, `SyntaxError` | Python could not even parse the file | chapter 6 | the line above the caret |
| `SettingWithCopyWarning` | not an error | you modified a slice of a data frame | `.copy()` after the filter, or `.loc[...] = ...`; harmless until it is not |
| `RecursionError`, `MemoryError` | ran out of stack or memory | rare here; usually a loop that should be a vectorised operation | chapter 6, the column-at-a-time pattern |

## Warnings are not errors

A warning is printed and execution continues. `WARNING:` from pip,
`FutureWarning` from pandas, `DeprecationWarning` from anything: they say "this will
change" or "this looks odd", not "this failed". Read them once, understand them, and
stop worrying. The exception is `SettingWithCopyWarning`, which sometimes flags a real
bug where a modification silently went to a copy; the fix is in the table.

An error stops the program. The last line of the output is the test: a traceback
ending in `SomethingError` is an error; anything else is not.

## Long logs: read the first error

An installation log, a compile log, a Quarto render log can be five hundred lines.
Python tracebacks put the cause at the bottom; build logs put it at the top. The
sequence is: something fails, then everything that depended on it fails, then a
summary line at the end names the last failure, which is a consequence.

Issue #5 was fifteen lines of fallout ending in `there is no package called 'DHARMa'`,
with the actual cause, `cannot find -llapack`, near the top. Same in Python: `error:
subprocess-exited-with-error` at the bottom of a pip log means "scroll up to the first
line starting with `error:` or `fatal error:`, that one is the cause".

Search the log for `rror` (which catches `Error`, `error:`, `ERROR`). The first hit is
the one to read.

## Chained exceptions

Sometimes two tracebacks are printed, separated by:

```
The above exception was the direct cause of the following exception:
```

or *During handling of the above exception, another exception occurred*. The first
one is the original problem; the second is a package trying to explain it. In issue
#3 the first said `No module named 'vegafusion'` and the second gave the install
command. Read both, act on the first.

## Then what

The four-step method from
[how to ask a question](https://github.com/vlmathieu/firs-uc33-modeling/blob/main/00-admin/how-to-ask-a-question.md):

1. **Read** the error. Last line, first `File` line that is yours, the paths.
2. **Read the documentation** of the function on that line: `help(pd.read_csv)`, or
   hover over it in VS Code.
3. **Search** the last line, with your own names stripped out: `AttributeError:
   'DataFrame' object has no attribute` finds the answer; `... 'reporter_desc'` finds
   nothing, because nobody else has your column.
4. **Ask**, with the complete traceback as text, `sys.executable`, and the five lines
   of chapter 8.

## Complementary readings

- *Understanding the Python traceback*, Real Python —
  <https://realpython.com/python-traceback/>. Long, and covers every common exception
  type with an example.
- *Errors and exceptions*, the official tutorial —
  <https://docs.python.org/3/tutorial/errors.html>. Shorter, exact.
- *Built-in exceptions* — <https://docs.python.org/3/library/exceptions.html>. What
  each error type means, when you meet one not in the table above.
- *Returning a view versus a copy*, pandas documentation —
  <https://pandas.pydata.org/docs/user_guide/indexing.html#returning-a-view-versus-a-copy>.
  The `SettingWithCopyWarning`, explained by the people who emit it.
