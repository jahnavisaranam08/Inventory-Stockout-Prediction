import pandas as pd
import os


# STEP 1: Load cleaned inventory data


inventory = pd.read_csv(
    "output/cleaned_inventory.csv"
)

print("Cleaned inventory dataset loaded successfully!")



# STEP 2: Create Stock Risk


def classify_stock_risk(qty):
    if qty <= 0:
        return "Critical"
    elif qty == 1:
        return "High"
    elif qty == 2:
        return "Medium"
    else:
        return "Low"


inventory["Stock_Risk"] = inventory["Qty on hand"].apply(
    classify_stock_risk
)



# STEP 3: Check Stock Risk Distribution


print("\nStock Risk Distribution:")

print(
    inventory["Stock_Risk"].value_counts()
)



# STEP 4: Create numeric target


risk_mapping = {
    "Critical": 3,
    "High": 2,
    "Medium": 1,
    "Low": 0
}

inventory["Risk_Score"] = inventory["Stock_Risk"].map(
    risk_mapping
)



# STEP 5: Save processed dataset


output_path = "output/predictions.csv"

inventory.to_csv(
    output_path,
    index=False
)

print("\nStock risk prediction dataset created!")
print("Saved to:", output_path)