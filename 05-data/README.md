# Jeux de données

## `comtrade_fr_roundwood_clean.csv` et `comtrade_fr_roundwood_dirty.csv`

Le **commerce extérieur français de bois ronds**, 2022-2024, d'après UN Comtrade.

Deux fichiers, **le même contenu**. Seul le format change.

| Fichier | Encodage | Séparateur | Décimales |
|---|---|---|---|
| `..._clean.csv` | UTF-8 | `,` | `.` |
| `..._dirty.csv` | Latin-1 | `;` | `,` |

Le second n'a pas été bricolé pour l'exercice : c'est ce que produit un export depuis
un Excel configuré en français. Vous en recevrez de cette forme toute votre carrière.

---

## Périmètre

| Dimension | Sélection |
|---|---|
| Source | UN Comtrade, classification SH, données annuelles |
| Période | 2022, 2023, 2024 |
| Filtre | toutes les lignes où **la France est déclarante ou partenaire** |
| Produits | 3 positions à 6 chiffres, toutes en **bois ronds** (grumes) |
| Flux | importations et exportations |
| Volume | **674 lignes, 13 colonnes** |

### Les trois produits

| Code SH | Produit |
|---|---|
| `440323` | Bois de sapin (*Abies* spp.) et d'épicéa (*Picea* spp.), bruts, plus grande dimension transversale ≥ 15 cm |
| `440349` | Bois tropicaux bruts, autres que dark red meranti, light red meranti et meranti bakau |
| `440391` | Bois de chêne (*Quercus* spp.), bruts |

Tous sont des **grumes** : du bois non transformé. C'est délibéré — l'export de grumes
de chêne françaises est un sujet de politique forestière vivant, et les données le
montrent.

---

## Dictionnaire des variables

### Identification du flux

| Colonne | Type | Description |
|---|---|---|
| `period` | texte | Année de référence. **Stockée en texte**, pas en nombre. |
| `reporterISO` | texte | Code ISO3 du pays déclarant |
| `reporterDesc` | texte | Nom du pays déclarant |
| `flowDesc` | texte | `Import` ou `Export`, **du point de vue du déclarant** |
| `partnerISO` | texte | Code ISO3 du partenaire. **`W00` = agrégat « tous partenaires ».** |
| `partnerDesc` | texte | Nom du partenaire ; `World` pour l'agrégat |
| `cmdCode` | texte | Position SH à 6 chiffres |
| `cmdDesc` | texte | Libellé officiel du produit. Contient des points-virgules et des virgules. |

### Produit et quantités

| Colonne | Type | Description |
|---|---|---|
| `aggrLevel` | entier | Niveau d'agrégation de la position SH. **Vaut 6 sur les 674 lignes** de cet extrait. |
| `qtyUnitAbbr` | texte | Unité de `qty` : `m³`, ou `N/A` si non renseignée |
| `qty` | nombre | Quantité dans l'unité ci-dessus |
| `netWgt` | nombre | Poids net, **en kilogrammes** |
| `primaryValue` | nombre | Valeur du flux, **en dollars américains** |

> Deux colonnes de grandeur, deux unités différentes : `qty` est un **volume** en m³,
> `netWgt` un **poids** en kg. Leur rapport est une densité, et c'est là que
> commence le travail du TP2.

---

## Ce que ces données contiennent vraiment

Rien de ce qui suit n'a été ajouté. Tout vient de la source.

| Caractéristique | Ampleur |
|---|---|
| Lignes où le partenaire est l'agrégat `World` | 18 |
| Quantités nulles (`qty = 0`) | 17 |
| Poids net manquant | 11 |
| Unité de `qty` non renseignée (`N/A`) | 11 |
| `aggrLevel` | **vaut 6 sur les 674 lignes** |
| Pays aux noms accentués | Côte d'Ivoire, Türkiye, Saint Barthélemy |
| Lignes où la France commerce avec la France | 3 |
| Pays déclarants distincts | 63 |
| Partenaires distincts | 68 |

---

## Quatre choses à savoir avant de calculer

### 1. `World` n'est pas un pays

C'est l'agrégat de tous les partenaires. Additionner `primaryValue` sans exclure ces
lignes **double exactement le total** — et rien ne vous préviendra. Sur les lignes où
la France est déclarante : **1 557,0 M$ avec `World`, 778,5 M$ sans. Facteur 2,00.**

Le repère fiable est `partnerISO == "W00"` — le code réservé à l'agrégat. Filtrer sur
le nom `partnerDesc != "World"` marche aussi, mais un nom se traduit et se renomme,
un code non.

### 2. Une colonne constante n'est pas une donnée

`aggrLevel` vaut **6 sur les 674 lignes**. C'est normal — l'extrait ne retient que des
positions SH à six chiffres — mais cela veut dire qu'aucun filtre, aucun regroupement
et aucune statistique sur cette colonne n'apporte quoi que ce soit.

Regardez la distribution de vos colonnes avant de les utiliser. Une colonne constante
se repère en une ligne (`table()` en R, `.nunique()` en Python) et vous évite de
construire un regroupement qui ne regroupe rien.

### 3. `netWgt / qty` donne une densité, et elle mérite une enquête

La médiane est à **884 kg/m³**, parfaitement plausible pour du bois vert.
Mais **13 %** des lignes tombent hors de l'intervalle physiquement défendable
[200, 1300] kg/m³, avec des valeurs à 1 kg/m³ et à plus de 40 000.

Ce n'est pas inexplicable, et le jeu de données contient de quoi enquêter :
**les anomalies se concentrent massivement sur les petits flux.** Parmi les lignes
sous 10 m³, **46 %** sont aberrantes ; au-dessus de 10 m³, seulement **8 %**. Le
volume médian d'une ligne aberrante est de 20 m³, contre 742 m³ pour une ligne
plausible.

Conclusion honnête, et c'est celle que vous devez pouvoir écrire vous-même : l'essentiel
des densités absurdes vient d'arrondis et de seuils de déclaration sur des flux
minuscules. Ce n'est ni une erreur de votre code, ni une raison de tout jeter — c'est
une raison de filtrer explicitement, et d'écrire pourquoi.

### 4. Deux pays ne déclarent pas la même chose

En 2023, la France déclare avoir exporté 147 158 m³ de grumes de chêne vers la Chine
pour 57,2 M$. La Chine déclare en avoir importé 283 521 m³ pour 128,4 M$ depuis la
France. Facteur 1,9 en volume.

Ce sont les **statistiques miroir**. Une partie de l'écart est structurelle : un import
est valorisé **CIF** — marchandise, assurance et fret jusqu'à la frontière de
l'importateur — tandis qu'un export est valorisé **FOB**, marchandise seule. Les deux
pays décrivent la même cargaison et n'y mettent pas les mêmes choses. Sur ce jeu, les
imports déclarés totalisent 1 253,6 M$ et les exports 752,1 M$.

Le reste — transit par des ports étrangers, pays d'origine contre pays d'expédition,
seuils de déclaration — est un objet d'étude à part entière.

---

## Provenance et licence

- **Source** : United Nations Comtrade Database, <https://comtradeplus.un.org/>
- **Extraction** : chapitre SH 44, données annuelles, réalisée par V. Mathieu.
- **Traitement** : sélection de lignes et de colonnes uniquement. **Aucune valeur n'a
  été modifiée, corrigée ou inventée.** Le fichier « sale » ne diffère du fichier
  « propre » que par son encodage, son séparateur et sa décimale.
- **Réutilisation** : extrait dérivé de faible volume, redistribué à des fins
  d'enseignement. Toute réutilisation doit citer UN Comtrade comme source.

Le fichier source complet (2 millions de lignes) n'est pas versionné dans ce dépôt.
