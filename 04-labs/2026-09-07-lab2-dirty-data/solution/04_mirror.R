# ---------------------------------------------------------------
# 04_mirror.R -- SOLUTION, lab 2 challenge 2
#
# Input  : data/processed/trade_clean.csv
# Output : output/tables/mirror_gaps.csv
# ---------------------------------------------------------------

# --- Dependencies ---
library(here)

# --- Parameters ---
OAK  <- 440391
YEAR <- 2023

# --- Load ---
clean <- read.csv(here("data", "processed", "trade_clean.csv"))

# --- 1. One case: French oak logs to China, 2023 ---
# The same cargo, described twice: once by the seller, once by the buyer.
fr_says <- subset(clean, cmdCode == OAK & period == YEAR & flowDesc == "Export" &
                         reporterDesc == "France" & partnerDesc == "China")
cn_says <- subset(clean, cmdCode == OAK & period == YEAR & flowDesc == "Import" &
                         reporterDesc == "China" & partnerDesc == "France")

cat("France reports exporting:", round(fr_says$primaryValue / 1e6, 1), "M$,",
    fr_says$qty, "m3\n")
cat("China reports importing :", round(cn_says$primaryValue / 1e6, 1), "M$,",
    cn_says$qty, "m3\n")
cat("Ratio, value            :", round(cn_says$primaryValue / fr_says$primaryValue, 2), "\n")

# --- 2. The general comparison: a join ---
# Two tables describing the same flows from the two ends. To line them up we
# need the columns to MEAN the same thing: in the mirror table the reporter is
# the partner of France, so it is renamed before joining.
# Name the columns after the ROLES, not after the file. In every row France is
# the exporter and the other country the importer, whichever one filed the
# declaration -- and "the importer declares more" is readable three weeks later
# in a way that "primaryValue_y" is not.
exports <- subset(clean, reporterDesc == "France" & flowDesc == "Export",
                  select = c(period, cmdCode, partnerDesc, primaryValue))
names(exports)[names(exports) == "partnerDesc"]  <- "importer"
names(exports)[names(exports) == "primaryValue"] <- "value_exporter"

mirror  <- subset(clean, partnerDesc == "France" & flowDesc == "Import",
                  select = c(period, cmdCode, reporterDesc, primaryValue))
names(mirror)[names(mirror) == "reporterDesc"]  <- "importer"
names(mirror)[names(mirror) == "primaryValue"]  <- "value_importer"

# merge keeps only the rows present on BOTH sides: a flow reported by one
# country and not the other simply has no mirror to compare against.
comp <- merge(exports, mirror, by = c("period", "cmdCode", "importer"))
comp$ratio <- comp$value_importer / comp$value_exporter

cat("\nMirror pairs found:", nrow(comp), "\n")
cat("Median ratio      :", round(median(comp$ratio), 2), "\n")
print(head(comp[order(-comp$ratio), c("period", "cmdCode", "importer", "ratio")], 5))

# --- 3. How big is the CIF/FOB effect on the whole file? ---
# An import is valued CIF (goods + insurance + freight to the importer's
# border), an export FOB (goods alone). Two countries describing the same
# cargo therefore do not put the same things in the price.
totals <- tapply(clean$primaryValue, clean$flowDesc, sum)
cat("\nReported exports:", round(totals[["Export"]] / 1e6, 1), "M$\n")
cat("Reported imports:", round(totals[["Import"]] / 1e6, 1), "M$\n")
cat("Ratio           :", round(totals[["Import"]] / totals[["Export"]], 2), "\n")

# --- Conclusion ---
# 1. CIF/FOB explains a gap of the order of 10 to 20 %, and on this file the
#    reported imports are about 1.7 times the reported exports. It is a real
#    effect and it is nowhere near enough on its own.
# 2. Transit does the rest: timber leaving France through a Belgian or Dutch
#    port is a French export to Belgium and a Chinese import from France.
#    Country of consignment and country of origin are two different questions.
# 3. Reporting thresholds and classification differences finish the job.
#    Mirror statistics are a DIAGNOSTIC, not a correction: they tell you the
#    two figures disagree, never which one is right.

# --- Output ---
write.csv(comp, here("output", "tables", "mirror_gaps.csv"), row.names = FALSE)
