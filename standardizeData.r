# Load library
library(readxl)
library(dplyr)

# Read first sheet
df <- read_excel("Business.xlsx", sheet = 2)
df <- as.data.frame(df)

# Define row and column ranges
row_range <- 6:103
col_range <- 3:14   # columns you want standardized

# Copy the data
df_std <- df

# Row-by-row standardization
for (r in row_range) {
  x <- as.numeric(df[r, col_range])
  
  # If all values are NA → skip
  if (all(is.na(x))) {
    next
  }
  
  # If sd is 0 (constant row) → set to 0
  if (sd(x, na.rm = TRUE) == 0) {
    df_std[r, col_range] <- ifelse(is.na(x), NA, 0)
  } else {
    mu <- mean(x, na.rm = TRUE)
    sigma <- sd(x, na.rm = TRUE)
    df_std[r, col_range] <- ifelse(is.na(x), NA, (x - mu) / sigma)
  }
}

# Preview result
print(df_std)

# Write standardized data to file
write.csv(df_std, "standardized_data.csv", row.names = FALSE)
cat("Standardized data written to standardized_data.csv\n")
