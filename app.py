
import streamlit as st
import pandas as pd
import joblib
import streamlit as st

st.title("App is working ✅")
st.write("Hello from Streamlit")



# Load model
model = joblib.load("model.pkl")

# App title
st.title("Customer Churn Prediction")

# Inputs
customerID = st.number_input("Customer ID", min_value=0)

gender = st.selectbox("Gender (0 = Female, 1 = Male)", [0, 1])

senior = st.selectbox("Senior Citizen", [0, 1])

partner = st.selectbox("Partner", [0, 1])

dependents = st.selectbox("Dependents", [0, 1])

tenure = st.number_input("Tenure", min_value=0)

phone = st.selectbox("Phone Service", [0, 1])

multiple = st.selectbox("Multiple Lines", [0, 1])

internet = st.selectbox("Internet Service", [0, 1, 2])

security = st.selectbox("Online Security", [0, 1])

backup = st.selectbox("Online Backup", [0, 1])

device = st.selectbox("Device Protection", [0, 1])

tech = st.selectbox("Tech Support", [0, 1])

tv = st.selectbox("Streaming TV", [0, 1])

movies = st.selectbox("Streaming Movies", [0, 1])

contract = st.selectbox("Contract", [0, 1, 2])

paperless = st.selectbox("Paperless Billing", [0, 1])

payment = st.selectbox("Payment Method", [0, 1, 2, 3])

monthly = st.number_input("Monthly Charges", min_value=0.0)

total = st.number_input("Total Charges", min_value=0.0)


# Prediction
if st.button("Predict"):

    data = pd.DataFrame([[
        customerID,
        gender,
        senior,
        partner,
        dependents,
        tenure,
        phone,
        multiple,
        internet,
        security,
        backup,
        device,
        tech,
        tv,
        movies,
        contract,
        paperless,
        payment,
        monthly,
        total,
    ]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk: Customer will leave ❌")
    else:
        st.success("⚠️ Low Risk: Customer will stay ✅")
        