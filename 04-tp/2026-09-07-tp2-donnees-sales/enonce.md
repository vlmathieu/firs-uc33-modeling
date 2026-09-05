# TP2 — Lire des données sales

**Lundi 7 septembre · 14h15 – 15h00 · 45 minutes · en binôme**

## Objectif

Charger un fichier réel, diagnostiquer ce qui ne va pas, le nettoyer par un script,
et produire un graphique.

Ce n'est pas un exercice artificiel. Le fichier `comtrade_fr_roundwood_dirty.csv`
n'a pas été trafiqué pour vous piéger : c'est ce que produit un export depuis un Excel
configuré en français. Vous en recevrez de cette forme toute votre carrière.

**Travaillez en miroir R / Python** : l'un de vous en R, l'autre en Python, puis
comparez. Vous verrez que les problèmes sont les mêmes et que les solutions se
ressemblent.

---

## Socle

### 1. Regarder avant de charger (5 min)

Téléchargez `comtrade_fr_roundwood_dirty.csv` dans `data/raw/`.

**Ne l'ouvrez pas dans Excel.** Regardez ses premières lignes depuis le terminal :

```
head -3 data/raw/comtrade_fr_roundwood_dirty.csv
```

Répondez à ces quatre questions avant d'écrire la moindre ligne de code :

- quel est le séparateur de colonnes ?
- quel est le séparateur décimal ?
- pourquoi certains champs sont-ils entre guillemets ?
- combien y a-t-il de colonnes ?

### 2. Charger naïvement, et constater (5 min)

```r
trade <- read.csv("data/raw/comtrade_fr_roundwood_dirty.csv")
str(trade)
```

Regardez le résultat et décrivez ce qui s'est passé. Combien de colonnes obtenez-vous ?
De quel type est `qty` ? Que valent les noms de pays ?

Faites la moyenne des quantités. Que se passe-t-il, et pourquoi ?

### 3. Charger correctement (10 min)

Trois choses à déclarer : le séparateur, la décimale, l'encodage.

```r
trade <- read.csv("data/raw/comtrade_fr_roundwood_dirty.csv",
                  sep = ";", dec = ",", fileEncoding = "latin1")
```

```python
trade = pd.read_csv("data/raw/comtrade_fr_roundwood_dirty.csv",
                    sep=";", decimal=",", encoding="latin-1")
```

Vérifiez trois choses :

- `Côte d'Ivoire` et `Türkiye` s'affichent correctement ;
- `qty`, `netWgt` et `primaryValue` sont bien numériques ;
- vous avez 674 lignes et 12 colonnes.

> **Un piège que vous allez rencontrer en Python.** La colonne `qtyUnitAbbr` contient
> la chaîne littérale `N/A`, qui signifie « unité non renseignée ». pandas la convertit
> automatiquement en valeur manquante. Est-ce ce que vous voulez ? Argumentez, puis
> décidez — et écrivez votre décision en commentaire.

### 4. Diagnostiquer (10 min)

Écrivez un court bloc de contrôle qui répond à ces questions :

- combien de valeurs manquantes, et dans quelles colonnes ?
- combien de lignes ont `qty = 0` ?
- quelles unités apparaissent dans `qtyUnitAbbr` ?
- quelles valeurs distinctes prend `partnerDesc` ? **Regardez bien cette liste.**

La dernière question est la plus importante du TP.

### 5. Nettoyer (10 min)

Produisez `data/processed/trade_clean.csv` à partir de la version brute, par un
script, en documentant chaque décision en commentaire — le *pourquoi*, pas le *quoi*.

Au minimum :

- traiter le cas de l'agrégat `World` ;
- décider quoi faire des lignes `qty = 0` ;
- décider quoi faire des poids nets manquants ;
- convertir `period` en nombre si vous en avez besoin comme tel.

Il n'y a pas une seule bonne réponse. Il y a des décisions, qui doivent être écrites.

### 6. Un graphique (5 min)

Produisez dans `output/figures/` une figure qui montre **l'évolution 2022-2024 des
exportations françaises de grumes de chêne (`440391`) par pays de destination**, en
valeur.

Gardez les cinq premiers partenaires, agrégez le reste.

---

## Le piège à ne pas manquer

`World` n'est pas un pays. C'est l'agrégat de tous les partenaires.

Si vous sommez `primaryValue` sans exclure ces lignes, **votre total est exactement le
double du vrai**. Aucune erreur ne sera levée. Votre graphique sera joli. Vos chiffres
seront faux.

Vérifiez votre nettoyage : sur les lignes où la France est déclarante, le total avec
`World` fait 1 557,0 M$ et sans `World` 778,5 M$.

Si vous trouvez 1 557, relisez votre filtre.

---

## Ce que vous devez avoir compris en sortant

- Un CSV n'est pas un format, c'est une famille de formats. Séparateur, décimale et
  encodage se déclarent, ils ne se devinent pas.
- Une colonne numérique lue comme du texte ne plante pas toujours : parfois elle donne
  un résultat faux.
- Une valeur manquante peut être codée de cinq manières dans le même fichier.
- **Regarder les valeurs distinctes d'une colonne avant de sommer** est le geste qui
  vous évitera le plus d'erreurs cette année.

Défis pour ceux qui ont fini : [`defis.md`](defis.md).
