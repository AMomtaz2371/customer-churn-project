import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

st.title("Customer Churn Prediction")

st.write("Enter values as numbers (0/1 where applicable)")

# Inputs (ALL numeric to match training after get_dummies)
gender = st.number_input("Gender (0 = Female, 1 = Male)", min_value=0, max_value=1)

SeniorCitizen = st.number_input("Senior Citizen (0 or 1)", min_value=0, max_value=1)

Partner = st.number_input("Partner (0 = No, 1 = Yes)", min_value=0, max_value=1)

Dependents = st.number_input("Dependents (0 = No, 1 = Yes)", min_value=0, max_value=1)

tenure = st.number_input("Tenure", min_value=0)

PhoneService = st.number_input("Phone Service (0 = No, 1 = Yes)", min_value=0, max_value=1)

MultipleLines = st.number_input("Multiple Lines (0 or 1)", min_value=0, max_value=1)

InternetService = st.number_input("Internet Service (0/1/2 encoded)", min_value=0)

OnlineSecurity = st.number_input("Online Security (0 or 1)", min_value=0, max_value=1)

OnlineBackup = st.number_input("Online Backup (0 or 1)", min_value=0, max_value=1)

DeviceProtection = st.number_input("Device Protection (0 or 1)", min_value=0, max_value=1)

TechSupport = st.number_input("Tech Support (0 or 1)", min_value=0, max_value=1)

StreamingTV = st.number_input("Streaming TV (0 or 1)", min_value=0, max_value=1)

StreamingMovies = st.number_input("Streaming Movies (0 or 1)", min_value=0, max_value=1)

Contract = st.number_input("Contract (encoded 0/1/2)", min_value=0)

PaperlessBilling = st.number_input("Paperless Billing (0 or 1)", min_value=0, max_value=1)

PaymentMethod = st.number_input("Payment Method (encoded number)", min_value=0)

MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0)

TotalCharges = st.number_input("Total Charges", min_value=0.0)

AvgCharges = st.number_input("Average Charges", min_value=0.0)

# Prediction
if st.button("Predict"):

    data = np.array([[
        gender, SeniorCitizen, Partner, Dependents,
        tenure, PhoneService, MultipleLines, InternetService,
        OnlineSecurity, OnlineBackup, DeviceProtection,
        TechSupport, StreamingTV, StreamingMovies,
        Contract, PaperlessBilling, PaymentMethod,
        MonthlyCharges, TotalCharges, AvgCharges
    ]])

    pred = model.predict(data)

    if pred[0] == 1:
        st.error("Customer will churn ❌")
    else:
        st.success("Customer will stay ✅")