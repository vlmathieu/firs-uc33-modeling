# TP3 — Atelier de crash

**Lundi 7 septembre · 15h15 – 16h05 · 50 minutes · en binôme**

## Objectif

Cinq scripts. Aucun ne fait ce qu'il annonce. Réparez-les.

Ce n'est pas un exercice de rapidité. **L'objectif est la méthode**, pas le nombre de
scripts réparés. Un binôme qui traite trois scripts en expliquant chaque diagnostic a
mieux travaillé qu'un binôme qui en corrige cinq au hasard.

Les scripts sont dans [`scripts-casses/`](scripts-casses/), en version R et en
version Python. Prenez celle que vous voulez ; le défi 1 consiste à faire l'autre.

---

## La méthode en quatre temps

À appliquer pour chacun, dans cet ordre, sans sauter d'étape.

1. **Lire l'erreur.** En entier, jusqu'à la dernière ligne. Un message d'erreur est
   une *information*, pas une punition. Il contient presque toujours le nom de l'objet
   fautif et le numéro de ligne.
2. **Lire la documentation** de la fonction concernée. `?read.csv`, `help(pd.read_csv)`.
3. **Chercher** le message sur un moteur de recherche, en retirant ce qui vous est
   propre.
4. **Demander** — au binôme, puis à l'enseignant.

Pour chaque script, notez sur une feuille :

| | |
|---|---|
| **Symptôme** | ce que la machine affiche |
| **Diagnostic** | ce qui ne va pas, en une phrase |
| **Correction** | ce que vous avez changé |
| **Prévention** | ce qui aurait évité ce bug dès l'écriture |

La colonne *Prévention* est celle qui vous servira toute l'année.

---

## Les cinq scripts

Prérequis : les deux fichiers de [`05-data/`](../../05-data/) doivent être dans
`data/raw/`, et vous travaillez depuis un projet ouvert correctement (TP1).

### 1. `01_chemin`
Compte les lignes du jeu de données. **Message attendu :** le fichier n'existe pas.

### 2. `02_paquet`
Affiche les cinq premières lignes. **Message attendu :** quelque chose est introuvable
— une *fonction* en R (`could not find function "read_csv"`), un *nom* en Python
(`NameError: name 'pd' is not defined`).

Attention : il y a **deux causes possibles** à ce type de message. Identifiez laquelle
s'applique ici, et dites comment vous auriez distingué les deux.

### 3. `03_nom`
Calcule une quantité moyenne. **Message attendu :** un objet est introuvable.
Le plus court des cinq à corriger, et le plus fréquent dans la vraie vie.

Observation à faire au passage, elle vaut le détour : Python vous souffle la réponse
(`Did you mean: 'exports'?`), R se contente de `object 'export' not found`. Les
messages d'erreur ne se valent pas d'un langage à l'autre. Notez-le.

### 4. `04_type`
Calcule une valeur totale, à partir du fichier **sale**. Le problème est un problème
de **type**, et il ne se manifeste pas de la même façon dans les deux langages. C'est
tout l'intérêt de ce script.

**En R**, une erreur est levée : `invalid 'type' (character) of argument`. Le langage
refuse d'additionner du texte.

**En Python**, rien ne plante. `sum()` sur une colonne de texte **concatène les
chaînes** et vous rend un nombre de 6 349 caractères de long. Le programme se termine
normalement.

Diagnostiquez la cause commune, corrigez les deux, puis répondez : lequel des deux
comportements préférez-vous, et pourquoi ?

**Deuxième problème, en R uniquement.** Une fois l'erreur de type corrigée, regardez
les noms de pays et la colonne `qtyUnitAbbr`. Vous verrez apparaître `m\xb3` et des
chaînes illisibles. Essayez de retrouver « Côte d'Ivoire » avec un `grepl()` : vous ne
trouverez **rien**, alors que la sous-chaîne `voire` est bien là. Expliquez pourquoi,
puis corrigez. Rien ne plante à aucun moment.

### 5. `05_silencieux` — le plus important des cinq

Ce script **ne plante pas**. Il s'exécute proprement et affiche :

```
Exportations francaises de grumes de chene, 2022-2024 :
   909.7 millions USD
   104 flux declares
```

Les deux langages donnent le même résultat, au centime près. Ils ont donc tort de la
même manière — ce qui devrait déjà vous alerter sur la valeur d'un « ça donne pareil
dans les deux ».

Le nombre est faux. Il est exactement **le double** de la bonne réponse.

Votre travail :

1. trouver pourquoi, sans qu'on vous dise où regarder ;
2. corriger ;
3. **répondre à la question qui compte : comment auriez-vous pu vous en apercevoir
   si je ne vous avais pas prévenus ?**

Trois lignes sur cent quatre suffisent à doubler le résultat. Aucun message, aucun
avertissement, aucune couleur rouge. Un graphique parfaitement présentable, et une
conclusion fausse.

C'est le type d'erreur qui survit à une soutenance, qui se retrouve dans un rapport,
et qui oriente une décision. Les quatre premiers scripts vous font perdre dix minutes.
Le cinquième vous fait perdre votre crédibilité.

---

## Ce que vous devez avoir compris en sortant

- Un message d'erreur est un cadeau : il vous dit où regarder. L'absence de message
  ne veut pas dire que tout va bien.
- Les quatre messages du jour — fichier introuvable, fonction ou nom introuvable,
  objet introuvable, type invalide — représentent l'écrasante majorité de ce que vous
  rencontrerez cette année.
- **Un langage plus permissif n'est pas un langage plus sûr.** R refuse d'additionner
  du texte ; Python le fait sans broncher. Le script 4 le montre en une ligne.
- **La seule protection contre l'erreur silencieuse est de savoir à quoi devrait
  ressembler le résultat avant de le calculer.**

Les corrigés sont publiés sur ce dépôt **après la séance**.

Défis pour ceux qui ont fini : [`defis.md`](defis.md).
