# R / Python / Julia equivalents

*One page. The most consulted sheet of the year: keep it open.*

The principle of this course unit is in this table: **the syntax changes, the concepts
do not.** You are not learning three languages, you are learning one set of ideas and
three ways of writing them.

---

## Basics

| Concept | R | Python | Julia |
|---|---|---|---|
| Comment | `# ...` | `# ...` | `# ...` |
| Assignment | `x <- 1` | `x = 1` | `x = 1` |
| Print | `print(x)` · `cat(x)` | `print(x)` | `println(x)` |
| True / false | `TRUE` `FALSE` | `True` `False` | `true` `false` |
| Missing value | `NA` | `None` · `np.nan` | `missing` · `nothing` |
| Test for missing | `is.na(x)` | `pd.isna(x)` | `ismissing(x)` |
| Help | `?fn` | `help(fn)` | `?fn` |

## Sequences of values

| Concept | R | Python | Julia |
|---|---|---|---|
| Create | `c(1, 2, 3)` | `[1, 2, 3]` | `[1, 2, 3]` |
| **First element** | `x[1]` | `x[0]` | `x[1]` |
| Last element | `x[length(x)]` | `x[-1]` | `x[end]` |
| Slice (2nd to 4th) | `x[2:4]` | `x[1:4]` | `x[2:4]` |
| Length | `length(x)` | `len(x)` | `length(x)` |
| Sequence 1 to 5 | `1:5` | `range(1, 6)` | `1:5` |
| Distinct values | `unique(x)` | `set(x)` · `.unique()` | `unique(x)` |

> **Trap number one when moving between languages.** R and Julia count from **1**.
> Python counts from **0**. That is not a quirk: it is a source of silent bugs that do
> not crash and shift every one of your results by one position.

## Key-value mappings

| Concept | R | Python | Julia |
|---|---|---|---|
| Create | `list(a = 1, b = 2)` | `{"a": 1, "b": 2}` | `Dict("a" => 1, "b" => 2)` |
| Access | `d$a` · `d[["a"]]` | `d["a"]` | `d["a"]` |

## Data tables

| Concept | R | Python (pandas) | Julia (DataFrames) |
|---|---|---|---|
| Create | `data.frame(x = 1:3)` | `pd.DataFrame({"x": [1,2,3]})` | `DataFrame(x = 1:3)` |
| Read a CSV | `read.csv("f.csv")` | `pd.read_csv("f.csv")` | `CSV.read("f.csv", DataFrame)` |
| Write a CSV | `write.csv(d, "f.csv")` | `d.to_csv("f.csv")` | `CSV.write("f.csv", d)` |
| First rows | `head(d)` | `d.head()` | `first(d, 6)` |
| Dimensions | `dim(d)` | `d.shape` | `size(d)` |
| One column | `d$qty` | `d["qty"]` | `d.qty` |
| Filter rows | `subset(d, qty > 0)` | `d[d.qty > 0]` | `filter(:qty => >(0), d)` |
| New column | `d$uv <- d$val / d$qty` | `d["uv"] = d.val / d.qty` | `d.uv = d.val ./ d.qty` |

## Functions and control flow

| Concept | R | Python | Julia |
|---|---|---|---|
| Define | `f <- function(x) { x * 2 }` | `def f(x): return x * 2` | `f(x) = 2x` |
| Condition | `if (x > 0) { ... } else { ... }` | `if x > 0: ... else: ...` | `if x > 0 ... else ... end` |
| Loop | `for (i in 1:5) { ... }` | `for i in range(5): ...` | `for i in 1:5 ... end` |

## Operating on a whole column at once

This is the real difference between the three, and it is worth understanding.

| Concept | R | Python | Julia |
|---|---|---|---|
| Multiply everything by 2 | `x * 2` | `np.array(x) * 2` | `x .* 2` |
| Apply a function | `f(x)` if `f` is vectorised | `[f(i) for i in x]` | `f.(x)` |

- **R** is vectorised by default: `x * 2` works on the whole vector. A statistician's
  inheritance.
- **Python** is not, on lists: you need `numpy` or `pandas` to get that behaviour back.
- **Julia** states it explicitly with a **dot**: `.` means "apply element by element".
  `f.(x)` applies `f` to each element. One character more verbose, and perfectly clear.

## Packages

| Concept | R | Python | Julia |
|---|---|---|---|
| Install (once) | `install.packages("sf")` | `pip install geopandas` | `] add GeoDataFrames` |
| Load (every session) | `library(sf)` | `import geopandas` | `using GeoDataFrames` |

**Installing is not loading.** `there is no package called 'sf'` means: not installed.
`could not find function "st_read"` means: installed, but not loaded.

## Files and paths

| Concept | R | Python | Julia |
|---|---|---|---|
| Current directory | `getwd()` | `os.getcwd()` | `pwd()` |
| Build a path | `file.path("data", "raw")` | `Path("data") / "raw"` | `joinpath("data", "raw")` |
| Project root | `here::here()` | `Path(__file__).parent.parent` | `@__DIR__` |

**Never write `setwd()`.** Open an RStudio Project (`.Rproj`), or build your paths from
the project root.

---

## Three traps worth knowing in advance

**Concatenating text.** `paste0("a", "b")` in R, `"a" + "b"` in Python, and
`"a" * "b"` in Julia — yes, the asterisk. Julia reserves `+` for numbers.

**Block delimiters.** R and Julia mark blocks explicitly (`{}` in R, `end` in Julia).
Python marks them by **indentation**: shifting a line by four spaces changes the logic
of the program. That is not style, it is syntax.

**Quotes.** `"text"` works everywhere. In R and Python, `'text'` does too. In Julia,
`'a'` denotes **a single character**, not a string — a one-character string is `"a"`.
