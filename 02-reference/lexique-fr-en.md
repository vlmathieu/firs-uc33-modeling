# Lexique du code — français ↔ anglais

Le cours est dispensé en anglais, la documentation que vous lirez l'est aussi, et les
messages d'erreur également. Cette page fait le pont.

Les termes **en gras** sont ceux que vous devez reconnaître à l'oral dès le
7 septembre.

## Le socle — onze mots

| Français | English | En une ligne |
|---|---|---|
| **variable** | variable | une étiquette collée sur une valeur |
| **type** | type | la nature d'une valeur : nombre, texte, booléen |
| **vecteur** | vector | une suite de valeurs de même type |
| **tableau de données** | data frame | une feuille de calcul vue par un langage |
| **dictionnaire** | dictionary, dict | une correspondance clé → valeur |
| **fonction** | function | une machine : elle prend, elle rend |
| **argument** | argument | ce qu'on donne à la fonction |
| **valeur de retour** | return value | ce qu'elle rend |
| **boucle** | loop | répéter une opération, un élément à la fois |
| **vectorisation** | vectorisation | appliquer l'opération à toute la colonne d'un coup |
| **paquet**, bibliothèque | package, library | du code écrit par quelqu'un d'autre |

## Types et valeurs

| Français | English |
|---|---|
| entier | integer, `int` |
| nombre décimal, flottant | float, double, `numeric` |
| chaîne de caractères | string, character |
| booléen | boolean, logical |
| valeur manquante | missing value, `NA`, `NaN`, `None` |
| affectation | assignment |
| conversion de type | casting, coercion |

## Écrire du code

| Français | English |
|---|---|
| script | script |
| en-tête | header |
| commentaire | comment |
| indentation | indentation |
| accolade `{}` | brace, curly bracket |
| crochet `[]` | square bracket |
| parenthèse `()` | parenthesis (pl. parentheses) |
| guillemet `"` | quote, quotation mark |
| point-virgule `;` | semicolon |
| deux-points `:` | colon |
| tiret bas `_` | underscore |
| barre oblique `/` | slash · **antislash `\`** : backslash |

## Fichiers et système

| Français | English |
|---|---|
| chemin | path |
| chemin absolu / relatif | absolute / relative path |
| répertoire de travail | working directory |
| dossier, répertoire | folder, directory |
| dossier parent | parent directory |
| encodage | encoding |
| séparateur | separator, delimiter |
| séparateur décimal | decimal separator |
| terminal, ligne de commande | terminal, shell, command line |
| invite de commande | prompt |
| exécuter, lancer | run, execute |

## Quand ça casse

| Français | English |
|---|---|
| erreur | error |
| avertissement | warning |
| message d'erreur | error message |
| déboguer | debug |
| exemple minimal reproductible | reproducible example, **reprex** |
| plantage | crash |
| erreur silencieuse | silent failure |
| jeu de test | test suite |
| assertion, garde-fou | assertion, sanity check |

## Projet et reproductibilité

| Français | English |
|---|---|
| dépôt | repository, repo |
| versionner | to version, version control |
| valider (un changement) | to commit |
| branche | branch |
| fusion | merge |
| conflit | conflict |
| dépendance | dependency |
| environnement (virtuel) | (virtual) environment |
| fichier de verrouillage | lockfile |
| reproductibilité | reproducibility |
| gabarit, modèle de projet | template |
| données brutes | raw data |
| données retraitées | processed data |

## Quatre faux amis

| Piège | Explication |
|---|---|
| *library* | en R, `library()` **charge** un paquet déjà installé ; ce n'est pas « installer ». Et une *library* n'est pas une librairie mais une bibliothèque. |
| *to commit* | ne veut pas dire « s'engager » : enregistrer un instantané de son travail. |
| *argument* | rien à voir avec une dispute : la valeur passée à une fonction. |
| *character* | en R, `character` désigne du **texte**, pas un caractère isolé. |
