# TP1 — Monter son projet propre

**Lundi 7 septembre · 13h30 – 14h15 · 45 minutes · en binôme**

## Objectif

À la fin de ce TP, votre dossier de travail tourne **sur la machine de votre binôme,
sans qu'il ait rien à modifier**. C'est le cran 3 de l'échelle de reproductibilité,
et il sera vérifié par quelqu'un d'autre que vous.

Vous travaillez chacun sur votre machine. Le contrôle croisé est en fin de séance.

---

## Socle

### 1. Récupérer le gabarit (5 min)

Téléchargez le dépôt `uc33-project-template` (bouton vert *Code* → *Download ZIP*),
décompressez-le, renommez le dossier `uc33-tp1`.

**Placez-le en dehors de tout dossier synchronisé** — pas dans OneDrive, iCloud,
Google Drive ni Dropbox. Ces services déplacent les fichiers sous vos pieds. Si vous
n'avez pas le choix, notez-le : nous en reparlerons si quelque chose casse.

Vérifiez que vous obtenez bien cette arborescence :

```
uc33-tp1/
├── data/
│   ├── raw/
│   └── processed/
├── src/
├── output/
│   ├── figures/
│   └── tables/
├── config/
├── README.md
└── uc33-tp1.Rproj
```

### 2. Installer les données (2 min)

Téléchargez `comtrade_fr_roundwood_clean.csv` depuis
[`05-data/`](../../05-data/) et placez-le dans **`data/raw/`**.

À partir de maintenant, ce fichier est en lecture seule. Vous ne l'ouvrez pas dans
Excel, vous ne l'écrasez pas, vous ne le renommez pas.

### 3. Ouvrir le projet, des deux façons (5 min)

**Dans RStudio** : double-cliquez sur `uc33-tp1.Rproj`. Vérifiez en haut à droite que
le nom du projet apparaît, puis tapez dans la console :

```r
getwd()
```

Le résultat doit être la racine de `uc33-tp1`. C'est ce que fait le fichier `.Rproj`,
et c'est la raison pour laquelle vous n'écrirez jamais `setwd()`.

**Dans VS Code** : *File* → *Open Folder* → sélectionnez `uc33-tp1`. Vous devez voir
toute l'arborescence dans l'explorateur de gauche, et non un seul fichier.

### 4. Réparer un script (15 min)

Ouvrez `src/01_import.R`. Il contient trois problèmes. Corrigez-les.

1. Un **chemin absolu**. Remplacez-le par un chemin relatif à la racine du projet.
2. Un **`setwd()`**. Supprimez-le. Il ne doit rien casser : si le projet est ouvert
   correctement, il est inutile.
3. Une **sortie écrite au mauvais endroit**. Les données retraitées vont dans
   `data/processed/`, jamais à côté des données brutes.

Le script doit produire `data/processed/trade_france.csv` et rien d'autre.

### 5. Installer et charger un paquet (5 min)

```r
install.packages("here")   # une fois, sur la machine
library(here)              # à chaque session, en haut du script
```

Remplacez votre chemin relatif par un appel à `here()` :

```r
read.csv(here("data", "raw", "comtrade_fr_roundwood_clean.csv"))
```

Comprenez la différence entre les deux lignes : la première télécharge, la seconde
déclare un besoin. Elles ne s'écrivent pas au même endroit et pas au même rythme.

### 6. « Restart and run all » (5 min)

Dans RStudio : `Session > Restart R` (ou `Ctrl+Shift+F10`), puis `Ctrl+Shift+Entrée`.

Votre script doit tourner **de haut en bas, depuis une session vide, sans
intervention**. S'il plante, vous venez de trouver un bug maintenant plutôt que ce
soir.

Répétez jusqu'à ce que ce soit propre.

### 7. Écrire le README (3 min)

Quatre lignes suffisent, mais elles doivent répondre à trois questions :

- à quoi sert ce dossier ?
- que faut-il installer pour le faire tourner ?
- dans quel ordre lancer les scripts ?

C'est ce document qui fait passer votre projet du cran 2 au cran 3.

### 8. Contrôle croisé (5 min)

Échangez vos dossiers avec votre binôme — clé USB, ou une archive zip envoyée par
mail. Chacun ouvre le projet de l'autre et exécute son script.

**Règle : vous n'avez pas le droit de modifier quoi que ce soit, ni de poser une
question.** Si ça ne tourne pas, notez pourquoi et rendez le dossier.

C'est le seul test qui compte.

---

## Ce que vous devez avoir compris en sortant

- Un `.Rproj` ouvert fixe le répertoire de travail. C'est tout le problème réglé.
- Un chemin absolu est une déclaration : « ce script ne marchera que chez moi ».
- Installer et charger un paquet sont deux gestes distincts.
- Un script qui ne survit pas à un redémarrage de session n'est pas terminé.

Défis pour ceux qui ont fini : [`defis.md`](defis.md).
