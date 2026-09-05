# -----------------------------------------------------------------
# 01 -- How many rows does the dataset contain?
# -----------------------------------------------------------------

trade <- read.csv("/Users/valentin/Documents/uc33/data/raw/comtrade_fr_roundwood_clean.csv")

cat("Rows:", nrow(trade), "\n")
