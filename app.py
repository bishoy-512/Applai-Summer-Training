import streamlit as st
import pandas as pd
import joblib

# Load model & features
model = joblib.load("loan_model.pkl")
features = joblib.load("features.pkl")

st.set_page_config(page_title="Loan Completion Predictor", layout="centered")
st.title("💳 Loan Completion Status Prediction")
st.write("Enter loan details to predict completion status")

# Collect user input
user_input = {}
for feature in features:
    user_input[feature] = st.number_input(feature, value=0.0)

# Predict
if st.button("Predict"):
    input_df = pd.DataFrame([user_input])
    prediction = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]

    status_map = {
        0: "Paid off with renewal",
        1: "Paid in full",
        2: "Default",
        3: "Paid via discounted payoff"
    }

    st.success(f"Prediction: **{status_map[prediction]}**")

    st.subheader("Prediction Probabilities")
    prob_df = pd.DataFrame({
        "Status": status_map.values(),
        "Probability": probabilities
    })
    st.bar_chart(prob_df.set_index("Status"))
