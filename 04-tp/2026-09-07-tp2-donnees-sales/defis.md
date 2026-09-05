# TP2 — Défis

## 1. Le bois qui flotte dans l'air

Calculez la densité apparente de chaque flux : `netWgt / qty`, en kg/m³, sur les
lignes en `m³`.

La médiane devrait tomber autour de 880 kg/m³ — plausible pour du bois vert.

Maintenant regardez les extrêmes. Vous trouverez des densités inférieures à 10 kg/m³
et supérieures à 40 000. Le bois le plus léger du monde (le balsa) est à 160 kg/m³ ;
le plus lourd (le gaïac) à 1 250.

**Écrivez un garde-fou** qui refuse de continuer si une densité sort de
l'intervalle [200, 1300] :

```r
stopifnot(all(d$dens > 200 & d$dens < 1300, na.rm = TRUE))
```

Combien de lignes échouent ? Que décidez-vous d'en faire — et pourquoi cette décision
doit-elle être écrite dans le script plutôt que dans votre tête ?

C'est le principe d'un **test** : si le modèle crée du carbone, il est faux, et un
test le dit. Nous y reviendrons le 23 octobre.

## 2. Les statistiques miroir

En 2023, pour les grumes de chêne (`440391`) :

- que déclare la France exporter vers la Chine ?
- que déclare la Chine importer depuis la France ?

Calculez l'écart, en volume et en valeur.

Puis généralisez : construisez une table qui, pour chaque partenaire, compare ce que
la France déclare et ce que le partenaire déclare.

Trouvez au moins **deux explications plausibles** à ces écarts. (Indices : le bois
transite par des ports étrangers ; les pays ne comptent pas les mêmes frais dans la
valeur.)

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
