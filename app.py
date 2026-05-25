# importing libraries

import streamlit as st
import joblib
import numpy as np

# loading the model
model = joblib.load('diabetes_model.pkl')
scaler = joblib.load('scaler.pkl')

# title and asking for input
st.title('Intelligent Diabetes Prediction System')
st.write('Please enter the following details to predict the likelihood of diabetes: ')

# User Input
col1, col2 = st.columns(2)

with col1:
    preg = st.slider("Pregnancies", 0, 17, 1)
    plas = st.slider("Glucose Level", 0, 200, 120)
    pres = st.slider("Blood Pressure", 0, 122, 70)

with col2:
    mass = st.slider("BMI", 0.0, 67.0, 25.0)
    pedi = st.slider("Diabetes Pedigree Function", 0.0, 2.5, 0.5)
    age = st.slider("Age", 21, 81, 30)

# creating a button for prediction -- prediction logic
if st.button('Predict'):
    # creating a numpy array for the input data
    input_data = np.array([[preg, plas, pres, mass, pedi, age]])
    # scaling the input data
    input_data_scaled = scaler.transform(input_data)
    # making the prediction
    result = model.predict(input_data_scaled)
    # calculating the probability of diabetes
    probability = model.decision_function(input_data_scaled)[0]
    # Risk Level
    if result[0] == 0:
        st.success("✅ Low Risk — Patient is likely Non-Diabetic")
        risk = "Low"
    elif plas > 140 or mass > 35:
        st.error("🔴 High Risk — Patient is likely Diabetic")
        risk = "High"
    else:
        st.warning("🟡 Medium Risk — Patient may be Diabetic")
        risk = "Medium"
    # Recommendations
    st.subheader("📋 Recommendations")
    if risk == "Low":
        st.write("• Maintain healthy diet")
        st.write("• Stay physically active")
        st.write("• Regular health checkups")
    elif risk == "Medium":
        st.write("• Monitor glucose levels regularly")
        st.write("• Reduce sugar and carb intake")
        st.write("• Consult a doctor soon")
        st.write("• Exercise at least 30 mins daily")
    else:
        st.write("• Consult a doctor immediately")
        st.write("• Strictly reduce sugar intake")
        st.write("• Monitor blood pressure daily")
        st.write("• Follow prescribed medication")