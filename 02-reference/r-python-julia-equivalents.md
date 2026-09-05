# Équivalences R / Python / Julia

*Une page. C'est la fiche la plus consultée de l'année : gardez-la ouverte.*

Le principe de l'UC tient dans ce tableau : **la syntaxe change, les concepts ne
changent pas.** Vous n'apprenez pas trois langages, vous apprenez un ensemble de
notions et trois façons de les écrire.

---

## Les bases

| Concept | R | Python | Julia |
|---|---|---|---|
| Commentaire | `# ...` | `# ...` | `# ...` |
| Affectation | `x <- 1` | `x = 1` | `x = 1` |
| Afficher | `print(x)` · `cat(x)` | `print(x)` | `println(x)` |
| Vrai / faux | `TRUE` `FALSE` | `True` `False` | `true` `false` |
| Valeur absente | `NA` | `None` · `np.nan` | `missing` · `nothing` |
| Tester l'absence | `is.na(x)` | `pd.isna(x)` | `ismissing(x)` |
| Aide | `?fn` | `help(fn)` | `?fn` |

## Suites de valeurs

| Concept | R | Python | Julia |
|---|---|---|---|
| Créer | `c(1, 2, 3)` | `[1, 2, 3]` | `[1, 2, 3]` |
| **Premier élément** | `x[1]` | `x[0]` | `x[1]` |
| Dernier élément | `x[length(x)]` | `x[-1]` | `x[end]` |
| Tranche (2e au 4e) | `x[2:4]` | `x[1:4]` | `x[2:4]` |
| Longueur | `length(x)` | `len(x)` | `length(x)` |
| Séquence 1 à 5 | `1:5` | `range(1, 6)` | `1:5` |
| Valeurs distinctes | `unique(x)` | `set(x)` · `.unique()` | `unique(x)` |

> **Le piège n°1 du passage d'un langage à l'autre.** R et Julia comptent à partir
> de **1**. Python compte à partir de **0**. Ce n'est pas une coquetterie : c'est une
> source de bugs silencieux, qui ne plantent pas et décalent tous vos résultats d'un
> cran.

## Correspondances clé → valeur

| Concept | R | Python | Julia |
|---|---|---|---|
| Créer | `list(a = 1, b = 2)` | `{"a": 1, "b": 2}` | `Dict("a" => 1, "b" => 2)` |
| Accéder | `d$a` · `d[["a"]]` | `d["a"]` | `d["a"]` |

## Tableaux de données

| Concept | R | Python (pandas) | Julia (DataFrames) |
|---|---|---|---|
| Créer | `data.frame(x = 1:3)` | `pd.DataFrame({"x": [1,2,3]})` | `DataFrame(x = 1:3)` |
| Lire un CSV | `read.csv("f.csv")` | `pd.read_csv("f.csv")` | `CSV.read("f.csv", DataFrame)` |
| Écrire un CSV | `write.csv(d, "f.csv")` | `d.to_csv("f.csv")` | `CSV.write("f.csv", d)` |
| Premières lignes | `head(d)` | `d.head()` | `first(d, 6)` |
| Dimensions | `dim(d)` | `d.shape` | `size(d)` |
| Une colonne | `d$qty` | `d["qty"]` | `d.qty` |
| Filtrer des lignes | `subset(d, qty > 0)` | `d[d.qty > 0]` | `filter(:qty => >(0), d)` |
| Nouvelle colonne | `d$uv <- d$val / d$qty` | `d["uv"] = d.val / d.qty` | `d.uv = d.val ./ d.qty` |

## Fonctions et structures de contrôle

| Concept | R | Python | Julia |
|---|---|---|---|
| Définir | `f <- function(x) { x * 2 }` | `def f(x): return x * 2` | `f(x) = 2x` |
| Condition | `if (x > 0) { ... } else { ... }` | `if x > 0: ... else: ...` | `if x > 0 ... else ... end` |
| Boucle | `for (i in 1:5) { ... }` | `for i in range(5): ...` | `for i in 1:5 ... end` |

## Opérer sur toute une colonne d'un coup

C'est la vraie différence entre les trois, et elle vaut la peine d'être comprise.

| Concept | R | Python | Julia |
|---|---|---|---|
| Multiplier tout par 2 | `x * 2` | `np.array(x) * 2` | `x .* 2` |
| Appliquer une fonction | `f(x)` si `f` est vectorisée | `[f(i) for i in x]` | `f.(x)` |

- **R** est vectorisé par défaut : `x * 2` marche sur tout le vecteur. Héritage
  statisticien.
- **Python** ne l'est pas sur les listes : il faut `numpy` ou `pandas` pour retrouver
  ce comportement.
- **Julia** l'exprime explicitement avec un **point** : `.` signifie « applique
  élément par élément ». `f.(x)` applique `f` à chaque élément. C'est verbeux d'un
  caractère, et parfaitement clair.

## Packages

| Concept | R | Python | Julia |
|---|---|---|---|
| Installer (une fois) | `install.packages("sf")` | `pip install geopandas` | `] add GeoDataFrames` |
| Charger (chaque session) | `library(sf)` | `import geopandas` | `using GeoDataFrames` |

**Installer ≠ charger.** `there is no package called 'sf'` veut dire : pas installé.
`could not find function "st_read"` veut dire : installé, mais pas chargé.

## Fichiers et chemins

| Concept | R | Python | Julia |
|---|---|---|---|
| Répertoire courant | `getwd()` | `os.getcwd()` | `pwd()` |
| Assembler un chemin | `file.path("data", "raw")` | `Path("data") / "raw"` | `joinpath("data", "raw")` |
| Racine du projet | `here::here()` | `Path(__file__).parent.parent` | `@__DIR__` |

**Ne jamais écrire `setwd()`.** Ouvrez un Projet RStudio (`.Rproj`), ou construisez
vos chemins depuis la racine du projet.

---

## Trois pièges à connaître d'avance

**Concaténer du texte.** `paste0("a", "b")` en R, `"a" + "b"` en Python, et
`"a" * "b"` en Julia — oui, l'étoile. Julia réserve `+` aux nombres.

**Les accolades.** R et Julia délimitent les blocs (`{}` pour R, `end` pour Julia).
Python les délimite par **l'indentation** : décaler une ligne de quatre espaces change
la logique du programme. Ce n'est pas du style, c'est de la syntaxe.

**Les guillemets.** `"texte"` fonctionne partout. En R et Python, `'texte'` aussi.
En Julia, `'a'` désigne **un seul caractère**, pas une chaîne — et une chaîne d'un
caractère s'écrit `"a"`.
