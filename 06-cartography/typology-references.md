# Model typologies and description protocols — annotated references

*Not a reading list to exhaust. Five references to read, a dozen typologies to draw on, and the rest to open once, on the column of the grid where you are stuck.*

The point of this deliverable is the typology ***you*** build.
These references exist to keep you from reinventing categories that already have names, and to give you the vocabulary to say where your own grid departs from theirs.

PDF files of the following references are available on [`seafile`](https://seafile.agroparistech.fr/smart-link/07e3fa83-8ebd-4eaf-af67-16e415eaf4a4/).

---

## Read these five

**Kelly (Letcher), R. A., Jakeman, A. J., Barreteau, O., et al. (2013).** Selecting among five common modelling approaches for integrated environmental assessment and management. *Environmental Modelling & Software*, 47, 159–181. [10.1016/j.envsoft.2013.05.005](https://doi.org/10.1016/j.envsoft.2013.05.005)

The closest thing to a ready-made grid.
Written for integrated assessment, so its five approaches will not swallow every model you meet, which is itself the kind of finding to report.

**Edmonds, B., Le Page, C., Bithell, M., et al. (2019).** Different Modelling Purposes. *JASSS*, 22(3). [10.18564/jasss.3993](https://doi.org/10.18564/jasss.3993)

Seven purposes, and the argument that a model good for one is usually bad for another.
The closed vocabulary of `purpose_class` comes from here.

**Levins, R. (1966).** The strategy of model building in population biology. *American Scientist*, 54(4), 421–431. No DOI.

Generality, realism and precision: you may have two of the three. The shortest route to an argument for your synthesis note, because it explains why your models disagree without any of them being wrong.

For the biophysical side: **Bugmann, H., & Seidl, R. (2022).** The evolution, complexity and diversity of models of long-term forest dynamics. *Journal of Ecology*, 110(10), 2288–2307. [10.1111/1365-2745.13989](https://doi.org/10.1111/1365-2745.13989)

For the economic side: **Latta, G. S., Sjølie, H. K., & Solberg, B. (2013).** A review of recent developments and applications of partial equilibrium models of the forest sector. *Journal of Forest Economics*, 19(4), 350–360. [10.1016/j.jfe.2013.06.006](https://doi.org/10.1016/j.jfe.2013.06.006)

---

## The typologies, and what each one sorts

### Models

Four of these sort models with no reference to any domain:

+ **Edmonds, B., Le Page, C., Bithell, M., et al. (2019).** Different Modelling Purposes. *JASSS*, 22(3). [10.18564/jasss.3993](https://doi.org/10.18564/jasss.3993) — sorts them by purpose, into seven classes
+ **Epstein, J. M. (2008).** Why Model? *JASSS*, 11(4), article 12. No DOI; <https://www.jasss.org/11/4/12.html> — does the same work with sixteen reasons to build a model, only one of which is prediction.
+ **Levins, R. (1966).** The strategy of model building in population biology. *American Scientist*, 54(4), 421–431. No DOI — sorts not the models but the strategies behind them, by which of generality, realism and precision they give up.
+ **Breiman, L. (2001).** Statistical Modeling: The Two Cultures. *Statistical Science*, 16(3), 199–231. [10.1214/ss/1009213726](https://doi.org/10.1214/ss/1009213726) — splits the statistical half of a cartography in two, data modelling against algorithmic modelling, which is what keeps a regression and a random forest from landing in the same row.

The one that sorts by approach rather than by intent is:

+ **Kelly (Letcher), R. A., Jakeman, A. J., Barreteau, O., et al. (2013).** Selecting among five common modelling approaches for integrated environmental assessment and management. *Environmental Modelling & Software*, 47, 159–181. [10.1016/j.envsoft.2013.05.005](https://doi.org/10.1016/j.envsoft.2013.05.005) — whose
eleven dimensions are the ones the grid is built on.

Four more sort models within a domain, and they are where to look when `model_family`
feels too coarse:

+ **Bugmann, H., & Seidl, R. (2022).** The evolution, complexity and diversity of models of long-term forest dynamics. *Journal of Ecology*, 110(10), 2288–2307. [10.1111/1365-2745.13989](https://doi.org/10.1111/1365-2745.13989) — covers fifty years of forest dynamics models, sorted by what they represent and at what cost in complexity.
+ Inside that set, **Bugmann, H. (2001).** A Review of Forest Gap Models. *Climatic Change*, 51(3-4), 259–305. [10.1023/A:1012525626267](https://doi.org/10.1023/A:1012525626267) — follows the gap model lineage from JABOWA on, with what each generation added, which lets you place a model inside a family rather than merely name the family.
+ **Pretzsch, H., Grote, R., Reineking, B., Rötzer, T., & Seifert, S. (2008).** Models for Forest Ecosystem Management: A European Perspective. *Annals of Botany*, 101(8), 1065–1087. [10.1093/aob/mcm246](https://doi.org/10.1093/aob/mcm246) — sorts the same material by level of organisation and degree of mechanism, from organ to landscape.
+ On the economic side, **Latta, G. S., Sjølie, H. K., & Solberg, B. (2013).** A review of recent developments and applications of partial equilibrium models of the forest sector. *Journal of Forest Economics*, 19(4), 350–360. [10.1016/j.jfe.2013.06.006](https://doi.org/10.1016/j.jfe.2013.06.006) — separates spatial equilibrium, recursive dynamic and intertemporal optimisation models, and says who uses which.

### Not models, but things your grid has columns for

Three typologies sort something other than models, and each one answers a column of your grid:

+ **Börjeson, L., Höjer, M., Dreborg, K.-H., Ekvall, T., & Finnveden, G. (2006).** Scenario types and techniques: towards a user's guide. *Futures*, 38(7), 723–739. [10.1016/j.futures.2005.12.002](https://doi.org/10.1016/j.futures.2005.12.002) — sorts scenarios into predictive, explorative and normative, and explains why the three are not interchangeable, which is also the quickest way to see that a scenario is an input set and not a model.
+ **Refsgaard, J. C., van der Sluijs, J. P., Højberg, A. L., & Vanrolleghem, P. A. (2007).** Uncertainty in the environmental modelling process: a framework and guidance. *Environmental Modelling & Software*, 22(11), 1543–1556. [10.1016/j.envsoft.2007.02.004](https://doi.org/10.1016/j.envsoft.2007.02.004) — sorts uncertainty by source, by nature and by where it enters the modelling chain, which is what lets you distinguish a model with no uncertainty analysis from one whose uncertainty is irreducible.
+ **Peng, R. D. (2011).** Reproducible Research in Computational Science. *Science*, 334(6060), 1226–1227. [10.1126/science.1213847](https://doi.org/10.1126/science.1213847) — turns reproducibility into a spectrum, from publication alone to full code and data, rather than a yes or no.

These are existing typologies of models.
None of them was written to classify the models you study in FIRS, and that is what the `what_does_not_fit` column in your grid is for.

---

## By column of the grid, when you are stuck

One or two references per column.

**`research_question`, and what a model is for**:

+ **Box, G. E. P. (1976).** Science and Statistics. *JASA*, 71(356), 791–799. [10.1080/01621459.1976.10480949](https://doi.org/10.1080/01621459.1976.10480949) — where "all models are wrong, some are useful" comes from, in its original and more demanding form. Four pages.

**The order in which to describe a model**:

+ **Grimm, V., Railsback, S. F., Vincenot, C. E., et al. (2020).** The ODD Protocol, A Second Update. *JASSS*, 23(2). [10.18564/jasss.4259](https://doi.org/10.18564/jasss.4259) — the protocol the grid is a flattened version of. A protocol does not sort models; it fixes the order in which one model is described. The 2006 original is
[10.1016/j.ecolmodel.2006.04.023](https://doi.org/10.1016/j.ecolmodel.2006.04.023) if
you want to see what the design concepts section looked like first.

**`calibration`, `parameter_origin`**:

+ **Jakeman, A. J., Letcher, R. A., & Norton, J. P. (2006).** Ten iterative steps in development and evaluation of environmental models. *Environmental Modelling & Software*, 21(5), 602–614. [10.1016/j.envsoft.2006.01.004](https://doi.org/10.1016/j.envsoft.2006.01.004) — useful in reverse: read a model's documentation against the ten steps and see which ones its authors skipped or did not report.

**`validation`**:

+ **Rykiel, E. J. (1996).** Testing ecological models: the meaning of validation. *Ecological Modelling*, 90(3), 229–244. [10.1016/0304-3800(95)00152-2](https://doi.org/10.1016/0304-3800(95)00152-2) — what the word can and cannot mean, and why it covers at least four different operations.
+ **Oreskes, N., Shrader-Frechette, K., & Belitz, K. (1994).** Verification, Validation, and Confirmation of Numerical Models in the Earth Sciences. *Science*, 263(5147), 641–646. [10.1126/science.263.5147.641](https://doi.org/10.1126/science.263.5147.641) — the harder argument: open-system models cannot be verified at all, only confirmed against partial evidence.

**`validation`, for rows where `behaviour` is not `none`**:

+ **Fagiolo, G., Moneta, A., & Windrum, P. (2007).** A Critical Guide to Empirical Validation of Agent-Based Models in Economics. *Computational Economics*, 30(3), 195–226. [10.1007/s10614-007-9104-4](https://doi.org/10.1007/s10614-007-9104-4) — validation where the outputs are emergent patterns rather than fitted series.

**The evidence that a model works, as a whole**:

+ **Grimm, V., Augusiak, J., Focks, A., et al. (2014).** Documenting model development, testing, and analysis using TRACE. *Ecological Modelling*, 280, 129–139. [10.1016/j.ecolmodel.2014.01.018](https://doi.org/10.1016/j.ecolmodel.2014.01.018) — ODD describes what a model is; TRACE documents why you should believe it. Its headings map almost one to one onto the Credibility block.
+ **Schmolke, A., Thorbek, P., DeAngelis, D. L., & Grimm, V. (2010).** Ecological models supporting environmental decision making: a strategy for the future. *TREE*, 25(8), 479–486. [10.1016/j.tree.2010.05.001](https://doi.org/10.1016/j.tree.2010.05.001) — four pages on why models used in decisions are so rarely documented well enough to be trusted.

**`uncertainty`**:

+ **Saltelli, A., Aleksankina, K., Becker, W., et al. (2019).** Why so many published sensitivity analyses are false. *Environmental Modelling & Software*, 114, 29–39. [10.1016/j.envsoft.2019.01.012](https://doi.org/10.1016/j.envsoft.2019.01.012) — most reported analyses vary one parameter at a time, which tells you almost nothing. Lets you write something sharper than "a sensitivity analysis was performed".
+ The two methods you will see named: **Morris 1991**, *Technometrics*, 33(2), 161–174. [10.1080/00401706.1991.10484804](https://doi.org/10.1080/00401706.1991.10484804) and **Sobol' 2001**, *Mathematics and Computers in Simulation*, 55(1-3), 271–280. [10.1016/S0378-4754(00)00270-6](https://doi.org/10.1016/S0378-4754(00)00270-6) — recognising which one was used is all the grid asks.

**`mechanism`, when the answer is `hybrid`**:

+ **Reichstein, M., Camps-Valls, G., Stevens, B., et al. (2019).** Deep learning and process understanding for data-driven Earth system science. *Nature*, 566(7743), 195–204. [10.1038/s41586-019-0912-1](https://doi.org/10.1038/s41586-019-0912-1) — where models that are part process, part learned actually sit.

**`limits`, `domain_of_validity`**:

+ **Lucas, R. E. (1976).** Econometric policy evaluation: A critique. *Carnegie-Rochester Conference Series on Public Policy*, 1, 19–46. [10.1016/S0167-2231(76)80003-6](https://doi.org/10.1016/S0167-2231(76)80003-6) — why a model fitted on past behaviour can break precisely when used to evaluate a policy that changes that behaviour.
+ **Rudin, C. (2019).** Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. *Nature Machine Intelligence*, 1(5), 206–215. [10.1038/s42256-019-0048-x](https://doi.org/10.1038/s42256-019-0048-x) — post-hoc explanation of an opaque model is not the same thing as an interpretable model.

**`access_licence`, `code_language`, `reproducibility`**:

+ **Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013).** Ten Simple Rules for Reproducible Computational Research. *PLOS Computational Biology*, 9(10), e1003285. [10.1371/journal.pcbi.1003285](https://doi.org/10.1371/journal.pcbi.1003285)
+ **Wilson, G., Bryan, J., Cranston, K., et al. (2017).** Good enough
practices in scientific computing. *PLOS Computational Biology*, 13(6), e1005510.
[10.1371/journal.pcbi.1005510](https://doi.org/10.1371/journal.pcbi.1005510)

**When a model is really several models**:

+ **Voinov, A., & Shugart, H. H. (2013).** 'Integronsters', integral and integrated modeling. *Environmental Modelling & Software*, 39, 149–158. [10.1016/j.envsoft.2012.05.014](https://doi.org/10.1016/j.envsoft.2012.05.014) — what happens when models are coupled without their assumptions being reconciled. Read it before calling any chain of models "integrated".

**When a modelling paradigm is itself the claim**:

+ **Arthur, W. B. (1999).** Complexity and the Economy. *Science*, 284(5411), 107–109. [10.1126/science.284.5411.107](https://doi.org/10.1126/science.284.5411.107)
+ **Deming, D. (2023).** M. King Hubbert and the rise and fall of peak oil theory. *AAPG Bulletin*, 107(6), 851–861. [10.1306/03202322131](https://doi.org/10.1306/03202322131) — the second is a post-mortem of a model that failed in public, and a useful counterweight to a cartography that only records what models claim to do.

---
