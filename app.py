import streamlit as st
import pandas as pd

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Inventory Stock-Out Risk Prediction",
    page_icon="📦",
    layout="wide"
)

# -----------------------------
# TITLE
# -----------------------------
st.title("📦 Inventory Stock-Out Risk Prediction")
st.write("Analyze inventory records and identify stock-out risk.")

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("output/predictions.csv")

st.success("Inventory dataset loaded successfully!")

# -----------------------------
# KPI CALCULATIONS
# -----------------------------
total_records = len(df)

critical_stock = (df["Stock_Risk"] == "Critical").sum()

high_risk = (df["Stock_Risk"] == "High").sum()

total_quantity = df["Qty on hand"].sum()

# -----------------------------
# KPI CARDS
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Inventory Records",
        f"{total_records:,}"
    )

with col2:
    st.metric(
        "Critical Stock",
        f"{critical_stock:,}"
    )

with col3:
    st.metric(
        "Total Quantity on Hand",
        f"{total_quantity:,}"
    )

with col4:
    st.metric(
        "High Risk Stock",
        f"{high_risk:,}"
    )

# -----------------------------
# INVENTORY DATA
# -----------------------------
st.subheader("📋 Inventory Data")

# STEP 4 - Key Metrics

st.subheader("📊 Inventory Overview")

col1, col2, col3, col4 = st.columns(4)

total_records = len(df)
critical_stock = (df["Stock_Risk"] == "Critical").sum()
high_risk = (df["Stock_Risk"] == "High").sum()
low_stock = (df["Stock_Risk"] == "Low").sum()

with col1:
    st.metric("Total Records", total_records)

with col2:
    st.metric("Critical Stock", critical_stock)

with col3:
    st.metric("High Risk Stock", high_risk)

with col4:
    st.metric("Low Risk Stock", low_stock)

    # STEP 5 - Stock Risk Distribution

st.subheader("📈 Stock Risk Distribution")

risk_counts = df["Stock_Risk"].value_counts()

st.bar_chart(risk_counts)

st.dataframe(
    df,
    use_container_width=True
)

# STEP 6 - Product Division Analysis

st.subheader("🏷️ Inventory by Product Division")

division_counts = df["Product Division"].value_counts()

st.bar_chart(division_counts)

# STEP 7 - Product Division Filter

st.subheader("🔎 Filter by Product Division")

divisions = df["Product Division"].dropna().unique()

selected_division = st.selectbox(
    "Select Product Division",
    ["All"] + list(divisions)
)

if selected_division != "All":
    filtered_df = df[df["Product Division"] == selected_division]
else:
    filtered_df = df

    # STEP 8 - Supplier Filter

st.subheader("🏭 Filter by Supplier")

suppliers = filtered_df["Supplier"].dropna().unique()

selected_supplier = st.selectbox(
    "Select Supplier",
    ["All"] + list(suppliers)
)

if selected_supplier != "All":
    filtered_df = filtered_df[
        filtered_df["Supplier"] == selected_supplier
    ]

    # STEP 9 - Stock Status Filter

st.subheader("📦 Filter by Stock Status")

stock_statuses = filtered_df["Stock Status"].dropna().unique()

selected_status = st.selectbox(
    "Select Stock Status",
    ["All"] + list(stock_statuses)
)

if selected_status != "All":
    filtered_df = filtered_df[
        filtered_df["Stock Status"] == selected_status
    ]

    # STEP 10 - Stock Risk Filter

st.subheader("⚠️ Filter by Stock Risk")

risk_levels = ["All", "Critical", "High", "Medium", "Low"]

selected_risk = st.selectbox(
    "Select Risk Level",
    risk_levels
)

if selected_risk != "All":
    filtered_df = filtered_df[
        filtered_df["Stock_Risk"] == selected_risk
    ]

    # STEP 11 - Filtered Records

st.subheader("📊 Filtered Inventory")

st.write(
    f"Records after applying filters: **{len(filtered_df):,}**"
)

st.dataframe(
    filtered_df,
    use_container_width=True
)

# STEP 13 - Risk by Product Division

st.subheader("📊 Stock Risk by Product Division")

risk_division = pd.crosstab(
    filtered_df["Product Division"],
    filtered_df["Stock_Risk"]
)

st.bar_chart(risk_division)
# STEP 14 - Top Stores

st.subheader("🏪 Top 10 Stores by Inventory Quantity")

top_stores = (
    filtered_df
    .groupby("Store")["Qty on hand"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_stores)

# STEP 15 - Critical Stock

st.subheader("🚨 Critical Stock Records")

critical_df = filtered_df[
    filtered_df["Stock_Risk"] == "Critical"
]

st.dataframe(
    critical_df,
    use_container_width=True
)

# STEP 16 - High Risk Stock

st.subheader("🔴 High Risk Stock Records")

high_df = filtered_df[
    filtered_df["Stock_Risk"] == "High"
]

st.dataframe(
    high_df,
    use_container_width=True
)

# STEP 17 - Download

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="⬇️ Download Filtered Inventory",
    data=csv,
    file_name="filtered_inventory.csv",
    mime="text/csv"
)
# STEP 18 - Project Explanation

st.subheader("💡 Project Purpose")

st.info(
    "This application analyzes inventory records and identifies "
    "stock-out risk levels such as Critical, High, Medium and Low. "
    "It helps businesses quickly identify where inventory risk exists "
    "and supports better inventory monitoring and decision-making."
)
