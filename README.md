# Inventory Stock-Out Prediction

## Project Overview
The Inventory Stock-Out Prediction project analyzes retail inventory data and classifies inventory records into stock risk levels using Python and Machine Learning. It helps identify items that may require attention and supports inventory monitoring and decision-making.

## Objectives
- Analyze and clean retail inventory data.
- Perform Exploratory Data Analysis (EDA).
- Classify inventory records by stock risk.
- Build a Machine Learning model.
- Visualize inventory insights using Power BI.
- Develop an interactive dashboard using Streamlit.

## Technologies Used
- Python
- Pandas and NumPy
- Scikit-learn
- Matplotlib
- SQL (Oracle SQL)
- Power BI
- Streamlit

## Stock Risk Classification
The project uses the quantity on hand to assign risk levels:

| Quantity on Hand | Risk Level |
|---|---|
| 0 or less | Critical |
| 1 | High |
| 2 | Medium |
| 3 or more | Low |

## Machine Learning
A Random Forest classifier is used to classify inventory stock risk. The model achieved approximately **62.30% accuracy** in the current evaluation.

*Note: The accuracy is based on the current dataset and evaluation setup; results may vary with different data.*

## Project Structure
- `app.py` — Streamlit dashboard
- `python/` — Data cleaning, EDA, database, model, and prediction scripts
- `sql/` — SQL queries and database scripts
- `powerbi/` — Power BI dashboard
- `requirements.txt` — Python dependencies
- `.gitignore` — Files excluded from Git tracking

## How to Run Locally
1. Install Python.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Install dependencies:

   `pip install -r requirements.txt`

5. Run the Streamlit app:

   `streamlit run app.py`

Make sure the required prediction data files are available at the paths expected by `app.py`.

## Limitations
The current dataset does not include all information needed to estimate an exact future stock-out date, such as daily demand and supplier lead time. The current project focuses on stock risk classification rather than exact stock-out date forecasting.

## Future Enhancements
- Add daily sales and supplier lead-time data.
- Improve model performance through feature engineering and model evaluation.
- Add automated inventory alerts.
- Deploy the Streamlit dashboard online.

## Author
Jahnavi
