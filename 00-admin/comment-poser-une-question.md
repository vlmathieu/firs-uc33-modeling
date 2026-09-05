# Comment poser une question technique

*Trois minutes de lecture. La compétence la plus rentable de l'année.*

---

## Pourquoi ça compte

Vous allez poser des questions techniques pendant toute votre carrière : à un forum,
à un collègue, à une IA, à un enseignant. La qualité de la réponse est presque
entièrement déterminée par la qualité de la question.

« Ça marche pas » n'a pas de réponse. Pas parce que la personne en face est de
mauvaise volonté, mais parce qu'il n'y a **rien à quoi répondre**.

Et il y a un bénéfice secondaire, qui est en fait le principal : **on trouve très
souvent la réponse en formulant la question.** Réduire son problème à un exemple
minimal, c'est déjà déboguer.

---

## Le reprex

Un *reprex* — **repr**oducible **ex**ample — est le plus petit programme complet qui
reproduit votre problème. Il a quatre propriétés.

**Minimal.** Retirez tout ce qui n'est pas nécessaire au déclenchement de l'erreur.
Vos 300 lignes se réduisent presque toujours à 5. Faites la réduction : c'est là que
la cause apparaît.

**Complet.** Quelqu'un doit pouvoir copier-coller votre code et obtenir la même
erreur. Cela veut dire : les `library()` / `import` en haut, et les données incluses.

**Reproductible.** Pas de chemin absolu, pas de fichier que vous seul possédez. Si le
problème vient de vos données, fabriquez trois lignes de données jouets qui le
reproduisent :

```r
# au lieu de : read.csv("C:/Users/moi/Documents/mes_donnees.csv")
d <- data.frame(qty = c(12.5, 0, 3.1), netWgt = c(9800, 450, NA))
```

**Accompagné du message d'erreur COMPLET.** En texte, jamais en capture d'écran, et
en entier. La ligne que vous jugez inutile est souvent celle qui contient la cause.

---

## La méthode en quatre temps, avant de demander

1. **Lire l'erreur.** En entier, jusqu'au bout. Un message d'erreur est une
   *information*, pas une punition. Il contient presque toujours le nom de l'objet
   fautif et le numéro de la ligne.
2. **Lire la documentation.** `?read.csv` en R, `help(pd.read_csv)` en Python.
3. **Chercher.** Collez le message d'erreur dans un moteur de recherche, en retirant
   ce qui vous est propre (vos noms de fichiers, vos noms de variables).
4. **Demander.** Avec un reprex.

Le quatrième temps est légitime. Il vient après les trois autres.

---

## Où demander

**Les issues de ce dépôt** sont le canal officiel de l'UC.

[→ Ouvrir une issue](https://github.com/vlmathieu/firs-uc33-modeling/issues/new/choose)

Le formulaire vous demande exactement les éléments ci-dessus. Ce n'est pas de
l'administration : c'est le reprex, imposé par l'outil.

Avantage sur le mail : la réponse est lisible par toute la promotion, et elle reste
consultable. Votre blocage n'est presque jamais le vôtre seul.

Dépôt public : aucun nom, aucune donnée personnelle, aucune capture contenant un
identifiant.

---

## Et l'IA ?

Les mêmes règles s'appliquent, pour la même raison : une IA à qui vous donnez le
contexte, la version et le message d'erreur complet répond bien mieux qu'à « ça
marche pas ».

Deux différences à garder en tête. Une IA répond toujours, y compris quand elle a
tort, et avec le même ton assuré. Et elle ne vous dira pas qu'elle n'a pas compris.
Demandez-lui une **explication** plutôt qu'un bloc de code à recopier — vous saurez
alors si la réponse tient.

Le cadre de déclaration de l'usage de l'IA dans vos rendus est traité dans le cours
dédié de la formation et rappelé au §9 du syllabus.
