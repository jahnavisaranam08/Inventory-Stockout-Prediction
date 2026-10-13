import pandas as pd
import matplotlib.pyplot as plt


# STEP 1: Load cleaned inventory dataset


inventory = pd.read_csv(
    "output/cleaned_inventory.csv"
)

print("Dataset loaded successfully!")



# STEP 2: Basic information


print("\nDataset Shape:")
print(inventory.shape)

print("\nColumn Names:")
print(inventory.columns.tolist())



# STEP 3: Stock Status Analysis


print("\nStock Status Distribution:")
print(inventory["Stock Status"].value_counts())



# STEP 4: Product Division Analysis


print("\nProduct Division:")
print(inventory["Product Division"].value_counts())



# STEP 5: Product Category Analysis


print("\nTop Product Categories:")
print(
    inventory["Product Category"]
    .value_counts()
    .head(10)
)



# STEP 6: Store Analysis


print("\nTop Stores:")
print(
    inventory["Store"]
    .value_counts()
    .head(10)
)



# STEP 7: Supplier Analysis


print("\nTop Suppliers:")
print(
    inventory["Supplier"]
    .value_counts()
    .head(10)
)



# STEP 8: Quantity on Hand


print("\nQuantity on Hand Statistics:")
print(
    inventory["Qty on hand"].describe()
)



# STEP 9: Stock value statistics


print("\nStock Selling Amount Statistics:")
print(
    inventory["Stocks Selling Amount"].describe()
)



# STEP 10: Cost of Stock statistics


print("\nCost of Stocks Statistics:")
print(
    inventory["Cost of Stocks"].describe()
)



# STEP 11: Highest stock products


print("\nProducts with Highest Quantity:")

top_products = (
    inventory
    .groupby("Product Description")["Qty on hand"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)



# STEP 12: Lowest stock products


print("\nProducts with Lowest Quantity:")

low_products = (
    inventory
    .groupby("Product Description")["Qty on hand"]
    .sum()
    .sort_values()
    .head(10)
)

print(low_products)



# STEP 13: Create chart


top_products.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Top 10 Products by Quantity on Hand")
plt.xlabel("Product")
plt.ylabel("Quantity")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()