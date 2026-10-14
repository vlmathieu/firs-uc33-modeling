# The cartography of models — guidance note

*Read this carefully. It is worth 40 % of the course unit, and it is built across the whole semester, not in January.*

---

## What you hand in

You have to deliver three objects, and they do different jobs.
Confusing them is the most common way to lose marks on an otherwise serious piece of work.

| Object | What it is for | Form |
|---|---|---|
| The **cartography** | Your reading of the whole set of models, laid out so that it can be taken in at once | One A3 page, PDF, orientation free |
| The **synthesis note** | An argument about what you found | PDF, 3 pages maximum |
| The **filled grid** | The working material behind the other two | One `.csv` file, annex, not page-counted |

A dozen models described along thirty-two columns do not fit legibly on an A3.
That is not a flaw in the exercise: deciding what to drop, what to group, and what to put at the centre *is* the exercise.
The grid is where you are exhaustive.
The A3 is where you take a position.
The note is where you defend it.
All three are written in English, like everything else in this course unit.

The layout of the A3 is yours.
Nothing obliges you to produce a table: a map, a set of axes, a tree, a matrix, a network, anything that can be read and argued with.

---

## Which models go in

Every model you meet anywhere in FIRS, in every course unit (not only in this one) and during the projects.
The opening session set the expectation at around a dozen; **ten is the floor**.
Models seen in UC 3.3 count, and so do those from survey sampling and inference, forest inventory and monitoring, remote sensing, data analytics, climate change and forests, wood markets, the expert-led sessions, your own engineering projects, etc.

The inclusion test is deliberately blunt.
If a course puts a model in front of you, it belongs in the cartography.
No family is required and none is excluded: a linear regression used to answer a question is a model, exactly as a partial equilibrium model of the forest sector is one.

Three things are easy to confuse, and the distinction is worth settling early.
A **model** is a representation of a system, with its assumptions.
Most of the time it is equations, or basic mathematics.
A **piece of software** is one implementation of a model, and the same model sometimes exists in several.
It is the R package you use, or the lines of code you produced.
A **scenario** is a set of inputs run through a model.
The grid holds one row per model, never one per scenario or per run.

---

## The grid

The five blocks were announced on 4 September, and `analysis-grid.csv` turns them into columns, filled with the dimensions from the typology part of the modelling lecture.

**Identity** — `research_question`, `purpose_class`, `model_family`, plus where and when you met the model and the reference you worked from.

**Frame** — `spatial_scale`, `spatial_resolution`, `time_step`, `time_horizon`, `aggregation`, and the `mechanism`, `behaviour` and `stochasticity` the model assumes.

**Flows** — `inputs_data`, `drivers`, `outputs`.

**Credibility** — `parameter_origin`, `data_intensity`, `calibration`, `validation`, `uncertainty`.

**Use** — `access_licence`, `code_language`, `reproducibility`, `strengths`, `limits`, `domain_of_validity`.

To which the grid adds two columns that carry most of the analytical weight: `typology_position`, where you place the model inside a published typology, and `what_does_not_fit`, where you say what that placement fails to capture.

The file ships with the worked example from slide 12 of the opening session already filled in, as a calibration of the expected level of detail.
Short entries.
The grid is not where you write prose.

That row is there to set the level of detail, not to be counted: delete it before you submit.
Neither it nor the worked example itself counts towards your ten models.

The file is comma-separated and encoded in UTF-8, and it has to come back that way.
A spreadsheet configured in French will offer to save it as Latin-1 with semicolons, which turns the whole grid into a single column.

### Six columns use a closed vocabulary

The grid is only comparable if the same word means the same thing on every row.
Six columns therefore take their values from a fixed list.
Everything else is free text.

| Column | Allowed values |
|---|---|
| `purpose_class` | `prediction`, `explanation`, `description`, `theoretical-exposition`, `illustration`, `analogy`, `social-learning` |
| `model_family` | `statistical`, `machine-learning`, `process-based`, `partial-equilibrium`, `optimisation`, `agent-based`, `system-dynamics`, `gap-or-landscape`, `sampling-inference`, `other` |
| `mechanism` | `empirical`, `mechanistic`, `hybrid` |
| `behaviour` | `none`, `optimising`, `adaptive`, `rule-based` |
| `stochasticity` | `deterministic`, `stochastic` |
| `data_intensity` | `low`, `medium`, `high` |

The `purpose_class` list comes from Edmonds et al. 2019, the `behaviour`, `stochasticity` and `data_intensity` ranges from the dimension table of Kelly et al. (2013) shown in the lecture, and `model_family` from the families named in the opening session.
`spatial_resolution` is free text, but the lecture's own range, *e.g.*, none, regions, grid, individual location, covers most cases.

When a model takes two values in one column, say so and say why in the free-text columns.
A hybrid is a finding, not a filling error.

### The grid is a starting point, not a template

You will settle the structure of your own cartography in October, together, and you are expected to change this one: add columns your set of models needs, drop the ones that stay empty, rename what reads badly.
The one thing not to do is keep a column you cannot fill for most of your models, because an empty column looks like negligence rather than like a deliberate choice.

---

## Axes and classes

There are two ways to sort models, and you need both.

**Axes** describe.
Each model takes a value along a dimension: a time step, a spatial resolution, a degree of stochasticity.
Axes are comparable across anything, which is why the grid is built on them.
Their weakness is that they flatten: a process-based stand model and a sector equilibrium model can end up looking similar once reduced to eight dimensions.

**Classes** interpret.
A published typology gives you named categories and places a model in one of them.
Classes carry meaning that axes lose, and they connect your work to a literature.
Their weakness is the opposite one: no published typology was written with your dozen models in mind, so some of them will not fit.

That misfit is the single most productive thing in this deliverable. 
There is no official taxonomy of models, only recurrent combinations of dimensions.
A entry that reports "this model sits between two of Kelly's approaches, and here is which assumption makes it so" is worth more than one that forces every model into a box and says nothing about the forcing.
That is what `what_does_not_fit` is for, and `typology-references.md` lists the typologies worth drawing on.

---

## How to actually do this

Document each model the day you meet it.
An entry written the same evening takes twenty minutes, because the talk is still fresh and you still remember what the speaker hedged about.
The same entry reconstructed in January takes a day, and you will have lost precisely the hedge that made it interesting.

Keep a running list from the start, with dates and where you saw each model.
The list costs nothing and it is what tells you, in November, that you are at four models and not nine.

For each model, three sources in this order.
The **primary reference**: the article describing the model (if existing), not an application of it.
The **technical documentation**, which is where time steps and parameter origins are actually written down.
The **code repository**, if there is one, which is the only honest answer to the `reproducibility` column.
When a speaker presents a model, the question worth asking in the room is which of the three exists and where.

Cite every source: articles, data, code, slides.
Use APA format throughout, and distinguish the primary reference of a model from an application of it.
Be transparent about your use of AI tools.

---

## How this goes wrong

**Paraphrasing each model's own documentation.** 
This is *the* failure mode, and it is the criterion carrying the most weight.
A cartography that restates what each model says about itself is a catalogue.
Models are to be compared with each other, on their assumptions, their strengths, their limits and their domains of use.

**Confusing calibration and validation.**
Fitting parameters on data is calibration.
Confronting the fitted model with data it has not seen is validation.
A model "validated" on its calibration sample has not been validated, and saying so is a finding worth a line in your note.

**Reading "dynamic" as "has a time axis".**
A model producing a yearly series is not dynamic if nothing in it feeds back.
Look for state variables updated from their own previous value.

**Confusing purpose with method.**
Agent-based is a method.
Explanation is a purpose.
The same method serves several purposes, and the same purpose is served by several methods, which is why the grid asks for both in separate columns.

**Handing in a table on an A3.**
A printed spreadsheet is the grid, not a cartography.
If your A3 says nothing that the CSV does not already say, it has no reason to exist.

---

## Deadlines and submission

Due **15 January, 23:59, Paris time**.
Submission by email to <valentin.mathieu@agroparistech.fr> and <antonello.lobianco@agroparistech.fr>, with three attachments named as follows, using your two surnames in lower case:

```
cartography-<name1>-<name2>.pdf
synthesis-<name1>-<name2>.pdf
grid-<name1>-<name2>.csv
```

Flag a delay in advance.
Otherwise the penalty announced in the opening session applies, typically 10 % per day, and beyond a limit the work may be refused.
You work in pairs formed by the teaching team, tasks are split as you see fit, and each of you answers for the whole thing.

The working calendar is the one given on 4 September: list the models and start sorting them before October, settle your structure and document a first model together before holidays, then add an entry each time you meet a model, until January.

---

## Where to look next

The assessment criteria and their weights are in [`assessment-criteria.md`](assessment-criteria.md).
The typologies and protocols worth drawing on, annotated, are in [`typology-references.md`](typology-references.md).
The grid itself is [`analysis-grid.csv`](analysis-grid.csv), and the level of detail expected per cell is set by the worked example on slide 12 of [`03-lectures/2026-09-04-opening/`](../03-lectures/2026-09-04-opening/), pending the fuller `worked-example.md`.

For what the columns mean, the lecture of 4 September is the reference: [`03-lectures/2026-09-04-modeling/`](../03-lectures/2026-09-04-modeling/), part B for typologies, and the rest for calibration, validation, uncertainty and reproducibility.

Your teachers are still available to help you and answer your questions.

Work well!
