# 🎓 Student Placement Predictor

A Machine Learning project that predicts whether a student will be placed or not based on academic performance and skills.

---

## 🌐 Live Demo

👉 https://eakuwglmeg8kwqze2fj6it.streamlit.app/

---

## ✅ Project Checklist (Requirement)

### 🎯 Problem Statement
To develop a classification model that predicts whether a student will get placed based on academic and skill-based features.

---

### 📊 Dataset
Used the Placement Prediction Dataset (Ruchika Kumbhar) containing 10,000 student records.
https://www.kaggle.com/datasets/ruchikakumbhar/placement-prediction-dataset

#### 📌 Features:
- CGPA  
- Internships  
- Projects
- Workshops/Certifications  
- Aptitude Test Score  
- Soft Skills Rating  
- SSC Marks  
- HSC Marks  

#### 🎯 Target:
- PlacementStatus (Placed / Not Placed)

---

### 🤖 Algorithm Used
- Logistic Regression (Binary Classification)

#### ✔ Why this algorithm?
- Suitable for Yes/No prediction  
- Simple and efficient  
- Easy to interpret  

---

## 📊 Model Performance

- Accuracy: ~80%  
- Type: Binary Classification  

---

## 🔗 Colab Notebook

👉 https://colab.research.google.com/drive/1PFg8cIxupFUF6HsFs00cSKXiveYdLn4I?usp=drive_link

---

## 🧠 Workflow

1. Data Loading  
2. Data Cleaning (removed unnecessary columns like StudentID)  
3. Handling Missing Values  
4. Feature Selection  
5. Model Training (Logistic Regression)  
6. Model Evaluation  
7. Model Saving using Joblib  
8. UI Development using Streamlit  
9. Deployment using Streamlit Cloud  

---

## 🖥️ Streamlit App

The application allows users to:
- Enter student details  
- Predict placement status instantly  
- View results in a simple interface  

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
