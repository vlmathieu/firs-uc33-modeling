# Lab 1 — Challenges

Take these if you have finished the core. Do not do them instead of it.

## 1. The Python version

Redo step 4 in Python, in `src/01_import.py`, using `pathlib`:

```python
from pathlib import Path
ROOT = Path(__file__).parent.parent
```

Compare with the R solution. What is more explicit in each of the two?

## 2. Break the project on purpose

Move `uc33-lab1` somewhere else on your disk, then run the script again. If you did the
work properly, nothing changes. If something breaks, you still had an absolute path
somewhere.

Do it again, this time by renaming the folder.

## 3. Parameters out of the code

Create `config/config.yml`:

```yaml
input_file: data/raw/comtrade_fr_roundwood_clean.csv
min_year: 2023
```

Read it from R (`yaml::read_yaml()`) or Python (`yaml.safe_load()`) and remove every
hard-coded value from your script.

This is a foretaste of 23 October.

## 4. Naming, put to the test

Create a file in `data/raw/` called `Données récoltées (final).csv`, try to read it from
your script, and explain to your partner **three distinct reasons** why that name is a
problem.

Then delete it.

## 5. Read the course repository as a project

Open [the course repository](https://github.com/vlmathieu/firs-uc33-modeling) and check
that it follows the rules it imposes on you: no accents or spaces in names, dates as
`YYYY-MM-DD`, explicit ordering, a README at the root.

**If it fails anywhere, open an issue.** This is serious: the first one found earns the
right to say so in class.
