# TP1 — Défis

À prendre si vous avez terminé le socle. Ne les faites pas à la place du socle.

## 1. La version Python

Refaites l'étape 4 en Python, dans `src/01_import.py`, avec `pathlib` :

```python
from pathlib import Path
ROOT = Path(__file__).parent.parent
```

Comparez avec la solution R. Qu'est-ce qui est plus explicite dans chacune des deux ?

## 2. Casser volontairement le projet

Déplacez `uc33-tp1` ailleurs sur votre disque, puis relancez le script. Si vous avez
bien travaillé, rien ne change. Si quelque chose casse, vous aviez encore un chemin
absolu quelque part.

Recommencez en renommant le dossier.

## 3. Les paramètres hors du code

Créez `config/config.yml` :

```yaml
fichier_entree: data/raw/comtrade_fr_roundwood_clean.csv
annee_min: 2023
```

Lisez-le depuis R (`yaml::read_yaml()`) ou Python (`yaml.safe_load()`) et faites
disparaître toutes les valeurs écrites en dur de votre script.

C'est un avant-goût du 23 octobre.

## 4. Le nommage à l'épreuve

Créez dans `data/raw/` un fichier nommé `Données récoltées (final).csv`, essayez de
le lire depuis votre script, et expliquez à votre binôme **trois raisons distinctes**
pour lesquelles ce nom est un problème.

Puis supprimez-le.

## 5. Lire le dépôt du cours comme un projet

Ouvrez [le dépôt de l'UC](https://github.com/vlmathieu/firs-uc33-modeling) et vérifiez
qu'il respecte les règles qu'il vous impose : pas d'accent ni d'espace dans les noms,
dates en `AAAA-MM-JJ`, ordre explicite, README à la racine.

**S'il ne les respecte pas quelque part, ouvrez une issue.** C'est sérieux : la
première trouvée gagne le droit de le dire en cours.
