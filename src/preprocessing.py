import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("data/application_train.csv")

df.head()

print("=" * 60)
print("Original Shape")
print(df.shape)

# Duplicate rows
duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

# Replace invalid DAYS_EMPLOYED value
df["DAYS_EMPLOYED"] = df["DAYS_EMPLOYED"].replace(365243, np.nan)


# Missing values
missing = df.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)


print("\nTop 20 Missing Columns")
print(missing.head(20))

# Numerical columns
numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns

# Categorical columns
categorical_cols = df.select_dtypes(include=["object"]).columns

print("\nNumber of Numerical Features :", len(numerical_cols))
print("Number of Categorical Features :", len(categorical_cols))

# Save cleaned data
df.to_csv("data/application_train_clean.csv", index=False)

print("\nClean dataset saved successfully!")
print(df.shape)