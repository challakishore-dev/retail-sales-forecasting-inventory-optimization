# Retail Sales Forecasting & Inventory Optimization System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-brightgreen)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success)

## Overview

An end-to-end retail analytics project that forecasts future product demand and converts predictions into smart inventory decisions such as **Safety Stock**, **Reorder Point (ROP)**, and **Recommended Order Quantity**.

This project demonstrates how data science solves real retail problems like:

* Stockouts causing lost sales
* Overstock causing blocked cash flow
* Poor replenishment planning
* Inaccurate manual forecasting

Designed as a portfolio-grade project for internships, placements, and recruiter review.

---

## Business Problem

Retail businesses need the right stock at the right time.

If inventory is too low:

* Sales are lost
* Customers leave

If inventory is too high:

* Money gets stuck in stock
* Warehousing cost increases

This system uses historical sales data to predict demand and optimize inventory.

---

## Key Features

* Demand forecasting using Machine Learning
* Feature engineering with lag and rolling metrics
* Inventory optimization logic
* Safety Stock calculation
* Reorder Point recommendation
* Streamlit recruiter-ready dashboard
* Interactive Store / Item filters
* KPI cards and charts
* Synthetic retail dataset included
* Modular production-ready code structure

---

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Streamlit
* Joblib
* SciPy

---

## Project Architecture

```text
Historical Sales Data
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Forecast Model
        ↓
Demand Prediction
        ↓
Inventory Logic
        ↓
Dashboard + Reports
```

---

## Folder Structure

```text
Retail-Sales-Forecasting/
│── app/
│   └── dashboard.py
│── data/
│   └── retail_sales.csv
│── src/
│   ├── preprocess.py
│   ├── features.py
│   └── inventory.py
│── models/
│── outputs/
│── main.py
│── requirements.txt
│── README.md
```

---

## Installation

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Project

### Train Model

```bash
python main.py
```

### Launch Dashboard

```bash
streamlit run app/dashboard.py
```

---

## Dashboard Preview

Add your screenshots inside 
<img width="1920" height="1080" alt="Screenshot (79)" src="https://github.com/user-attachments/assets/498a512a-feb4-427f-836c-e42d1c01b45e" />
## Dashboard
<img width="1920" height="1080" alt="Screenshot (80)" src="https://github.com/user-attachments/assets/38d49486-6c8c-428a-9470-93e6ad6dce3c" />
## Sales Trend
<img width="1920" height="1080" alt="Screenshot (81)" src="https://github.com/user-attachments/assets/ecdc05d3-c2ba-4d0e-913b-55948d37d6fa" />
## Monthly sales
<img width="1920" height="1080" alt="Screenshot (82)" src="https://github.com/user-attachments/assets/f79794cc-75db-4b39-bfda-bad4a2319da4" />

## Inventory Recommendation

## Output Generated

After running:

```text
models/model.pkl
outputs/predictions.csv
```

Includes:

* Forecast predictions
* Trained ML model
* Inventory recommendations

---

## Sample Business Metrics

* Total Sales
* Average Daily Demand
* Peak Sales
* Promo Days
* Safety Stock
* Reorder Point
* Order Quantity

---

## Why This Project Matters

Used in real companies such as:

* Amazon
* Walmart
* Flipkart
* Reliance Retail
* D-Mart
* BigBasket

These companies depend on forecasting and replenishment systems daily.

---

## Future Improvements

* XGBoost / LightGBM forecasting
* Multi-store optimization
* Promotion impact modeling
* Real-time APIs
* Power BI dashboard
* Live deployment
* Automated reorder emails
* Demand anomaly detection

---

## Resume Impact

Built a production-ready retail forecasting system using Machine Learning and Streamlit that predicts demand and optimizes inventory decisions using Safety Stock and Reorder Point logic.

---

## Author

Challa Kishore 
Aspiring Data Analyst / Data Scientist

## Recruiter Notes

This project demonstrates:

* Business understanding
* Forecasting knowledge
* Inventory analytics
* Python development
* Dashboarding
* Real-world problem solving

## License

MIT License

