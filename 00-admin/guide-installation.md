# Prérequis machine — ce qu'il faut installer

*Version du 4 septembre 2026. Envoyée par mail avant la première séance.*

Comptez **45 minutes à 1 heure**. Partout où ce n'est pas précisé, gardez les options
par défaut de l'installateur.

Installez dans l'ordre : R avant RStudio, sinon RStudio ne trouvera rien à piloter.

---

## a. R

<https://cloud.r-project.org/>

Choisissez votre système, puis le lien **base**.

## b. RStudio Desktop

<https://posit.co/download/rstudio-desktop/>

Version gratuite. **Après R.**

## c. Python 3.12 ou plus

<https://www.python.org/downloads/>

> **Windows — la seule case qui compte.** Sur le premier écran de l'installateur,
> cochez **« Add python.exe to PATH »** avant de cliquer sur *Install*. Elle n'est pas
> cochée par défaut. Sans elle, Python s'installe correctement mais reste invisible
> depuis le terminal, et vous passerez une heure à chercher pourquoi.

> **macOS.** Installez-le quand même. Le Python livré avec le système est ancien et
> réservé à l'usage interne de macOS.

## d. VS Code

<https://code.visualstudio.com/Download>

Puis **trois extensions**, via l'icône Extensions de la barre latérale
(`Ctrl+Shift+X` sous Windows, `Cmd+Shift+X` sous macOS) :

| Extension | Éditeur |
|---|---|
| **Python** | Microsoft |
| **R** | REditorSupport |
| **Quarto** | Quarto |

## e. Quarto

<https://quarto.org/docs/get-started/>

## f. git

<https://git-scm.com/downloads>

git ne sera enseigné qu'en octobre. Installez-le **maintenant** quand même : cela
économisera environ 45 minutes le 20 octobre, et l'installation est le seul moment
où ça peut mal se passer.

- **Windows** : toutes les options par défaut, sans exception. L'installateur pose
  beaucoup de questions ; les réponses proposées sont les bonnes.
- **macOS** : tapez `git --version` dans le Terminal. macOS vous proposera de
  l'installer lui-même.

## g. Un compte GitHub

<https://github.com/signup>

Gratuit.

> Prenez comme identifiant **`prenom-nom`** plutôt qu'un pseudonyme. Ce compte vous
> suivra : il figurera sur votre CV, et un recruteur le regardera. Un profil lisible
> est un actif.

Demandez ensuite le **GitHub Student Pack** avec votre adresse AgroParisTech :
<https://education.github.com/pack>

---

## Vérification — 2 minutes

Ouvrez un terminal.

- **Windows** : menu Démarrer → *Terminal* ou *PowerShell*
- **macOS** : Applications › Utilitaires › Terminal

Tapez les trois commandes suivantes, une par une :

```
python --version
git --version
quarto --version
```

**Chacune doit renvoyer un numéro de version.** Si l'une répond
`command not found` (macOS) ou `n'est pas reconnu en tant que commande interne ou
externe` (Windows), c'est que le programme n'est pas installé, **ou** qu'il est
installé mais introuvable depuis le terminal — le plus souvent la case PATH oubliée
au point (c).

Ouvrez enfin RStudio et VS Code une fois chacun, pour vérifier qu'ils démarrent.

---

## Si ça bloque

Ne restez pas coincé seul jusqu'au dernier moment. Ouvrez une issue sur ce dépôt
([→ formulaire](https://github.com/vlmathieu/firs-uc33-modeling/issues/new/choose)) en indiquant :

1. votre système d'exploitation ;
2. l'étape exacte qui coince ;
3. **le message d'erreur complet**, copié en texte.

Ce n'est pas une formalité : savoir décrire un problème de façon exploitable est une
compétence du programme, et vous la pratiquerez toute l'année.
Voir [`comment-poser-une-question.md`](comment-poser-une-question.md).

Si vous n'êtes pas administrateur de votre machine et ne pouvez rien installer,
signalez-le : une solution existe.
