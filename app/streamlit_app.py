import streamlit as st
import pickle
import numpy as np
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "loan_model.pkl")


if not os.path.exists(model_path):
    st.error(" Model file not found!")
    st.write("Expected path:", model_path)
    st.stop()


model = pickle.load(open(model_path, "rb"))


st.title("🏦 Bank Loan Prediction System")

st.write("Enter customer details:")


gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])

applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Term", min_value=0)

credit_history = st.selectbox("Credit History", ["Good", "Bad"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])


gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
dependents = {"0": 0, "1": 1, "2": 2, "3+": 3}[dependents]
education = 0 if education == "Graduate" else 1
self_employed = 1 if self_employed == "Yes" else 0
credit_history = 1 if credit_history == "Good" else 0
property_area = {"Urban": 2, "Semiurban": 1, "Rural": 0}[property_area]


if st.button("Predict Loan Status"):

    data = np.array([[gender, married, dependents, education,
                      self_employed, applicant_income, coapplicant_income,
                      loan_amount, loan_term, credit_history, property_area]])

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    if prediction == 1:
        st.success(f" Loan Approved (Probability: {round(probability*100, 2)}%)")
    else:
        st.error(f" Loan Rejected (Probability: {round(probability*100, 2)}%)")