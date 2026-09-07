# 01 -- SOLUTION: path relative to the project root, not an absolute path.
library(here)
trade <- read.csv(here("data", "raw", "comtrade_fr_roundwood_clean.csv"))
cat("Rows:", nrow(trade), "\n")
