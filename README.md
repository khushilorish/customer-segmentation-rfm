# Customer Segmentation using RFM Analysis and K-Means Clustering

## Overview
This project performs customer segmentation using **RFM (Recency, Frequency, Monetary)** analysis and **K-Means Clustering**. The goal is to group customers with similar purchasing behavior so businesses can create targeted marketing strategies, improve customer retention, and maximize revenue.

---

## Problem Statement
Businesses often have thousands of customers with different purchasing patterns. Treating every customer the same leads to ineffective marketing.

This project segments customers into meaningful groups based on their purchasing behavior using RFM analysis and K-Means clustering.

---

## Dataset
- **Dataset:** Online Retail Dataset
- **Rows:** 5,881 customers (after RFM feature engineering)
- **Features:**
  - Customer ID
  - Recency
  - Frequency
  - Monetary

---

## Project Workflow

1. Data Cleaning
   - Removed missing Customer IDs
   - Removed duplicate records
   - Removed cancelled transactions
   - Removed invalid quantities and prices
   - Converted InvoiceDate to datetime format

2. Feature Engineering
   - Created RFM (Recency, Frequency, Monetary) features
   - Generated one row per customer

3. Exploratory Data Analysis
   - Distribution plots
   - Boxplots
   - Missing value analysis
   - Duplicate analysis

4. Data Preprocessing
   - Log Transformation
   - Standard Scaling

5. Model Building
   - K-Means Clustering

6. Cluster Evaluation
   - Elbow Method
   ![Elbow Method](Elbow%20Method.png)
   - Silhouette Score
   ![Silhouette Method](Silhouette%20Score.png)

7. Cluster Profiling
   - Average RFM values
   - Customer distribution
   - Business interpretation

8. Customer Segmentation
   - VIP Customers
   - Active Customers
   - At Risk Customers
   - Lost Customers

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

---

## Results

The customers were successfully segmented into four meaningful business groups:

| Customer Segment | Description |
|------------------|-------------|
| VIP Customers | High-value customers with frequent purchases and high spending. |
| Active Customers | Recently active customers with moderate purchasing behavior. |
| At Risk Customers | Customers showing reduced activity who may leave soon. |
| Lost Customers | Customers who have not purchased for a long time and have low engagement. |

---

## Business Recommendations

| Segment | Recommendation |
|---------|----------------|
| VIP Customers | Loyalty rewards and premium offers |
| Active Customers | Cross-sell and upsell campaigns |
| At Risk Customers | Retention campaigns and personalized discounts |
| Lost Customers | Win-back emails and special offers |

---

## Repository Structure

```
customer-segmentation-rfm/
│
├── customer_segmentation.ipynb
├── preprocessing.py
├── feature_engineering.py
├── requirements.txt
├── README.md
└── dataset/
```

