# Print out summary statistics of the co2_levels DataFrame
print(co2_levels.describe())

# Print out the minima of the co2 column in the co2_levels DataFrame
print(co2_levels.describe().loc['min'])

# Print out the maxima of the co2 column in the co2_levels DataFrame
print(co2_levels.describe().loc['max'])
