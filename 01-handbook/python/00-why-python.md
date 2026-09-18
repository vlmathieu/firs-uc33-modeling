# Why Python

*Ten minutes. Read once, before the install.*

You already have R and you will meet Julia later in the year. This chapter says why a
third language is worth the trouble, and where it is not.

## What Python is

A general-purpose programming language, created in 1991, free, open source, run by a
non-profit foundation. It was not designed for statistics. It was designed to be
readable and to glue other programs together. Data work came later, through packages
written by scientists: NumPy (2006), pandas (2008), scikit-learn (2010), GeoPandas
(2013).

That history explains most of what follows. R was built for data by statisticians;
Python was adapted to data by engineers, and both origins show.

## Strengths

The same language covers the whole pipeline. The script that downloads the data, the
one that cleans it, the model, the web service that serves the result and the job that
reruns everything every night can all be Python. R does the middle of that chain very
well and the two ends less well.

It is readable. Indentation is the syntax, so code written by a stranger is usually
understandable on first read. In a career you read far more code than you write, so
this matters more than it sounds.

Whatever the task, someone has published a package for it. The ones this course unit
relies on:

| Task | Package |
|---|---|
| tables, the equivalent of a data frame | pandas |
| numerical arrays | NumPy |
| plots | matplotlib, plotly, altair |
| statistics and models | statsmodels, scikit-learn |
| spatial data | GeoPandas, rasterio, shapely |
| reading almost any file format | built in, or one `import` away |

Employers ask for it. In the forest and environmental sector as elsewhere, job
advertisements name Python more often than R; the ones that name R usually say
"statistician" somewhere. Knowing both is the comfortable position.

It runs on laptops, servers and clusters, and inside QGIS, ArcGIS and Excel.

## Weaknesses

Installing it is the hard part, and this handbook exists because of that. Several
Pythons can live on one machine, each with its own packages, and nothing warns you
when you install into one and run another. R has one installation and one library per
version. Chapters 2 to 4 are about managing something R never asks you to manage.

Statistics are not native. In R a linear model is `lm(y ~ x, data)`, one line, with a
summary table designed by a statistician. In Python it is `statsmodels`, which imitates
R's formula syntax and does it well, but as an add-on. For mixed models, survival
analysis or specialised tests, R has the reference implementation and Python has a
port, sometimes.

Plain loops are slow. A `for` loop over a million rows takes seconds in Python where
it takes milliseconds in Julia. The answer is the same as in R: operate on whole
columns and let pandas and NumPy do the loop in compiled code. Chapter 6 shows the
pattern.

There is no single obvious editor. R has RStudio and everyone uses it. Python has
VS Code, PyCharm, Spyder, JupyterLab and others. This course unit uses VS Code because
it is free, runs R and Quarto too, and is what most workplaces use. Chapter 3 covers
it.

Versions drift. Python releases a new version every October and packages take a few
months to catch up, so installing the very newest Python in the autumn is a reliable
way to hit compile errors. Chapter 2 says which version to pick.

## When to reach for which

| Situation | Reach for |
|---|---|
| exploratory statistics, a model with a formula, a publication figure | R |
| cleaning a large file, joining twenty of them, automating the job | Python |
| spatial data, satellite imagery, anything that talks to GIS | Python |
| a numerical model that must run fast and that you write yourself | Julia |
| a report mixing text, code and figures | Quarto, with any of the three inside |

A working analyst opens both R and Python in the same week and does not think of it as
switching languages. A data frame is a data frame, a join is a join, a missing value is
a missing value. The sheet
[R / Python / Julia equivalents](https://github.com/vlmathieu/firs-uc33-modeling/blob/main/02-reference/r-python-julia-equivalents.md)
is built on that idea.

## Complementary readings

- *Think Python*, Allen Downey — <https://allendowney.github.io/ThinkPython/>. Free,
  from zero, the reference for the language itself rather than for data work.
- *Python for Data Analysis*, Wes McKinney — <https://wesmckinney.com/book/>. Free
  online. Written by the author of pandas. Chapters 5 to 8 are the ones you will use.
- The official tutorial — <https://docs.python.org/3/tutorial/>. Dense, exact, and
  the place to check when a blog post and the documentation disagree.
- Stack Overflow developer survey — <https://survey.stackoverflow.co/>. The yearly
  picture of what is actually used. Look for Python and R in the "technology" section.
