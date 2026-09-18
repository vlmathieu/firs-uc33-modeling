# Checklist

*One page. Print it, or keep it open.*

## Before opening an issue: five commands

Run them in the VS Code terminal of the project, after selecting the interpreter,
and paste the complete output into the issue. They answer the questions that are
otherwise asked one at a time over three days.

Windows, Linux and macOS on Path B (on macOS Path A, replace `python` with `python3`):

```
python --version
python -c "import sys; print(sys.executable)"
python -m pip --version
python -c "import pandas; print(pandas.__version__, pandas.__file__)"
conda env list
```

The last line is for Path B; on Path A it says `command not found`, which is also an
answer. Replace `pandas` with the package that is failing.

Add, if the problem is in a notebook, the output of the first cell:

```python
import sys
print(sys.executable)
```

And the complete error message, as text, from `Traceback` to the last line.

## The three-way check

The same path must come out of all three; if not, you have found the problem.

| Where | How | Prints |
|---|---|---|
| run button ▷ | `check.py` with `import sys; print(sys.executable)` | |
| terminal | `python -c "import sys; print(sys.executable)"` | |
| notebook | first cell, same two lines | |

Fix the odd one out: terminal, open a new one; notebook, *Select Kernel*; ▷,
*Python: Select Interpreter*.

## Symptoms, one line each

| Symptom | Go to |
|---|---|
| `ModuleNotFoundError` after a successful install | three-way check; chapter 4 |
| `command not found` / `not recognized` for `python` | chapter 2, PATH; on Windows try `py` |
| `(base)` in the prompt, not `(uc33)` | `conda activate uc33`; status bar; chapter 3 |
| running scripts is disabled (Windows) | chapter 2, Path B, execution policy |
| `FileNotFoundError` on a relative path | open the *folder*; `Path.cwd()`; chapter 5 |
| `NameError: __file__` | you are in a console; chapter 5 |
| works in the notebook, not as a script (or the reverse) | kernel ≠ interpreter; chapter 5 |
| worked yesterday, not today, different folder | interpreter not chosen for this workspace; status bar |
| pip prints a `WARNING` about PATH | ignore; chapter 4 |
| a wall of red compile output | no wheel for your Python, or missing system library; chapter 4 |
| `SSL: CERTIFICATE_VERIFY_FAILED` (macOS) | *Install Certificates.command*; chapter 2 |
| `externally-managed-environment` (Linux) | do not force; conda or venv; chapter 2 |
| `import pandas` underlined, script runs | Pylance on another interpreter; reload window |
| interpreter list shows only Anaconda | Python extension disabled or outdated; chapter 3 |
| `UnicodeDecodeError` | `encoding="latin-1"`; chapter 6 |
| `SyntaxError` with a caret | the line above; chapter 6 |

## Habits that prevent most of it

1. Open the folder, never a lone file.
2. Look at the status bar before running anything.
3. `python -m pip`, never `pip`. Path B: `conda activate uc33` first.
4. New terminal after changing interpreter.
5. `sys.executable` as the first cell of every notebook.
6. Restart the kernel or console before believing a result.
7. Read the traceback: last line, first `File` that is yours, the paths.
8. In a long log, the first `error` is the cause.
9. Warnings are advice, not failures.
10. One Python per machine, or know at all times which one is running.

## Shortcuts, both systems

| | Windows / Linux | macOS |
|---|---|---|
| command palette | `Ctrl+Shift+P` | `Cmd+Shift+P` |
| terminal | ``Ctrl+` `` (`Ctrl+ù` French keyboard) | ``Ctrl+` `` |
| extensions | `Ctrl+Shift+X` | `Cmd+Shift+X` |
| run line / selection | `Shift+Enter` | `Shift+Enter` |
| run cell | `Ctrl+Enter` | `Cmd+Enter` |
| interrupt (terminal) | `Ctrl+C` | `Ctrl+C` |
| comment line | `Ctrl+/` | `Cmd+/` |
| search in all files | `Ctrl+Shift+F` | `Cmd+Shift+F` |

## Command palette entries worth memorising

- *Python: Select Interpreter*
- *Developer: Reload Window*
- *Terminal: Create New Terminal*
- *Jupyter: Restart Kernel*
- *Convert Indentation to Spaces*
