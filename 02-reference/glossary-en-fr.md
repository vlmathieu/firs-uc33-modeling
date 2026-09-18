# Code glossary — English ↔ French

The course is delivered in English, the documentation you will read is in English, and
so are the error messages. This page is the bridge.

Terms in **bold** are the ones you must recognise by ear from 7 September.

## The core — eleven words

| English | Français | In one line |
|---|---|---|
| **variable** | variable | a label stuck onto a value |
| **type** | type | the nature of a value: number, text, boolean |
| **vector** | vecteur | a sequence of values of the same type |
| **data frame** | tableau de données | a spreadsheet as seen by a programming language |
| **dictionary**, dict | dictionnaire | a key → value mapping |
| **function** | fonction | a machine: it takes something in, it gives something back |
| **argument** | argument | what you hand to the function |
| **return value** | valeur de retour | what it hands back |
| **loop** | boucle | repeating an operation, one element at a time |
| **vectorisation** | vectorisation | applying the operation to the whole column at once |
| **package**, library | paquet, bibliothèque | code someone else wrote that you reuse |

## Types and values

| English | Français |
|---|---|
| integer, `int` | entier |
| float, double, `numeric` | nombre décimal, flottant |
| string, character | chaîne de caractères |
| boolean, logical | booléen |
| missing value, `NA`, `NaN`, `None` | valeur manquante |
| assignment | affectation |
| casting, coercion | conversion de type |

## Writing code

| English | Français |
|---|---|
| script | script |
| header | en-tête |
| comment | commentaire |
| indentation | indentation |
| brace, curly bracket `{}` | accolade |
| square bracket `[]` | crochet |
| parenthesis (pl. parentheses) `()` | parenthèse |
| quote, quotation mark `"` | guillemet |
| semicolon `;` | point-virgule |
| colon `:` | deux-points |
| underscore `_` | tiret bas |
| slash `/` · **backslash `\`** | barre oblique · antislash |

## Files and system

| English | Français |
|---|---|
| path | chemin |
| absolute / relative path | chemin absolu / relatif |
| working directory | répertoire de travail |
| folder, directory | dossier, répertoire |
| parent directory | dossier parent |
| encoding | encodage |
| separator, delimiter | séparateur |
| decimal separator | séparateur décimal |
| terminal, shell, command line | terminal, ligne de commande |
| prompt | invite de commande |
| run, execute | exécuter, lancer |

## When things break

| English | Français |
|---|---|
| error | erreur |
| warning | avertissement |
| error message | message d'erreur |
| debug | déboguer |
| reproducible example, **reprex** | exemple minimal reproductible |
| crash | plantage |
| silent failure | erreur silencieuse |
| test suite | jeu de test |
| assertion, sanity check | assertion, garde-fou |

## Project and reproducibility

| English | Français |
|---|---|
| repository, repo | dépôt |
| to version, version control | versionner |
| to commit | valider (un changement) |
| branch | branche |
| merge | fusion |
| conflict | conflit |
| dependency | dépendance |
| (virtual) environment | environnement (virtuel) |
| lockfile | fichier de verrouillage |
| reproducibility | reproductibilité |
| template | gabarit, modèle de projet |
| raw data | données brutes |
| processed data | données retraitées |

## Python tooling

The vocabulary of [handbook part 1](../01-handbook/README.md), chapter 1 in particular.

| English | Français | In one line |
|---|---|---|
| **interpreter** | interpréteur | the program that executes Python; several can coexist on one machine |
| **kernel** | noyau | an interpreter running behind a notebook, keeping its state |
| module | module | one `.py` file you `import` |
| standard library | bibliothèque standard | the modules that come with every Python |
| third-party package | paquet tiers | anything you must install: pandas, matplotlib… |
| **package manager** | gestionnaire de paquets | the tool that installs packages: pip, conda |
| distribution | distribution | a way of packaging Python: python.org, Miniforge, Anaconda… |
| channel | canal | where conda downloads from: conda-forge |
| wheel | wheel (archive précompilée) | a pre-built package file, one per Python version and system |
| **PATH** | PATH (variable d'environnement) | the list of folders the terminal searches for a command |
| `site-packages` | dossier des paquets installés | the folder, inside one interpreter, where its packages live |
| to activate (an environment) | activer | tell the terminal which interpreter `python` means |
| console, REPL | console interactive | the `>>>` prompt where Python is typed one line at a time |
| notebook | carnet, notebook | a `.ipynb` file of cells with their output |
| cell | cellule | one block of code in a notebook or after `# %%` |
| **traceback** | trace d'appels, traceback | the error report: calls from top to bottom, message last |
| extension | extension | what teaches VS Code a language |
| command palette | palette de commandes | `Ctrl+Shift+P`: every VS Code action by name |
| status bar | barre d'état | the bottom strip of VS Code; the interpreter shows bottom right |
| workspace | espace de travail | the folder opened in VS Code |
| shortcut | raccourci clavier | |

## Four false friends

| Trap | Why |
|---|---|
| *library* | In R, `library()` **loads** an already-installed package; it does not install it. And a *library* is a `bibliothèque`, not a `librairie` (a bookshop). |
| *to commit* | Nothing to do with `s'engager`: it means saving a snapshot of your work. |
| *argument* | Nothing to do with a dispute: it is the value passed to a function. |
| *character* | In R, `character` means **text**, not a single character. |
