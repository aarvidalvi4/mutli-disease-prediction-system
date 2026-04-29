# 🩺 Multi-Disease Prediction System (ML + Streamlit)

## 📌 Overview
The Multi-Disease Prediction System is a machine learning-based web application that predicts the risk of multiple diseases using patient health data.

It supports prediction for:
- Diabetes  
- Heart Disease  
- Breast Cancer  

This project demonstrates a complete ML pipeline from data preprocessing and model training to deployment using Streamlit.

---

## 🎯 Objective
To build an end-to-end machine learning system that:
- Takes medical inputs from users  
- Processes data using trained models  
- Predicts disease risk (High / Low)  
- Displays results in a simple web interface  

---

## ⚙️ Features
- Multi-disease prediction in one app (diabetes, heart disease, breast cancer)
- Real-time user input using Streamlit  
- Machine learning-based classification models  
- Clean and interactive UI  
- Pre-trained models saved using Joblib  
- Scalable structure to add more diseases  

---

## 🧠 Machine Learning Models Used
- Random Forest Classifier  
- Logistic Regression (for experimentation)  
- StandardScaler for preprocessing  

---

## 📊 Datasets Used
- Pima Indians Diabetes Dataset  
- UCI Heart Disease Dataset  
- Wisconsin Breast Cancer Dataset  

---

## 🛠️ Tech Stack
- Python  
- NumPy, Pandas  
- Scikit-learn  
- Streamlit  
- Joblib  

---

## 📂 Project Structure
```
multi-disease-app/
│
├── app.py
├── heart_model.pkl
├── diabetes_model.pkl
├── cancer_model.pkl
├── scaler.pkl
├── scaler_cancer.pkl
│
├── Heart disease prediction.ipynb
├── Diabetes Prediction.ipynb
├── breast cancer.ipynb
│
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the app
```bash
streamlit run app.py
```

---

## 🧪 How It Works
1. User selects a disease  
2. Enters medical parameters  
3. Data is processed using trained models  
4. Model predicts risk level  
5. Output is displayed as:
   - ⚠️ High Risk  
   - ✅ Low Risk  

---

## 🧠 Key Learnings
- Data preprocessing and feature scaling  
- Training classification models  
- Evaluating model performance  
- Saving/loading models using Joblib  
- Building ML web apps using Streamlit  

---

## ⚠️ Limitations
- Model accuracy depends on dataset quality  
- Some overlap exists in medical data  
- Not suitable for real medical diagnosis  

---

## 🔮 Future Improvements
- Add more diseases (kidney, liver, etc.)  
- Add probability-based predictions  
- Improve accuracy using advanced models  
- Deploy online (Streamlit Cloud)  
- Add explainability (feature importance / SHAP)  

---

## 👨‍💻 Author
Aarvi Amol Dalvi
BSc Artificial Intelligence Student  
Interested in Machine Learning & Healthcare AI  

---

## 📌 Disclaimer
This project is for educational purposes only and should not be used for medical diagnosis.
