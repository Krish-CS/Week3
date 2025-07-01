# 🌊 Final Project – Water Quality Prediction (Polished & App-Enabled Version)

This final version of the **Water Quality Prediction** project demonstrates a complete machine learning pipeline: from data preprocessing and multi-target regression to visualizations and an interactive web app using Streamlit. This project was developed as part of the **AICTE Virtual Internship** sponsored by **Shell**, conducted by **Edunet Foundation** in **June 2025**.

---

## 🎯 Objective

To build a scalable and user-friendly predictive model that estimates key water pollutant levels for a selected monitoring station and year, and makes the results accessible through a Streamlit-based web application.

---

## ✅ Key Features

* Predicts six major water pollutants using Random Forest Regression
* Uses `MultiOutputRegressor` to handle multiple pollutant targets simultaneously
* Includes an interactive web app (`app.py`) for real-time predictions
* Generates visualizations: correlation heatmap and actual vs. predicted plots
* Modular code with reusable prediction function: `predict_pollutants(station_id, year)`

---

## 📈 Predicted Water Quality Parameters

* Oxygen (O₂)
* Nitrate (NO₃)
* Nitrite (NO₂)
* Sulphate (SO₄)
* Phosphate (PO₄)
* Chloride (CL)

---

## 💻 Streamlit Web App

The project includes a web app that allows users to input a **station ID** and **year**, and receive predicted pollutant levels in both tabular and visual form.

### ▶️ To Run the App:

```bash
streamlit run app.py
```

---

## 📁 Project Files

* `Water_Quality_Prediction.ipynb` – Final machine learning notebook
* `app.py` – Streamlit web application script
* `pollution_model.pkl` – Trained ML model file
* `model_columns.pkl` – Encoded column structure
* `Water_Quality_Prediction_Dataset.csv` – Cleaned dataset
* `requirements.txt` – List of Python packages
* `README.md` – Project documentation

---

## 🛠️ Technologies Used

* Python 3.12
* Pandas, NumPy – Data handling and preprocessing
* Scikit-learn – Machine learning model
* Matplotlib, Seaborn – Data visualization
* Joblib – Model saving/loading
* Streamlit – Web application interface
* Jupyter Notebook – Development environment

---

## 📊 Model Evaluation Metrics

* R² Score – Measures how well the model explains the variance in data
* Mean Squared Error (MSE) – Quantifies prediction accuracy

---

## 📅 Internship Details

This project was developed under the following internship program:

* AICTE Virtual Internship
* Conducted by Edunet Foundation
* Sponsored by Shell
* Duration: June 2025
* Week: Week 3 (Final Project Submission)
* Focus Area: Artificial Intelligence in Environmental Monitoring

---
