# ---------------------------------------------------------------
# 01_import.R -- SOLUTION
# Loads the Comtrade extract and produces the France working table.
#
# Input  : data/raw/comtrade_fr_roundwood_clean.csv
# Output : data/processed/trade_france.csv
# ---------------------------------------------------------------

# --- Dependencies ---
library(here)

# --- Parameters ---
COUNTRY <- "France"

# --- Body ---
# here() resolves from the project root: no setwd(), no absolute path.
trade <- read.csv(here("data", "raw", "comtrade_fr_roundwood_clean.csv"))

# partnerDesc == "World" is the all-partners aggregate: keeping it would
# double every total computed downstream.
france <- subset(trade, reporterDesc == COUNTRY & partnerDesc != "World")

# --- Output ---
# Processed data goes to processed/, never next to the raw data.
write.csv(france, here("data", "processed", "trade_france.csv"), row.names = FALSE)

cat("Written:", nrow(france), "rows\n")
