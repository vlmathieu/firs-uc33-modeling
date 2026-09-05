# Jeux de données

## `comtrade_fr_roundwood_clean.csv` et `comtrade_fr_roundwood_dirty.csv`

Le **commerce extérieur français de bois ronds**, 2022-2024, d'après UN Comtrade.

Deux fichiers, **le même contenu**. Seul le format change.

| Fichier | Encodage | Séparateur | Décimales |
|---|---|---|---|
| `..._clean.csv` | UTF-8 | `,` | `.` |
| `..._dirty.csv` | Latin-1 | `;` | `,` |

Le second n'a pas été bricolé pour l'exercice : c'est ce que produit un export
depuis un Excel configuré en français. Vous en recevrez de cette forme toute votre
carrière.

---

## Périmètre

| Dimension | Sélection |
|---|---|
| Source | UN Comtrade, classification SH, données annuelles |
| Période | 2022, 2023, 2024 |
| Filtre | toutes les lignes où **la France est déclarante ou partenaire** |
| Produits | 3 positions à 6 chiffres, toutes en **bois ronds** (grumes) |
| Flux | importations et exportations |
| Volume | **674 lignes, 12 colonnes** |

### Les trois produits

| Code SH | Produit |
|---|---|
| `440323` | Bois de sapin (*Abies* spp.) et d'épicéa (*Picea* spp.), bruts, plus grande dimension transversale ≥ 15 cm |
| `440349` | Bois tropicaux bruts, autres que dark red meranti, light red meranti et meranti bakau |
| `440391` | Bois de chêne (*Quercus* spp.), bruts |

Tous sont des **grumes** : du bois non transformé. C'est délibéré — l'export de
grumes de chêne françaises est un sujet de politique forestière vivant, et les
données le montrent.

---

## Dictionnaire des variables

| Colonne | Type | Description |
|---|---|---|
| `period` | texte | Année de référence. **Stockée en texte**, pas en nombre. |
| `reporterISO` | texte | Code ISO3 du pays déclarant |
| `reporterDesc` | texte | Nom du pays déclarant |
| `flowDesc` | texte | `Import` ou `Export`, **du point de vue du déclarant** |
| `partnerISO` | texte | Code ISO3 du partenaire ; `W00` pour l'agrégat « World » |
| `partnerDesc` | texte | Nom du partenaire ; **`World` = tous partenaires confondus** |
| `cmdCode` | texte | Position SH à 6 chiffres |
| `cmdDesc` | texte | Libellé officiel du produit. Contient des points-virgules et des virgules. |
| `qtyUnitAbbr` | texte | Unité de la quantité : `m³`, ou `N/A` si non renseignée |
| `qty` | nombre | Quantité, dans l'unité de `qtyUnitAbbr` |
| `netWgt` | nombre | Poids net, **en kilogrammes** |
| `primaryValue` | nombre | Valeur du flux, **en dollars américains** |

---

## Ce que ces données contiennent vraiment

Rien de ce qui suit n'a été ajouté. Tout vient de la source.

| Caractéristique | Ampleur |
|---|---|
| Lignes où le partenaire est l'agrégat `World` | 18 |
| Quantités nulles (`qty = 0`) | 17 |
| Poids net manquant | 11 |
| Unité non renseignée (`N/A`) | 11 |
| Pays aux noms accentués | Côte d'Ivoire, Türkiye, Saint Barthélemy |
| Lignes où la France commerce avec la France | 3 |
| Densités apparentes physiquement impossibles | ~13 % des lignes |
| Pays déclarants distincts | 63 |
| Partenaires distincts | 68 |

### Trois choses à savoir avant de faire une somme

**1. `World` n'est pas un pays.** C'est l'agrégat de tous les partenaires. Additionner
la colonne `primaryValue` sans exclure ces lignes **double exactement le total** —
et rien ne vous préviendra. Sur les lignes où la France est déclarante :
1 557,0 M$ avec `World`, 778,5 M$ sans. Facteur 2,00.

**2. Deux pays ne déclarent pas la même chose.** En 2023, la France déclare avoir
exporté 147 158 m³ de grumes de chêne vers la Chine pour 57,2 M$. La Chine déclare
en avoir importé 283 521 m³ pour 128,4 M$ depuis la France. Un facteur 1,9 en volume.
Ce sont les *statistiques miroir*, et l'écart est un objet d'étude en soi.

**3. `netWgt / qty` donne une densité, et elle est parfois absurde.** La médiane est
à 884 kg/m³, plausible pour du bois vert. Mais 13 % des lignes tombent hors de
l'intervalle physiquement défendable [200, 1300] kg/m³ — avec des valeurs à
1 kg/m³ et à plus de 40 000 kg/m³. Un calcul de densité ne plantera pas pour autant.
C'est exactement le genre de résultat faux et silencieux qu'un garde-fou attrape et
qu'un œil distrait laisse passer.

---

## Provenance et licence

- **Source** : United Nations Comtrade Database, <https://comtradeplus.un.org/>
- **Extraction** : chapitre SH 44, données annuelles, réalisée par V. Mathieu.
- **Traitement** : sélection de lignes et de colonnes uniquement. **Aucune valeur
  n'a été modifiée, corrigée ou inventée.** Le fichier « sale » diffère du fichier
  « propre » par son seul encodage-séparateur-décimale.
- **Réutilisation** : extrait dérivé de faible volume, redistribué à des fins
  d'enseignement. Toute réutilisation doit citer UN Comtrade comme source.

Le fichier source complet (2 millions de lignes) n'est pas versionné dans ce dépôt.
