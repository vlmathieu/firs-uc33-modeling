# ---------------------------------------------------------------
# 02_cleaning_challenges.R -- SOLUTION, lab 2 core + challenge 1
#
# The brief on its own is 02_cleaning.R. This script adds the apparent
# density and the aberrant values (challenge 1), and overwrites the same
# trade_clean.csv with two extra columns. The figure is 03_figure.R.
#
# Input  : data/raw/comtrade_fr_roundwood_dirty.csv
# Output : data/processed/trade_clean.csv  (+ density, density_suspect)
# ---------------------------------------------------------------

# --- Dependencies ---
library(here)

# --- Parameters ---
DENS_MIN <- 200      # kg/m3 -- lighter than balsa (160): impossible
DENS_MAX <- 1300     # kg/m3 -- heavier than lignum vitae (1250): impossible

# --- Load ---
# sep, dec and fileEncoding must be DECLARED. Without them read.csv fails on
# "more columns than column names": the assumed separator is the comma, which
# also appears inside the cmdDesc labels.
trade <- read.csv(here("data", "raw", "comtrade_fr_roundwood_dirty.csv"),
                  sep = ";", dec = ",", fileEncoding = "latin1")

stopifnot(nrow(trade) == 674, ncol(trade) == 13)

# --- Diagnose ---
cat("Missing values per column:\n"); print(colSums(is.na(trade))[colSums(is.na(trade)) > 0])
cat("qty == 0      :", sum(trade$qty == 0, na.rm = TRUE), "\n")
cat("units of qty  :", unique(trade$qtyUnitAbbr), "\n")
cat("aggrLevel     :", unique(trade$aggrLevel), "<- constant, unusable\n")

# --- Clean ---
# 1. World is the all-partners aggregate: keeping it doubles every total.
#    Filter on the CODE partnerISO == "W00" rather than on the name: a name
#    gets translated and renamed, a reserved code does not.
clean <- subset(trade, partnerISO != "W00")

# 2. aggrLevel equals 6 on all 674 rows: constant column, no use at all.
clean$aggrLevel <- NULL

# 3. The types. qty, netWgt and primaryValue are the columns at risk: their
#    decimal mark is a comma, and undeclared they arrive as character.
stopifnot(is.numeric(clean$qty), is.numeric(clean$netWgt),
          is.numeric(clean$primaryValue))

# 4. Apparent density, only where a volume is actually reported.
#    qty == 0 would yield Inf, which travels through a mean without a sound.
volume <- ifelse(clean$qtyUnitAbbr == "m³" & clean$qty > 0, clean$qty, NA)
clean$density <- clean$netWgt / volume

# 5. We KEEP the aberrant densities, but flag them.
#    They cluster on very small flows (46 % below 10 m3, 8 % above): rounding
#    and reporting thresholds, not data entry errors.
clean$density_suspect <- !(clean$density >= DENS_MIN & clean$density <= DENS_MAX)

cat("\nRows kept        :", nrow(clean), "out of", nrow(trade), "\n")
cat("Median density   :", round(median(clean$density, na.rm = TRUE)), "kg/m3\n")
cat("Suspect densities:", sum(clean$density_suspect, na.rm = TRUE), "\n")

# --- Check: the total must have been halved ---
fr <- subset(clean, reporterDesc == "France")
cat("France total     :", round(sum(fr$primaryValue) / 1e6, 1), "M$ (expected 778.5)\n")
stopifnot(abs(sum(fr$primaryValue) / 1e6 - 778.5) < 0.1)

# --- Challenge 1: WHY are the densities aberrant? ---
# The guard rail first. It fails, and that is the point: a script that
# refuses to lie beats a script that quietly produces a wrong mean.
#   stopifnot(all(d$density > DENS_MIN & d$density < DENS_MAX))   # fails
d <- subset(clean, !is.na(density))

# Split the flows into volume bands and look at the share of aberrant
# densities inside each one.
d$band <- cut(d$qty, breaks = c(0, 10, 100, 1000, Inf),
              labels = c("< 10", "10-100", "100-1000", "> 1000"))

cat("\nFlows per volume band:\n");        print(table(d$band))
cat("Share aberrant, per band (%):\n");   print(round(tapply(d$density_suspect, d$band, mean) * 100, 1))
cat("Median volume, aberrant vs not:\n"); print(tapply(d$qty, d$density_suspect, median))

# CONCLUSION, in three lines.
# 1. 46 % of the flows under 10 m3 have an impossible density, against 6 to
#    12 % everywhere else. The smallest volumes go down to 0.001 m3.
# 2. That is arithmetic, not fraud: a weight rounded to the kilo divided by a
#    volume rounded to the thousandth of a cubic metre produces anything at all.
# 3. So we KEEP them and flag them. Deleting 13.5 % of the rows would bias any
#    count of flows; a test that rejects correct data is a bad test.

# --- Output ---
write.csv(clean, here("data", "processed", "trade_clean.csv"), row.names = FALSE)
