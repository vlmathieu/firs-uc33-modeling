# Lab 1 — Challenges

Take these if you have finished the core. Do not do them instead of it.

## 1. The Python version

Redo step 4 in Python, in `src/01_import.py`, using `pathlib`:

```python
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]     # the project root
```

Two things will stop you before you get there. Both are worth more than the exercise
itself.

### `ModuleNotFoundError: No module named 'pandas'`

```
>>> import pandas as pd
ModuleNotFoundError: No module named 'pandas'
```

pandas is not part of Python. It is a package, and nothing has installed it yet — the
prerequisites installed the *language*, not the libraries. Step 5 of the brief has the
command; here it is again, **in the terminal**, not at the `>>>` prompt:

```
python -m pip install pandas
```

```
py -m pip install pandas
```

The second form is the Windows fallback, for when `python` is not recognised.

Then **start a new Python session**: a package installed while a session is open is not
visible to that session.

If it still says the module is missing after an install that said it succeeded, you have
two Pythons and you installed into the wrong one. Ask them who they are:

```python
import sys
sys.executable      # the interpreter this session is running
```

```
python -c "import sys; print(sys.executable)"
```

Run both. If the two paths differ, that is your answer. Fix it in VS Code with
`Ctrl+Shift+P` → **Python: Select Interpreter**, pick the one you installed into, then
close the terminal and open a new one.

### `NameError: name '__file__' is not defined`

```
>>> ROOT = Path(__file__).resolve().parents[1]
NameError: name '__file__' is not defined. Did you mean: '__name__'?
```

This one is not a mistake, it is a fact about where you typed the line.

`__file__` is the path of **the file Python is currently executing**. Send a line to
the console with `Shift+Enter` and Python is not executing a file — it is executing
you, one line at a time. There is no file, so there is no `__file__`, and there is
nothing to take the parent of.

So: the same line belongs in two different forms depending on where it runs.

| Where | What locates the project root |
|---|---|
| In a **script**, run as a script | `ROOT = Path(__file__).resolve().parents[1]` |
| In the **console** | `ROOT = Path.cwd()` — provided you opened the *folder* `uc33-lab1` in VS Code, which is what makes the terminal start at the project root |

Check it before you trust it:

```python
from pathlib import Path
ROOT = Path.cwd()
ROOT                                    # must end in uc33-lab1
(ROOT / "data" / "raw").exists()        # must be True
```

Then run the finished script properly, from the project root:

```
python src/01_import.py
```

That is when `__file__` exists, and that is the version that has to work — your partner
will run the script, not your console.

### Then compare

Compare with the R solution. What is more explicit in each of the two?

One thing to notice while you do. In R, `here()` gives the same answer in the console
and in the script, because the `.Rproj` fixed the working directory for both. In
Python nothing fixed anything for you: the script finds itself from `__file__`, the
console has to be told. That is the same lesson as step 3, seen from the side where
it is not done for you.

## 2. Break the project on purpose

Move `uc33-lab1` somewhere else on your disk, then run the script again. If you did the
work properly, nothing changes. If something breaks, you still had an absolute path
somewhere.

Do it again, this time by renaming the folder.

## 3. Parameters out of the code

The template already ships `config/config.yml`. Open it: it holds the two paths, the
country, and a switch. Nothing in it is code.

```yaml
input_file: data/raw/comtrade_fr_roundwood_clean.csv
output_file: data/processed/trade_france.csv

country: France
exclude_partner_aggregate: true
```

**Read it in the console first**, before touching your script, so that you can see what
you get back.

```r
# R
install.packages("yaml")   # once on the machine, from inside R
library(yaml)
library(here)

params <- read_yaml(here("config", "config.yml"))

str(params)              # a named list
params$input_file        # "data/raw/comtrade_fr_roundwood_clean.csv"
params$country           # "France"
```

For Python the package is called `pyyaml`, and it installs from the terminal:

```
python -m pip install pyyaml
```

```python
# Python
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]   # in a script
# ROOT = Path.cwd()                          # in the console, at the project root

params = yaml.safe_load(open(ROOT / "config" / "config.yml"))

params                       # a dict
params["input_file"]         # 'data/raw/comtrade_fr_roundwood_clean.csv'
params["country"]            # 'France'
```

A YAML file becomes a **named list** in R and a **dict** in Python. You reach into it
the same way you would reach into anything else, and there is no third concept to learn.

Now use it. In your script, every hard-coded value is replaced by a lookup:

```r
# R
trade  <- read.csv(here(params$input_file))
france <- subset(trade, reporterDesc == params$country)
```

```python
# Python
trade  = pd.read_csv(ROOT / params["input_file"])
france = trade[trade.reporterDesc == params["country"]]
```

Then the test: change `country` to `Belgium` in the YAML file, run the script again,
and check that **you did not open a single `.R` or `.py` file to do it.** You should get
18 rows instead of 379. That is the
whole point — the person who changes the parameters is not necessarily the person who
can read the code.

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
