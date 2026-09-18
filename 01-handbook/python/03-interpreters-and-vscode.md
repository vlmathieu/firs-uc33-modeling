# Interpreters in VS Code

*Twenty minutes. The chapter that answers "it works in the terminal but not in VS Code".*

VS Code does not have a Python of its own. Every time it runs your code it hands it to
one of the interpreters installed on your machine, and you choose which. Most
Python problems in this course unit are a mismatch between the one you chose and the
one you installed a package into.

## Shortcuts used in this chapter

| Action | Windows / Linux | macOS |
|---|---|---|
| Command palette | `Ctrl+Shift+P` | `Cmd+Shift+P` |
| New terminal | ``Ctrl+` `` (`Ctrl+ù` on a French keyboard) | ``Ctrl+` `` |
| Extensions panel | `Ctrl+Shift+X` | `Cmd+Shift+X` |
| Settings | `Ctrl+,` | `Cmd+,` |
| Open folder | `Ctrl+K Ctrl+O` | `Cmd+O` |

The command palette is the one to remember. Every VS Code action can be reached by
typing its name there, which is how this handbook refers to them: *Python: Select
Interpreter* means "open the palette, type that, press Enter".

## Extensions: install, enable, update

Extensions panel, search, *Install*:

| Extension | Publisher | Gives you |
|---|---|---|
| **Python** | Microsoft | interpreter selector, run button, error underlining, `Shift+Enter` |
| **Jupyter** | Microsoft | notebooks, interactive window, `# %%` cells |

Installing Python also pulls in Pylance (code intelligence) and Python Debugger. Leave
them installed.

Two things went wrong with extensions this month. An extension can be installed and
switched off: in the panel, a disabled one shows *Enable* instead of a gear. If Python
is disabled, VS Code cannot list your interpreters and falls back on whatever
registered itself system wide, usually Anaconda, which is what happened in issue #3.
And an extension can be out of date: the panel shows a badge with a count when updates
are pending. Update, then run *Developer: Reload Window*.

A third case, for later: with a remote setup (WSL, SSH) an extension can be installed
locally but not on the remote side. It will not concern you this year unless you use
WSL.

## Open the folder, not the file

*File › Open Folder*, and select the project root, the folder holding `data/`, `src/`
and `README.md`. Never double-click a single `.py` file to start working.

Three things depend on it. The terminal opens at the project root, so relative paths
in your scripts resolve, which is what lab 1 relies on. VS Code remembers the
interpreter per folder, so you choose it once. And the file explorer shows the whole
project, which is how you notice that a file landed in the wrong place.

The folder you opened is called the **workspace**. Its name is in the window title.

## Select the interpreter

*Python: Select Interpreter*. A list appears: every Python that VS Code found. Reading
it is a skill.

| Entry looks like | It is |
|---|---|
| `Python 3.12.6 64-bit  ~\AppData\Local\Python\pythoncore-3.12-64\python.exe` | python.org, Install Manager (Windows) |
| `Python 3.12.6 64-bit  /Library/Frameworks/Python.framework/Versions/3.12/bin/python3` | python.org (macOS) |
| `Python 3.12.6 ('uc33': conda)  ~/miniforge3/envs/uc33/bin/python` | your Miniforge environment |
| `Python 3.12.6 ('base': conda)  ~/miniforge3/bin/python` | Miniforge's base, not the one you want |
| `Python 3.13.1 ('base': conda)  C:\ProgramData\anaconda3\python.exe` | Anaconda's base |
| `Python 3.9.6 64-bit  /usr/bin/python3` | the system Python, never this one |
| `Python 3.12.6 ('.venv': venv)  ./.venv/bin/python` | a virtual environment inside the project |

Pick the one whose path matches what you wrote down at the end of chapter 2. If it is
not listed, *Enter interpreter path…* and paste the path. If you are on Path B and see
`base` but not `uc33`, the environment was created after VS Code started: reload the
window.

The choice shows in the **status bar**, bottom right: version number and, for conda,
the environment name in brackets. Look there whenever something is off. It is the
first thing anyone helping you will ask about.

## What the selection changes, and what it does not

Selecting an interpreter changes:

- what the run button ▷ (top right of an open `.py` file) executes with;
- what `Shift+Enter` sends lines to;
- which packages Pylance knows about, so `import pandas` stops being underlined;
- which environment new terminals activate.

It does not change:

- terminals already open, which keep the Python they started with. Close them and open
  a new one;
- the notebook kernel, which has its own selector at the top right of the notebook
  (chapter 5);
- anything outside VS Code. RStudio, a terminal opened from the Start menu, Quarto run
  from the command line: none of them know what VS Code selected.

## The integrated terminal

``Ctrl+` `` opens a terminal inside the workspace folder. With an interpreter
selected, VS Code activates it there: for conda, `(uc33)` appears at the prompt; for a
venv, `(.venv)`; for python.org, nothing visible, but `python` resolves to it.

Open the terminal after selecting the interpreter, or open a new one after changing
it. If the prompt should show `(uc33)` and does not, the activation failed; on Windows
that is nearly always the PowerShell execution policy (chapter 2, Path B).
*Terminal › New Terminal* several times gives several terminals, and the trash icon
closes one. A terminal left over from before an interpreter switch is a common reason
for "installed but not found".

## The check that settles every argument

Three places can run Python inside VS Code. Ask each one who it is.

First, the run button. Create `check.py` in the project:

```python
import sys
print(sys.executable)
print(sys.version)
```

Click ▷. Note the path.

Second, the terminal. In a fresh integrated terminal:

```
python -c "import sys; print(sys.executable)"
```

(`python3` on macOS if you are on Path A.)

Third, the notebook, if you use them. First cell:

```python
import sys
print(sys.executable)
```

If the three paths are identical, you are done: anything you install from that
terminal is visible to scripts and notebooks alike.

If two of them differ, you have found the cause of any `ModuleNotFoundError` you have.
Fix the odd one out. If the terminal differs, close it and open a new one. If the
notebook differs, change the kernel (chapter 5). If the run button differs, run
*Python: Select Interpreter* again and check the status bar.

## Where the choice is stored

VS Code remembers the interpreter per workspace, in its own internal storage, so
opening the same folder next week finds the same one. Opening a different folder
starts from scratch, which is why a new lab sometimes runs on the wrong Python: nobody
chose one for that workspace yet. The status bar tells you.

A project can also set a default in `.vscode/settings.json`, as
`python.defaultInterpreterPath`. That value is an absolute path specific to one
machine, one of the rare places where an absolute path is legitimate, because it
describes that machine only. It must not be shared: keep `.vscode/` out of git, or
commit it only if it contains no path.

## Symptoms and causes

| Symptom | Likely cause | First thing to do |
|---|---|---|
| `ModuleNotFoundError` after a successful install | installed into a different interpreter | the three-way check above |
| `import pandas` underlined in yellow, but the script runs | Pylance uses another interpreter than the run | *Python: Select Interpreter*, reload window |
| `python` not recognised in the terminal, but ▷ works | terminal has no activated environment, or PATH issue | new terminal; on Windows, `py` instead of `python` |
| interpreter list shows only Anaconda | Python extension disabled or outdated | extensions panel, enable, update, reload |
| `(base)` in the prompt instead of `(uc33)` | interpreter selected is base, or terminal predates the selection | status bar, then new terminal |
| works on Monday, broken on Tuesday in a new folder | interpreter not chosen for the new workspace | status bar |
| running scripts is disabled on this system (Windows) | PowerShell execution policy | chapter 2, Path B, step 3 |

## Complementary readings

- *Python environments in VS Code* —
  <https://code.visualstudio.com/docs/python/environments>. The reference for the
  interpreter selector, including how VS Code discovers conda and venv.
- *Getting started with Python in VS Code* —
  <https://code.visualstudio.com/docs/python/python-tutorial>. Twenty minutes, from
  extension install to first run.
- *Terminal basics in VS Code* —
  <https://code.visualstudio.com/docs/terminal/basics>. Several terminals, split,
  which shell, and the ``Ctrl+` `` key.
- *Keyboard shortcuts reference* —
  <https://code.visualstudio.com/docs/getstarted/keybindings>. Printable one-pagers
  per operating system at the bottom.
