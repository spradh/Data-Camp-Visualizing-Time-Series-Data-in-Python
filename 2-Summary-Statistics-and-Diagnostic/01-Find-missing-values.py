# Display first seven rows of co2_levels
print(co2_levels.head(7))

# Set datestamp column as index
co2_levels = co2_levels.set_index('datestamp')

# Print out the number of missing values
print(co2_levels.isnull().sum())

