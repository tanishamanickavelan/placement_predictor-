import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('placement_model.pkl')

st.title("🎓 Student Placement Predictor")

st.write("Enter student details to predict placement")

# Inputs
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0)
internships = st.number_input("Internships", min_value=0)
projects = st.number_input("Projects", min_value=0)
workshops = st.number_input("Workshops/Certifications", min_value=0)
aptitude = st.number_input("Aptitude Test Score", min_value=0)
softskills = st.number_input("Soft Skills Rating", min_value=0.0, max_value=5.0)
ssc = st.number_input("SSC Marks", min_value=0)
hsc = st.number_input("HSC Marks", min_value=0)

# Prediction button
if st.button("Predict"):
    input_data = np.array([[cgpa, internships, projects, workshops,
                            aptitude, softskills, ssc, hsc]])

    result = model.predict(input_data)

    if result[0] == 1:
        st.success("✅ High chances of placement")
    else:
        st.error("❌ Low chances of placement")