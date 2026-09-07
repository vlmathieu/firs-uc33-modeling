# ---------------------------------------------------------------
# 04_mirror.py -- SOLUTION, lab 2 challenge 2
#
# Input  : data/processed/trade_clean.csv
# Output : output/tables/mirror_gaps.csv
# ---------------------------------------------------------------

# --- Dependencies ---
from pathlib import Path
import pandas as pd

# --- Parameters ---
ROOT = Path(__file__).resolve().parents[1]
OAK  = 440391
YEAR = 2023

# --- Load ---
clean = pd.read_csv(ROOT / "data" / "processed" / "trade_clean.csv")

# --- 1. One case: French oak logs to China, 2023 ---
fr_says = clean[(clean.cmdCode == OAK) & (clean.period == YEAR)
                & (clean.flowDesc == "Export")
                & (clean.reporterDesc == "France") & (clean.partnerDesc == "China")]
cn_says = clean[(clean.cmdCode == OAK) & (clean.period == YEAR)
                & (clean.flowDesc == "Import")
                & (clean.reporterDesc == "China") & (clean.partnerDesc == "France")]

print(f"France reports exporting: {fr_says.primaryValue.iloc[0]/1e6:.1f} M$, "
      f"{fr_says.qty.iloc[0]:.0f} m3")
print(f"China reports importing : {cn_says.primaryValue.iloc[0]/1e6:.1f} M$, "
      f"{cn_says.qty.iloc[0]:.0f} m3")
print(f"Ratio, value            : "
      f"{cn_says.primaryValue.iloc[0]/fr_says.primaryValue.iloc[0]:.2f}")

# --- 2. The general comparison: a join ---
# For the two tables to line up, the columns must MEAN the same thing: in the
# mirror table the reporter is France's partner, so it is renamed first.
# Name the columns after the ROLES, not after the file. In every row France is
# the exporter and the other country the importer, whichever one filed the
# declaration -- and "the importer declares more" is readable three weeks later
# in a way that "primaryValue_y" is not.
exports = (clean[(clean.reporterDesc == "France") & (clean.flowDesc == "Export")]
           [["period", "cmdCode", "partnerDesc", "primaryValue"]]
           .rename(columns={"partnerDesc": "importer",
                            "primaryValue": "value_exporter"}))

mirror = (clean[(clean.partnerDesc == "France") & (clean.flowDesc == "Import")]
          [["period", "cmdCode", "reporterDesc", "primaryValue"]]
          .rename(columns={"reporterDesc": "importer",
                           "primaryValue": "value_importer"}))

# An inner join: only the flows both sides reported have a mirror to compare.
comp = exports.merge(mirror, on=["period", "cmdCode", "importer"])
comp["ratio"] = comp.value_importer / comp.value_exporter

print(f"\nMirror pairs found: {len(comp)}")
print(f"Median ratio      : {comp.ratio.median():.2f}")
print(comp.sort_values("ratio", ascending=False)
          [["period", "cmdCode", "importer", "ratio"]].head(5))

# --- 3. How big is the CIF/FOB effect on the whole file? ---
# Imports are valued CIF (goods + insurance + freight), exports FOB (goods
# alone). The same cargo does not carry the same price in the two reports.
totals = clean.groupby("flowDesc").primaryValue.sum()
print(f"\nReported exports: {totals['Export']/1e6:.1f} M$")
print(f"Reported imports: {totals['Import']/1e6:.1f} M$")
print(f"Ratio           : {totals['Import']/totals['Export']:.2f}")

# --- Conclusion ---
# 1. CIF/FOB explains a gap of the order of 10 to 20 %, and on this file the
#    reported imports are about 1.7 times the reported exports. Real, and
#    nowhere near enough on its own.
# 2. Transit does the rest: timber leaving France through a Belgian or Dutch
#    port is a French export to Belgium and a Chinese import from France.
#    Country of consignment and country of origin are two different questions.
# 3. Reporting thresholds and classification differences finish the job.
#    Mirror statistics are a DIAGNOSTIC, not a correction: they tell you the
#    two figures disagree, never which one is right.

# --- Output ---
comp.to_csv(ROOT / "output" / "tables" / "mirror_gaps.csv", index=False)
