# ---------------------------------------------------------------
# 03_figure.R -- SOLUTION, lab 2 step 7
#
# Input  : data/processed/trade_clean.csv   (produced by 02_cleaning.R)
# Output : output/figures/oak_destinations.png
#
# This is the script you were given, unchanged. What follows is why
# each choice was made, which is the part you were asked to work out.
# ---------------------------------------------------------------

# --- Dependencies ---
library(here)
library(ggplot2)

# --- Parameters ---
# Named constants rather than numbers buried in the code: when the HS code
# changes, it changes in one place, and the change is visible in a diff.
OAK   <- 440391    # HS code: oak logs
N_TOP <- 5         # destinations shown by name; the rest become "Other"

# --- Load ---
# The output of the previous script, not the raw file. That is what makes
# this a separate stage: re-running it costs nothing, and it can be handed
# to someone who never reads 02_cleaning.
clean <- read.csv(here("data", "processed", "trade_clean.csv"))

# --- 1. Filter ---
oak <- subset(clean, cmdCode == OAK &                  # oak logs only
                     reporterDesc == "France" &        # declared by France
                     flowDesc == "Export")             # outgoing flows

# --- 2. Aggregate ---
# One value per (year, destination). Read the formula as: sum primaryValue,
# for each combination of period and partnerDesc.
by_country <- aggregate(primaryValue ~ period + partnerDesc, data = oak, FUN = sum)

# Rank destinations over the whole period, not year by year: a country that
# is fourth every year should not disappear because it is never first.
totals <- aggregate(primaryValue ~ partnerDesc, data = by_country, FUN = sum)
totals <- totals[order(-totals$primaryValue), ]
top    <- head(totals$partnerDesc, N_TOP)

# Everything outside the top five becomes "Other". Without this the legend
# has sixty entries, the palette recycles colours, and the figure says
# nothing. Re-aggregating afterwards is what makes the Others add up.
by_country$destination <- ifelse(by_country$partnerDesc %in% top,
                                 by_country$partnerDesc, "Other")
graph <- aggregate(primaryValue ~ period + destination, data = by_country, FUN = sum)

# A factor fixes the legend order. Left as text, ggplot2 sorts alphabetically
# and "Other" lands in the middle of the ranking, which reads as a country.
graph$destination <- factor(graph$destination, levels = c(top, "Other"))

# --- 3. Plot ---
# Stacked bars rather than lines: three years make three points, and six
# series on three points is a worse figure than three bars. A stacked bar
# carries the total and its composition in the same object.
ggplot(graph, aes(x = factor(period),              # one bar per year
                  y = primaryValue / 1e6,          # height, in millions
                  fill = destination)) +           # the split inside the bar
  geom_col() +
  labs(title = "French oak log exports (HS 440391)",
       x = NULL, y = "million USD", fill = "Destination")

# --- Output ---
# Into output/figures/, which is regenerable and deletable. Nothing of value
# lives there: if this file is lost, this script rebuilds it.
ggsave(here("output", "figures", "oak_destinations.png"),
       width = 9, height = 5, dpi = 150)

cat("Figure written. Top destination:", as.character(totals$partnerDesc[1]),
    paste0("(", round(totals$primaryValue[1] / 1e6, 1), " M$ over three years)\n"))
