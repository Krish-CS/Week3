import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt

# Load model and column structure
model = joblib.load("pollution_model.pkl")
model_columns = joblib.load("model_columns.pkl")

# Define pollutants
pollutants = ['O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']

# App title
st.title("💧 Water Quality Prediction App")
st.subheader("AICTE Virtual Internship – Shell & Edunet (June 2025)")

st.markdown("""
This app predicts six major water quality pollutant levels based on a selected **Station ID** and **Year**.
""")

# Sidebar Inputs
st.sidebar.header("📥 Input Parameters")
station_id = st.sidebar.number_input("Station ID (1–22)", min_value=1, max_value=22, value=22)
year_input = st.sidebar.number_input("Year", min_value=2000, max_value=2030, value=2024)

# Predict function
def predict_pollutants(station_id, year_input):
    input_data = pd.DataFrame({'year': [year_input], 'id': [station_id]})
    input_encoded = pd.get_dummies(input_data, columns=['id'])

    for col in model_columns:
        if col not in input_encoded.columns:
            input_encoded[col] = 0

    input_encoded = input_encoded[model_columns]
    result = model.predict(input_encoded)[0]
    return dict(zip(pollutants, result))

# Predict button
if st.button("🔮 Predict Pollutant Levels"):
    prediction = predict_pollutants(station_id, year_input)

    # Display result
    st.success(f"Predicted Pollutant Levels for Station {station_id} in {year_input}:")
    result_df = pd.DataFrame(prediction.items(), columns=["Pollutant", "Predicted Value"])
    result_df["Predicted Value"] = result_df["Predicted Value"].round(2)
    st.table(result_df)

    # Bar chart
    st.bar_chart(result_df.set_index("Pollutant"))
