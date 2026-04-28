🩺 Multi-Disease Prediction System (ML + Streamlit)
📌 Overview

The Multi-Disease Prediction System is a machine learning web application that predicts the risk of multiple diseases based on patient health parameters.

This system is designed to simulate real-world healthcare AI applications by combining data science, machine learning, and web deployment into a single interactive platform.

It supports prediction for:

--> Diabetes
--> Heart Disease
--> Breast Cancer

The goal of this project is to demonstrate how machine learning models can be used in healthcare to assist early disease risk detection.

🎯 Objective

To build an end-to-end machine learning system that:

Takes patient health data as input
Processes and transforms data appropriately
Applies trained ML models for prediction
Outputs interpretable risk results (High / Low risk)
⚙️ Features
🧠 Multi-disease prediction in a single application
⚡ Real-time user input handling via Streamlit UI
📊 Machine learning-based classification models
🔍 Probability-based or class-based risk output
🎨 Clean and interactive web interface
💾 Pre-trained models saved using Joblib
🔄 Scalable structure for adding more diseases
🧠 Machine Learning Models Used
Disease	Model
Diabetes	Random Forest / Logistic Regression
Heart Disease	Random Forest Classifier
Breast Cancer	Random Forest Classifier


Dataset Information
The models were trained using publicly available datasets:

Diabetes Dataset (Pima Indians Diabetes Dataset)
Heart Disease Dataset (UCI ML Repository)
Breast Cancer Dataset (Wisconsin Diagnostic Dataset)

Each dataset contains structured medical attributes such as:

Age
Blood pressure
Cholesterol levels
Glucose levels
Tumor measurements (for cancer dataset)

Tech Stack:
Python 
NumPy & Pandas 
Scikit-learn 
Streamlit
Joblib 
