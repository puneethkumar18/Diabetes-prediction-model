import streamlit as st
import pandas as pd
import joblib
#pipe = joblib.load('diabetes.joblib')

st.title('Diabetes Disease Prediction')

col1, col2 = st.columns(2)

with col1:
    pregnanciess = st.number_input('Pregnancies', step=1)
with col2:
    glucose = st.number_input('Glucose')

col3, col4 = st.columns(2)

with col3:
    bp = st.number_input('Blood Pressure')
with col4:
    skin_thickness = st.number_input('Skin Thickness')

col5, col6 = st.columns(2)

with col5:
    insulin = st.number_input('Insulin')
with col6:
    bmi = st.number_input('Body Mass Index')

col7, col8 = st.columns(2)

with col7:
    dpf = st.number_input('Diabetes Pedigree Function')
with col8:
    age = st.number_input('Age', step=1)

if st.button('Predict'):
    input_df = pd.DataFrame({'Pregnancies': [pregnanciess],
                             'Glucose': [glucose],
                             'BloodPressure': [bp],
                             'SkinThickness': [skin_thickness],
                             'Insulin': [insulin],
                             'BMI': [bmi],
                             'DiabetesPedigreeFunction': [dpf],
                             'Age': [age]})
    result = pipe.predict(input_df)

    if result == 1:
        st.text("You have Diabetes")
    else:
        st.text("You don't have Diabetes")
