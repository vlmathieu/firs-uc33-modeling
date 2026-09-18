# Handbook

The course handbook: structured, concise, with examples. It is meant to be used all
year, not only on the day it is handed out; that is what distinguishes it from a set of
lab notes.

## Part 1 — Python and VS Code

Written from the questions raised in the repository's issues during the first
fortnight. Nine short chapters, each readable alone, each ending with complementary
readings.

| Chapter | Read it when |
|---|---|
| [00 Why Python](python/00-why-python.md) | you wonder why a third language |
| [01 Key concepts](python/01-key-concepts.md) | interpreter, package, kernel, PATH… mean nothing to you yet |
| [02 Installing Python](python/02-install.md) | before installing, or when two Pythons are fighting |
| [03 Interpreters in VS Code](python/03-interpreters-and-vscode.md) | "it works in the terminal but not in VS Code" |
| [04 Installing packages](python/04-install-packages.md) | `ModuleNotFoundError` after a successful install |
| [05 Running code](python/05-run-code.md) | ▷, `Shift+Enter`, `# %%`, notebooks: which, when |
| [06 Writing a script](python/06-script-conventions.md) | before writing your first script |
| [07 Reading errors](python/07-read-errors.md) | a traceback is on screen |
| [08 Checklist](python/08-checklist.md) | print it; run its five commands before opening an issue |

## Reading it

On GitHub, click a chapter. The files are plain Markdown.

As one document, the folder is a [Quarto book](https://quarto.org/docs/books/): from
this folder, `quarto render` produces `_book/` with an HTML site and a PDF. The
rendered output is not committed; the Markdown files are the source of truth.

## Other parts

Glossary, R and Python commands side by side, project layout, path traps and the
terminal are in [`02-reference/`](../02-reference/) for now. They will join this
handbook as further parts.
