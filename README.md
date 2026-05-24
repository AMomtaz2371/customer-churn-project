# Customer Churn Prediction Project
 # Project Overview
 
This project is a Machine Learning web application that predicts whether a customer will stay or leave (churn).  The model is built using customer demographic and service usage data to support business decisions and improve customer retention.

- The system includes:

1-Data preprocessing and cleaning

2-Feature engineering and selection

3-Exploratory Data Analysis (EDA)

4-Model training and evaluation

5-Hyperparameter tuning

6-Web deployment using Streamlit

------------
# Objective

The main goal of this project is to:

Identify customers who are likely to churn (leave the service)
Help businesses improve customer retention strategies
Provide an interactive web app for real-time predictions.

----------
# Dataset

The dataset includes customer information such as:

- Gender

- SeniorCitizen

- Partner / Dependents

- Tenure

- Contract type

- Monthly and Total Charges

- Internet and service features

- Payment method

-------

# Data Preprocessing

The following steps were applied:

- Handling missing values

- Converting data types to numeric

- Encoding categorical variables

- Feature engineering (AvgCharges = TotalCharges / (Tenure + 1))

---------
# Feature Engineering

A new feature was created:


AvgCharges = TotalCharges / (Tenure + 1)


This helps capture average customer spending behavior.

-----------

# Exploratory Data Analysis (EDA)

- The dataset was analyzed using:

Univariate analysis (distribution of features) 

Bivariate analysis (relationship with churn)

- Visualizations such as:

Countplots

Histograms

Heatmaps

- Key insights:

Long-term contracts reduce churn

Higher monthly charges increase churn probability

Tenure strongly affects churn behavior

--------
# Machine Learning Models

Algorithm: Random Forest Classifier
Compared with other models (Logistic Regression, Decision Tree)
Hyperparameter tuning using GridSearchCV
Final model selected based on best performance
✔ The best performing model was Random Forest Classifier.

---------

# Technologies Used
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  
- Joblib

- -----
# Model Optimization
Hyperparameter tuning was performed using GridSearchCV
Best parameters were selected based on performance.

-----
# Evaluation Metrics

The model was evaluated using:

1-Accuracy

2-Precision

3-Recall

Classification Report


✔ The model achieved good performance overall
✔ Better at predicting customers who stay than those who churn due to class imbalance.

------

# Deployment

The model was deployed using Streamlit.

👉 Live App:
https://customer-churn-project-krdkj4gx8ee6pkuxf9kdt9.streamlit.app/

--------

# Project Files
1-app.py → Streamlit web application

2-model.pkl → Trained machine learning model

3-notebook.ipynb → Data analysis and training

4-dataset → Original dataset

5-requirements.txt → Required libraries

-------
# Notes
No separate transformer file was saved because preprocessing was done using pandas encoding techniques.
The model performs better for non-churning customers due to class imbalance in the dataset.
Feature engineering was applied using AvgCharges for better performance.
