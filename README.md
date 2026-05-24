# Customer Churn Prediction Project

(1) #📌 Overview
This project is a Machine Learning web application that predicts whether a customer will stay or leave (churn).  
The model is built using customer demographic and service usage data to support business decisions and improve customer retention.

---

# Objective
To help companies identify customers who are likely to churn so that proactive actions can be taken to retain them.

---

# Dataset
The dataset includes customer information such as:
- Gender  
- SeniorCitizen  
- Tenure  
- Contract type  
- Monthly and Total charges  
- Internet and service features  

---

#  Machine Learning Model
- Algorithm: Random Forest Classifier  
- The model was trained on preprocessed data after encoding categorical features.  
- The trained model was saved using Joblib for deployment.

---

# Technologies Used
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  
- Joblib  

---

# How to Run the Project

# 1. Install dependencies:
pip install -r requirements.txt

##2. Run the application:
streamlit run app.py

📁 Project Files
app.py → Streamlit web application
model.pkl → Trained machine learning model
notebook.ipynb → Data analysis and model training
dataset → Original dataset
📈 Output

The model predicts:

Customer will stay ✅
Customer will churn ❌
⚠️ Notes
No separate transformer file was saved because preprocessing was done using pandas get_dummies.
The model performs better for non-churning customers due to class imbalance in the dataset.
