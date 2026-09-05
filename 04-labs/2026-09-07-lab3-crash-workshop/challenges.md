# TP3 — Défis

## 1. L'autre langage

Refaites les cinq scripts dans l'autre langage. Les messages d'erreur ne se
ressemblent pas ; les causes, si.

Dressez la correspondance :

| Cause | Message R | Message Python |
|---|---|---|
| fichier introuvable | | |
| fonction introuvable | | |
| objet introuvable | | |
| type invalide | | |

Cette table vaut plus que les corrections elles-mêmes.

## 2. Écrire le garde-fou qui aurait attrapé le script 5

Le problème du script 5 est qu'il additionne un agrégat avec ses composantes.

Écrivez une **assertion** qui rend ce bug impossible — c'est-à-dire une ligne qui
fait échouer le script au lieu de le laisser produire un résultat faux :

```r
stopifnot(!"World" %in% oak$partnerDesc)
```

Puis généralisez : quelles autres assertions poseriez-vous d'emblée sur ce jeu de
données ? Écrivez-en trois.

C'est exactement ce qu'on appelle un **test**, et c'est le sujet du 23 octobre.

## 3. Le reprex

Prenez le script 5 **avant correction** et transformez-le en exemple minimal
reproductible destiné à quelqu'un qui n'a pas le fichier de données : trois lignes de
données fabriquées à la main, le code réduit au strict nécessaire, et l'énoncé du
comportement attendu contre le comportement observé.

Vous devez tomber sous les dix lignes.

C'est l'exercice du bloc suivant. Prenez de l'avance.

## 4. Fabriquer un sixième script

Écrivez vous-même un script qui produit un résultat faux sans lever d'erreur, sur ce
jeu de données. Échangez-le avec un autre binôme.

Trois pistes, si vous en voulez : les unités, les statistiques miroir, les valeurs
manquantes qui disparaissent silencieusement d'une moyenne.

Le meilleur sera ajouté au dépôt pour la promotion suivante — avec votre nom, si vous
le souhaitez.

## 5. Comment auriez-vous pu le voir ?

Sans regarder les données, estimez de tête : la France exporte-t-elle pour 450 ou pour
900 millions de dollars de grumes de chêne sur trois ans ?

Cherchez un ordre de grandeur externe — récolte française de chêne, prix moyen du
mètre cube, statistiques douanières publiées. Vous devez pouvoir trancher.

C'est **le** réflexe qui protège de l'erreur silencieuse, et il ne s'écrit pas en
code : savoir à quoi devrait ressembler le résultat avant de le calculer.
