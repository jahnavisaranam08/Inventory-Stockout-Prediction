LOAD DATA

INFILE 'C:\Users\saranam Jahnavi\OneDrive\Desktop\jahnavi\Inventory_Stockout_Project\output\predictions.csv'

INTO TABLE inventory

APPEND

FIELDS TERMINATED BY ','

OPTIONALLY ENCLOSED BY '"'

TRAILING NULLCOLS

(
    id SEQUENCE(MAX,1),
    start_date DATE "YYYY-MM-DD",
    end_date DATE "YYYY-MM-DD",
    stock_status CHAR,
    supplier CHAR,
    product_no CHAR,
    product_description CHAR,
    product_division CHAR,
    product_category CHAR,
    product_subcategory CHAR,
    product_segment CHAR,
    store CHAR,
    store_type CHAR,
    sales_channel CHAR,
    qty_on_hand INTEGER EXTERNAL,
    stocks_selling_amount DECIMAL EXTERNAL,
    cost_of_stocks DECIMAL EXTERNAL,
    stock_unit_selling_price DECIMAL EXTERNAL,
    stock_unit_cost_price DECIMAL EXTERNAL,
    stock_risk CHAR,
    risk_score INTEGER EXTERNAL
)