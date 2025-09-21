# Load required libraries
library(readr)
library(dplyr)
library(ggplot2)
library(tidyr)

# Read the data files
regression_results <- read_csv("regression_results.csv", show_col_types = FALSE)
standardized_data <- read_csv("standardized_data.csv", show_col_types = FALSE)

# Clean and prepare standardized data
# Skip header rows and get the data starting from row 7
std_data_clean <- standardized_data[7:nrow(standardized_data), ]

# Set proper column names
colnames(std_data_clean) <- c("Row", "Industry", "2012", "2013", "2014", "2015", 
                              "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023")

# Remove the row number column and convert to long format
std_data_long <- std_data_clean %>%
  select(-Row) %>%
  filter(!is.na(Industry) & Industry != "…") %>%
  pivot_longer(cols = -Industry, names_to = "Year", values_to = "Standardized") %>%
  mutate(
    Year = as.numeric(Year),
    Standardized = as.numeric(Standardized)
  ) %>%
  filter(!is.na(Standardized) & Standardized != "…")

# Get top 5 industries by slope from regression results
top5_industries <- regression_results %>%
  arrange(desc(Slope)) %>%
  slice_head(n = 5)

print("Top 5 industries by regression slope:")
print(top5_industries)

# Filter standardized data for top 5 industries
std_data_top5 <- std_data_long %>%
  filter(Industry %in% top5_industries$Name)

# Create years for regression lines (2012-2025)
years_extended <- 2012:2025

# Create regression line data
regression_lines <- top5_industries %>%
  crossing(Year = years_extended) %>%
  mutate(
    Predicted = Slope * Year + Intercept
  )

# Create the plot
p <- ggplot() +
  # Add regression lines
  geom_line(data = regression_lines, 
            aes(x = Year, y = Predicted, color = Name), 
            size = 1.2, alpha = 0.8) +
  # Add data points from standardized data
  geom_point(data = std_data_top5, 
             aes(x = Year, y = Standardized, color = Industry), 
             size = 3, alpha = 0.7) +
  # Styling
  theme_minimal(base_size = 13) +
  scale_x_continuous(breaks = seq(2012, 2025, 2), limits = c(2012, 2025)) +
  scale_color_viridis_d(name = "Industry", option = "plasma") +
  labs(
    title = "Top 5 Industries: Regression Lines vs Standardized Data Points",
    subtitle = "Regression lines projected from 2012-2025, data points from standardized data",
    x = "Year",
    y = "Standardized Value",
    color = "Industry"
  ) +
  theme(
    panel.background = element_rect(fill = "white", color = NA),
    plot.background = element_rect(fill = "white", color = NA),
    legend.background = element_rect(fill = "white", color = NA),
    legend.position = "bottom",
    legend.text = element_text(size = 8),
    plot.title = element_text(size = 16, face = "bold"),
    plot.subtitle = element_text(size = 12)
  ) +
  guides(color = guide_legend(nrow = 3, byrow = TRUE))

# Display the plot
print(p)

# Save the plot
ggsave("top5_regression_vs_data.png", p, width = 12, height = 8, dpi = 300)

print("Plot saved as 'top5_regression_vs_data.png'")

# Display summary statistics
cat("\nSummary of Top 5 Industries:\n")
for(i in 1:nrow(top5_industries)) {
  cat(sprintf("%d. %s (Slope: %.4f)\n", i, top5_industries$Name[i], top5_industries$Slope[i]))
}