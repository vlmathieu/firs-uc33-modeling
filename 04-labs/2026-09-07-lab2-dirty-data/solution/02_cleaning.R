# ---------------------------------------------------------------
# 02_cleaning.R -- SOLUTION, lab 2 core (steps 3 and 6)
#
# Input  : data/raw/comtrade_fr_roundwood_dirty.csv
# Output : data/processed/trade_clean.csv
#
# This is the brief, and nothing more. The density work and the
# investigation behind it are in 02_cleaning_challenges.R.
# ---------------------------------------------------------------

# --- Dependencies ---
library(here)

# --- Load ---
# sep, dec and fileEncoding must be DECLARED. Without them read.csv fails on
# "more columns than column names": the assumed separator is the comma, which
# also appears inside the cmdDesc labels.
trade <- read.csv(here("data", "raw", "comtrade_fr_roundwood_dirty.csv"),
                  sep = ";", dec = ",", fileEncoding = "latin1")

stopifnot(nrow(trade) == 674, ncol(trade) == 13)

# --- Clean: five decisions, each with its reason ---

# a) World is the all-partners aggregate, sitting in the table next to the
#    partners it is the total of. Keeping it doubles every total.
#    Filter on the CODE, not the label: a label gets translated and renamed,
#    a reserved code does not.
clean <- subset(trade, partnerISO != "W00")

# b) The 17 rows with qty == 0 are KEPT. They are real flows with an
#    unreported quantity, and nothing in this script divides by qty, so
#    there is no Inf to produce. The decision belongs to whoever divides:
#    see 02_cleaning_challenges.R, which does, and excludes them there.
cat("qty == 0 rows kept:", sum(trade$qty == 0, na.rm = TRUE), "\n")

# c) The 11 missing netWgt are KEPT, for the same reason: no computation
#    here uses the net weight. Deleting a row costs information; leaving a
#    missing value costs nothing until something tries to average it.
cat("missing netWgt kept:", sum(is.na(trade$netWgt)), "\n")

# d) aggrLevel equals 6 on all 674 rows. A constant column allows no filter,
#    no grouping and no statistic, and left in place it invites a group_by
#    that groups nothing.
clean$aggrLevel <- NULL

# e) The types. str() before trusting anything: qty, netWgt and primaryValue
#    are the columns at risk, because their decimal mark is a comma. Declared
#    at load time they are numeric; undeclared they arrive as character and
#    nothing says so. period is already an integer here -- checked, not assumed.
stopifnot(is.numeric(clean$primaryValue), is.numeric(clean$qty),
          is.numeric(clean$netWgt), is.integer(clean$period))

# --- Check ---
# The trap of the lab, turned into a line that fails rather than lies.
fr <- subset(clean, reporterDesc == "France")
cat("Rows kept    :", nrow(clean), "out of", nrow(trade), "\n")
cat("France total :", round(sum(fr$primaryValue) / 1e6, 1), "M$ (expected 778.5)\n")
stopifnot(abs(sum(fr$primaryValue) / 1e6 - 778.5) < 0.1)

# --- Output ---
write.csv(clean, here("data", "processed", "trade_clean.csv"), row.names = FALSE)
