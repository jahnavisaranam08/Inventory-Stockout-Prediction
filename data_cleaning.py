import pandas as pd
import os

# Project folder location
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Dataset path
file_path = os.path.join(
    BASE_DIR,
    "data",
    "retail_inventory_ml_apl.csv"
)

# Read dataset
inventory = pd.read_csv(file_path)

print("Dataset loaded successfully!")

print("\nFIRST 5 ROWS:")
print(inventory.head())

print("\nDATASET SHAPE:")
print(inventory.shape)

print("\nCOLUMN NAMES:")
print(inventory.columns.tolist())

print("\nMISSING VALUES:")
print(inventory.isnull().sum())

print("\nDUPLICATE ROWS:")
print(inventory.duplicated().sum())

# Remove duplicates
inventory = inventory.drop_duplicates()

# Remove missing values
inventory = inventory.dropna()

# Output folder path
output_path = os.path.join(
    BASE_DIR,
    "output",
    "cleaned_inventory.csv"
)

# Save cleaned data
inventory.to_csv(output_path, index=False)

print("\nDATA CLEANING COMPLETED SUCCESSFULLY!")
print("Saved to:", output_path)