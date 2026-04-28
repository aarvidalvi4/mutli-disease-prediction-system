import streamlit as st
import numpy as np
import joblib

diabetes_model = joblib.load("diabetes_model.pkl")
diabetes_scaler = joblib.load("scaler.pkl")

heart_model = joblib.load("heart_model.pkl")

cancer_model = joblib.load("cancer_model.pkl")
cancer_scaler = joblib.load("scaler_cancer.pkl")

st.set_page_config(page_title="Multi Disease Predictor", layout="centered")

st.title("🩺 Multi-Disease Prediction System")
st.write("Select a disease and enter patient details")

disease = st.selectbox(
    "Choose Disease",
    ["Diabetes", "Heart Disease", "Breast Cancer"]
)

if disease == "Diabetes":

    st.subheader("Diabetes Prediction")

    pregnancies = st.number_input("Pregnancies", 0, 20)
    glucose = st.number_input("Glucose Level")
    bp = st.number_input("Blood Pressure")
    skin = st.number_input("Skin Thickness")
    insulin = st.number_input("Insulin")
    bmi = st.number_input("BMI")
    dpf = st.number_input("Diabetes Pedigree Function")
    age = st.number_input("Age")

    if st.button("Predict Diabetes"):

        input_data = np.array([[pregnancies, glucose, bp, skin,
                                insulin, bmi, dpf, age]])

        input_scaled = diabetes_scaler.transform(input_data)
        prediction = diabetes_model.predict(input_scaled)

        if prediction[0] == 1:
            st.error("⚠️ High Risk of Diabetes")
        else:
            st.success("✅ Low Risk of Diabetes")

elif disease == "Heart Disease":

    st.subheader("Heart Disease Prediction")

    age = st.number_input("Age")
    sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
    cp = st.selectbox("Chest Pain Type (0-3)", [0,1,2,3])
    trestbps = st.number_input("Resting Blood Pressure")
    chol = st.number_input("Cholesterol")
    fbs = st.selectbox("Fasting Blood Sugar > 120", [0,1])
    restecg = st.selectbox("Rest ECG", [0,1,2])
    thalach = st.number_input("Max Heart Rate")
    exang = st.selectbox("Exercise Induced Angina", [0,1])
    oldpeak = st.number_input("ST Depression")
    slope = st.selectbox("Slope", [0,1,2])
    ca = st.selectbox("Number of Vessels", [0,1,2,3])
    thal = st.selectbox("Thal", [1,2,3])

    if st.button("Predict Heart Disease"):

        input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                                restecg, thalach, exang, oldpeak,
                                slope, ca, thal]])

        prediction = heart_model.predict(input_data)

        if prediction[0] == 1:
            st.error("⚠️ High Risk of Heart Disease")
        else:
            st.success("✅ Low Risk of Heart Disease")

elif disease == "Breast Cancer":

    st.subheader("Breast Cancer Prediction")

    radius = st.number_input("Mean Radius")
    texture = st.number_input("Mean Texture")
    perimeter = st.number_input("Mean Perimeter")
    area = st.number_input("Mean Area")
    smoothness = st.number_input("Mean Smoothness")

    if st.button("Predict Cancer"):

        input_data = np.array([[radius, texture, perimeter, area, smoothness]])

        input_scaled = cancer_scaler.transform(input_data)
        prediction = cancer_model.predict(input_scaled)

        if prediction[0] == 0:
            st.error("⚠️ Malignant (Cancerous)")
        else:
            st.success("✅ Benign (Non-Cancerous)")