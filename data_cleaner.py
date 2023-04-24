import pandas as pd

# Read in the original CSV file
df = pd.read_csv('temperature.csv')

# Drop any rows containing 'NA' values
df.dropna(inplace=True)

# Write the cleaned data to a new CSV file
df.to_csv('cleaned_data.csv', index=False)
