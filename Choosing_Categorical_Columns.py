import pandas as pd

# Load the dataset
df = pd.read_csv("titanic.csv")

# Select the categorical features
categorical_features = df.select_dtypes(include=['object'])

# Display first 5 rows of categorical data
pd.set_option('display.max_columns', None)
print("Selected Categorical Data (first 5 rows):")
print(categorical_features.head())