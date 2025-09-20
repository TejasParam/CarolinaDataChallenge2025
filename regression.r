library(dplyr)

# Read standardized data from CSV file
df_std <- read.csv("standardized_data.csv", stringsAsFactors = FALSE)

# Define ranges
row_range <- 6:103
col_range <- 3:14   # regression data

results <- data.frame(Name = character(), Slope = numeric(), stringsAsFactors = FALSE)

for (r in row_range) {
  y <- as.numeric(df_std[r, col_range])
  name <- as.character(df_std[r, 2])   # take name from column 2
  
  # Skip if all NA
  if (all(is.na(y))) {
    next
  }
  
  # Define x as column indices (or years if your headers are years)
  x <- 1:length(y)   # change to: as.numeric(colnames(df_std)[col_range]) if they are years
  
  # Keep only non-NA pairs
  mask <- !is.na(y)
  x <- x[mask]
  y <- y[mask]
  
  if (length(unique(x)) > 1) {
    fit <- lm(y ~ x)
    slope <- coef(fit)[2]
  } else {
    slope <- NA
  }
  
  results <- rbind(results, data.frame(Name = name, Slope = slope))
}

# Sort by slope, highest to lowest
results_sorted <- results %>%
  arrange(desc(Slope))

head(results_sorted)

# Write regression results to file
write.csv(results_sorted, "regression_results.csv", row.names = FALSE)
cat("Regression results written to regression_results.csv\n")

# Also write a summary file with all results (not just head)
write.csv(results_sorted, "regression_results_full.csv", row.names = FALSE)
cat("Full regression results written to regression_results_full.csv\n")
