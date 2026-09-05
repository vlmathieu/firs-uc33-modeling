# UC 3.3 Modeling — matériel de cours

Parcours **FIRS** (*Forests and their Environment, Innovative Resources and
Sustainability*) — AgroParisTech, année 2026-2027.
Unité de cours 3.3, rattachée à l'UE 3. Intervenants : A. Lobianco, V. Mathieu.

Ce dépôt rassemble tout ce dont vous avez besoin pour l'UC : supports, travaux
pratiques, jeux de données, fiches de référence, et le dossier de la cartographie
des modèles.

---

## Par où commencer

| Vous êtes… | Allez à |
|---|---|
| avant la première séance | [`00-admin/guide-installation.md`](00-admin/guide-installation.md) |
| bloqué sur une erreur | [`00-admin/comment-poser-une-question.md`](00-admin/comment-poser-une-question.md), puis [ouvrez une issue](https://github.com/vlmathieu/firs-uc33-modeling/issues/new/choose) |
| en train de chercher un mot | [`02-reference/lexique-fr-en.md`](02-reference/lexique-fr-en.md) |
| en train de traduire du R en Python | [`02-reference/equivalences-r-python-julia.md`](02-reference/equivalences-r-python-julia.md) |
| en TP | [`04-tp/`](04-tp/) |
| sur la cartographie des modèles | [`06-cartography/`](06-cartography/) |

---

## Organisation

```
00-admin/        installation, protocole de demande d'aide
01-fascicule/    le livret de cours (source Quarto + PDF imprimable)
02-reference/    lexique, équivalences entre langages, mémo terminal
03-cours/        supports de CM, un dossier par séance
04-tp/           énoncés, défis et corrigés des travaux pratiques
05-data/         jeux de données jouets, avec leur dictionnaire
06-cartography/  guidance note, grille d'analyse, critères d'évaluation
07-liens.md      ressources externes
```

Les dossiers sont préfixés et les séances datées en `AAAA-MM-JJ` pour que l'ordre
alphabétique soit l'ordre de lecture. Ce n'est pas une coquetterie : c'est l'une des
règles enseignées dans l'UC, et **ce dépôt applique ce qu'il enseigne**. Vous êtes
invités à le vérifier, et à signaler tout endroit où il ne s'y tient pas.

Rien n'est jamais renommé ni déplacé : un lien donné en septembre fonctionne encore
en janvier.

---

## Ce qui change, et quand

Le dépôt évolue toute l'année. Les ajouts et surtout les **corrections** sont consignés
dans [`CHANGELOG.md`](CHANGELOG.md).

Si vous travaillez sur du matériel téléchargé il y a quelques semaines, c'est le
premier fichier à ouvrir.

---

## Poser une question

Les **issues de ce dépôt sont le canal de questions techniques de l'UC**.

Une question posée ici reçoit une réponse que toute la promotion peut lire — et votre
blocage n'est presque jamais le vôtre seul. Le formulaire vous demande votre système,
votre version, un exemple minimal et le message d'erreur complet : ce n'est pas de la
bureaucratie, c'est exactement la démarche du *reprex* enseignée le 7 septembre. Il
arrive souvent qu'on trouve la réponse en remplissant le formulaire.

[→ Ouvrir une issue](https://github.com/vlmathieu/firs-uc33-modeling/issues/new/choose) · [→ Le protocole en trois minutes](00-admin/comment-poser-une-question.md)

Dépôt public : aucun nom, aucune note, aucune donnée personnelle dans les issues ni
dans les captures d'écran.

---

## Licences

- **Code** (scripts, exemples, gabarits) : [MIT](LICENSE).
- **Documents** (supports, énoncés, fascicule, notes) :
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr) — réutilisation
  libre, y compris commerciale et modifiée, à condition de citer la source.
- **Données** : voir [`05-data/README.md`](05-data/README.md). Les extraits proviennent
  d'UN Comtrade et sont redistribués à des fins d'enseignement, avec leur provenance.

Pour citer ce matériel : voir [`CITATION.cff`](CITATION.cff).
