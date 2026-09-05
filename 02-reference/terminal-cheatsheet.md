# Cheatsheet — the terminal, survival level

A window where you **type the name of a program instead of clicking its icon**. That
is all it is. The oldest interface there is, and the most precise.

## Where to find it

| System | Where |
|---|---|
| Windows | Start menu → *Terminal* or *PowerShell* |
| macOS | Applications › Utilities › Terminal |
| RStudio | the **Terminal** tab, next to the Console |
| VS Code | ``Ctrl+` `` (or menu *Terminal* → *New Terminal*) |

Most of the time you will not open it separately: it lives inside your editor.

## The five gestures

| What you want | macOS / Linux | Windows (PowerShell) |
|---|---|---|
| Where am I? | `pwd` | `pwd` |
| What is in here? | `ls` | `ls` or `dir` |
| Go into a folder | `cd folder_name` | same |
| Go up one level | `cd ..` | same |
| Run a script | `Rscript script.R` · `python script.py` | same |

**A terminal is always somewhere.** In a folder. That is the most important point on
this page: most "file not found" errors come from there.

## The key to remember before all others

**TAB.**

Type the first three letters of a file or folder name, press TAB, and the terminal
completes it. It prevents ninety per cent of typos — and a typo in a path costs ten
minutes.

Use TAB. Every time.

## PATH, and "command not found"

When you type `python`, the terminal does not search your disk. It looks in **a short,
known list of folders**: the **PATH**.

| Message | What it means |
|---|---|
| `command not found` (macOS) | either the program is not installed, |
| `is not recognized as an internal or external command` (Windows) | or it is, but it is not on the PATH |

Knowing which of the two is already ninety per cent of the fix. On Windows the most
common cause is the **"Add python.exe to PATH"** checkbox missed at installation.

## Checking your installation

```
python --version
git --version
quarto --version
```

Each must return a version number.

## A few commands that become useful next

| Command | Effect |
|---|---|
| `cd ~` | go to your home folder |
| `mkdir my_folder` | create a folder |
| `cat file.csv` | print a text file |
| `head -5 file.csv` | print the first 5 lines — useful on a large CSV |
| `↑` (up arrow) | recall the previous command |
| `Ctrl+C` | interrupt a running program |
