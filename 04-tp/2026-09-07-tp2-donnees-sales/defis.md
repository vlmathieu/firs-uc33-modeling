# TP2 — Défis

## 1. Le bois qui flotte dans l'air — enquête

Calculez la densité apparente de chaque flux : `netWgt / qty`, en kg/m³, sur les
lignes où `qtyUnitAbbr` vaut `m³`.

La médiane tombe autour de **884 kg/m³** — plausible pour du bois vert.

Maintenant regardez les extrêmes. Vous trouverez des densités inférieures à 10 kg/m³
et supérieures à 40 000. Le bois le plus léger du monde, le balsa, est à 160 kg/m³ ;
le plus lourd, le gaïac, à 1 250. Environ **13 %** des lignes sortent de l'intervalle
défendable [200, 1300].

**Écrivez d'abord un garde-fou**, c'est-à-dire une ligne qui fait échouer le script
plutôt que de le laisser produire un résultat faux :

```r
stopifnot(all(d$dens > 200 & d$dens < 1300, na.rm = TRUE))
```

Puis menez l'enquête. Le jeu de données contient de quoi répondre — c'est le but de
l'exercice, et il n'y a pas une seule bonne réponse.

**Piste a — la taille du flux.** Comparez le volume médian des lignes aberrantes à
celui des lignes plausibles. Puis découpez par tranche de volume : moins de 10 m³,
10 à 100, 100 à 1 000, plus de 1 000. Le résultat est net, et c'est la vraie
explication.

**Piste b — les unités.** Toutes les lignes sont-elles bien en m³ ? Que faites-vous
des onze lignes où `qtyUnitAbbr` vaut `N/A` — les inclure dans un calcul de densité
a-t-il un sens ?

**Piste c — les zéros.** Dix-sept lignes ont `qty = 0`. Que produit la division ?
Ce résultat traverse-t-il une moyenne sans rien signaler ?

À la fin, écrivez **trois lignes de conclusion** dans votre script, en commentaire :
qu'est-ce qui explique quoi, que gardez-vous, que jetez-vous, et pourquoi.

C'est le principe d'un **test** : si le modèle crée du carbone, il est faux, et un
test le dit. Mais un test qui rejette 13 % de données correctes est un mauvais test.
Toute la difficulté est là. Nous y reviendrons le 23 octobre.

## 2. Les statistiques miroir

En 2023, pour les grumes de chêne (`440391`) :

- que déclare la France exporter vers la Chine ?
- que déclare la Chine importer depuis la France ?

Calculez l'écart, en volume et en valeur.

Puis généralisez : construisez une table qui, pour chaque partenaire, compare ce que
la France déclare et ce que le partenaire déclare.

Trouvez au moins **deux explications plausibles** à ces écarts.

La première explication est une convention de valorisation. Un import est compté
**CIF** — marchandise, assurance et fret jusqu'à la frontière de l'importateur — et
un export **FOB**, marchandise seule. Deux pays décrivant la même cargaison n'y
mettent donc pas les mêmes choses.

Quantifiez : sur ce jeu, quel est le total des imports déclarés, et celui des exports ?
L'écart suffit-il à expliquer le facteur observé sur le chêne vers la Chine, ou
faut-il autre chose ?

Cherchez au moins deux autres explications. Pistes : le bois transite par des ports
étrangers ; pays d'origine et pays d'expédition ne coïncident pas ; les seuils de
déclaration ne sont pas les mêmes partout.

## 3. La France commerce avec la France

Trois lignes du fichier ont `reporterDesc` et `partnerDesc` égaux à `France`.

Ce n'est pas une erreur de saisie. Trouvez de quoi il s'agit, et décidez si ces lignes
doivent rester dans votre jeu nettoyé.

## 4. Un CSV vraiment hostile

Ouvrez `comtrade_fr_roundwood_dirty.csv` dans Excel, **sans rien enregistrer**.
Regardez ce qui arrive aux noms de pays accentués et aux grandes valeurs numériques.

Puis fermez sans sauvegarder.

Écrivez trois lignes expliquant à un collègue pourquoi « jeter juste un œil dans
Excel » est un geste dangereux sur une donnée brute.

## 5. Le format qui ne pose aucun de ces problèmes

Réenregistrez votre table nettoyée en **Parquet** (`arrow::write_parquet()` en R,
`d.to_parquet()` en Python). Comparez la taille, la vitesse de relecture, et
demandez-vous ce qu'il advient des types de colonnes.

Pourquoi le CSV reste-t-il malgré tout le format le plus utilisé au monde ?
