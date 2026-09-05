# -----------------------------------------------------------------
# 04 -- Total value of the flows in the dataset
# -----------------------------------------------------------------

trade <- read.csv("data/raw/comtrade_fr_roundwood_dirty.csv", sep = ";")

cat("Total value:", sum(trade$primaryValue, na.rm = TRUE), "USD\n")
