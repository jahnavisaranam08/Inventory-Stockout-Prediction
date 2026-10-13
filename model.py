import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt



# STEP 1: Load prediction dataset


print("Loading dataset...")

data = pd.read_csv(
    "output/predictions.csv"
)

print("Dataset loaded successfully!")
print("Dataset shape:", data.shape)



# STEP 2: Select input features


features = [
    "Supplier",
    "Product Division",
    "Product Category",
    "Product Subcategory",
    "Product Segment",
    "Store",
    "Store Type",
    "Sales Channel",
    "Stock Unit Selling Price",
    "Stock Unit Cost Price"
]



# STEP 3: Define X and y


X = data[features]

y = data["Stock_Risk"]


print("\nFeatures selected:")
print(features)

print("\nTarget:")
print("Stock_Risk")



# STEP 4: Identify categorical and numerical columns


categorical_features = [
    "Supplier",
    "Product Division",
    "Product Category",
    "Product Subcategory",
    "Product Segment",
    "Store",
    "Store Type",
    "Sales Channel"
]

numerical_features = [
    "Stock Unit Selling Price",
    "Stock Unit Cost Price"
]



# STEP 5: Encode categorical columns


preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(
                handle_unknown="ignore"
            ),
            categorical_features
        )
    ],
    remainder="passthrough"
)



# STEP 6: Create Random Forest model


model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced"
)



# STEP 7: Create ML Pipeline


pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)



# STEP 8: Train/Test Split


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))



# STEP 9: Train the model


print("\nTraining Random Forest model...")

pipeline.fit(
    X_train,
    y_train
)

print("Model training completed!")



# STEP 10: Make predictions


y_pred = pipeline.predict(X_test)



# STEP 11: Calculate accuracy


accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nModel Accuracy:")
print(f"{accuracy:.4f}")

print(
    f"Accuracy Percentage: {accuracy * 100:.2f}%"
)



# STEP 12: Classification Report


print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred
    )
)



# STEP 13: Save test predictions


results = X_test.copy()

results["Actual_Risk"] = y_test.values

results["Predicted_Risk"] = y_pred

results.to_csv(
    "output/ml_predictions.csv",
    index=False
)

print("\nML predictions saved successfully!")

print(
    "File: output/ml_predictions.csv"
)


# STEP 14: Confusion Matrix


print("\nCreating Confusion Matrix...")

cm = confusion_matrix(
    y_test,
    y_pred,
    labels=["Critical", "High", "Medium", "Low"]
)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Critical", "High", "Medium", "Low"]
)

disp.plot()

plt.title("Stock Risk Prediction - Confusion Matrix")

plt.tight_layout()

plt.savefig(
    "output/confusion_matrix.png"
)

plt.show()

print("Confusion Matrix saved successfully!")


# --------------------------------------------------
# STEP 15: Feature Importance
# --------------------------------------------------

print("\nCalculating Feature Importance...")

# Get transformed feature names
feature_names = pipeline.named_steps[
    "preprocessor"
].get_feature_names_out()

# Get Random Forest model
rf_model = pipeline.named_steps[
    "model"
]

# Get importance values
importance_values = rf_model.feature_importances_


# Create feature importance dataframe
importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importance_values
})


# Sort by importance
importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)


print("\nTop 20 Important Features:")

print(
    importance_df.head(20)
)



# STEP 16: Save Feature Importance


importance_df.to_csv(
    "output/feature_importance.csv",
    index=False
)

print("\nFeature importance saved successfully!")



# STEP 17: Plot Top 15 Features


top_features = importance_df.head(15)

plt.figure(figsize=(10, 7))

plt.barh(
    top_features["Feature"][::-1],
    top_features["Importance"][::-1]
)

plt.xlabel("Importance")

plt.ylabel("Feature")

plt.title(
    "Top 15 Features Influencing Stock Risk"
)

plt.tight_layout()

plt.savefig(
    "output/feature_importance.png"
)

plt.show()

print("Feature importance chart saved successfully!")