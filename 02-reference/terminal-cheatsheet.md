# Mémo — le terminal, minimum vital

Une fenêtre où vous **tapez le nom d'un programme au lieu de cliquer sur son icône**.
C'est tout. L'interface la plus ancienne, et la plus précise.

## Où le trouver

| Système | Où |
|---|---|
| Windows | menu Démarrer → *Terminal* ou *PowerShell* |
| macOS | Applications › Utilitaires › Terminal |
| RStudio | onglet **Terminal**, à côté de la Console |
| VS Code | ``Ctrl+` `` (ou menu *Terminal* → *New Terminal*) |

Le plus souvent, vous ne l'ouvrirez pas séparément : il est dans votre éditeur.

## Les cinq gestes

| Ce que vous voulez | macOS / Linux | Windows (PowerShell) |
|---|---|---|
| Où suis-je ? | `pwd` | `pwd` |
| Que contient ce dossier ? | `ls` | `ls` ou `dir` |
| Aller dans un dossier | `cd nom_du_dossier` | idem |
| Remonter d'un niveau | `cd ..` | idem |
| Lancer un script | `Rscript script.R` · `python script.py` | idem |

**Un terminal est toujours quelque part.** Dans un dossier. C'est le point le plus
important de cette page : la plupart des « fichier introuvable » viennent de là.

## La touche à retenir avant toutes les autres

**TAB.**

Tapez les trois premières lettres d'un nom de fichier ou de dossier, appuyez sur TAB,
le terminal complète. Cela évite 90 % des fautes de frappe — et une faute de frappe
dans un chemin coûte dix minutes.

Utilisez TAB. Systématiquement.

## Le PATH, et « command not found »

Quand vous tapez `python`, le terminal ne fouille pas votre disque. Il regarde dans
**une liste courte de dossiers, connue d'avance** : le **PATH**.

| Message | Ce que ça veut dire |
|---|---|
| `command not found` (macOS) | soit le programme n'est pas installé, |
| `n'est pas reconnu en tant que commande...` (Windows) | soit il l'est mais n'est pas dans le PATH |

Savoir laquelle des deux, c'est déjà 90 % du dépannage. Sous Windows, la cause la
plus fréquente est la case **« Add python.exe to PATH »** oubliée à l'installation.

## Vérifier son installation

```
python --version
git --version
quarto --version
```

Chacune doit renvoyer un numéro de version.

## Quelques commandes utiles ensuite

| Commande | Effet |
|---|---|
| `cd ~` | aller dans son dossier personnel |
| `mkdir mon_dossier` | créer un dossier |
| `cat fichier.csv` | afficher le contenu d'un fichier texte |
| `head -5 fichier.csv` | afficher les 5 premières lignes — utile sur un gros CSV |
| `↑` (flèche haut) | rappeler la commande précédente |
| `Ctrl+C` | interrompre un programme qui tourne |
