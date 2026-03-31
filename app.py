import streamlit as st
import pandas as pd
import numpy as np
import joblib


model = joblib.load("model_dropout.pkl")
scaler = joblib.load("scaler.pkl")
feature_names = joblib.load("feature_names.pkl")

st.set_page_config(page_title="Dropout Predictor", layout="wide")


st.title("Student Dropout Prediction System")
st.markdown("Predict student dropout risk for early intervention.")


st.sidebar.header("Input Student Data")

# Basic Info
age = st.sidebar.slider("Age at Enrollment", 17, 60, 20)
admission_grade = st.sidebar.slider("Admission Grade", 0.0, 200.0, 120.0)

# Academic Semester 1
approved = st.sidebar.slider("Approved Units (1st Sem)", 0, 20, 5)
enrolled = st.sidebar.slider("Enrolled Units (1st Sem)", 0, 20, 6)
grade = st.sidebar.slider("Average Grade (1st Sem)", 0.0, 20.0, 10.0)

# Financial

debtor = st.sidebar.selectbox("Debtor", [0, 1])
tuition = st.sidebar.selectbox("Tuition Fees Up To Date", [0, 1])


success_rate = approved / enrolled if enrolled != 0 else 0


input_dict = {
    'Age_at_enrollment': age,
    'Admission_grade': admission_grade,
    'Curricular_units_1st_sem_approved': approved,
    'Curricular_units_1st_sem_enrolled': enrolled,
    'Curricular_units_1st_sem_grade': grade,
    'Debtor': debtor,
    'Tuition_fees_up_to_date': tuition,
    'success_rate': success_rate
}

input_df = pd.DataFrame([input_dict])


model_features = feature_names
for col in model_features:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[model_features]


input_scaled = scaler.transform(input_df)


if st.button("Predict Dropout Risk"):
    prediction = model.predict(input_scaled)[0]
    proba = model.predict_proba(input_scaled)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error(f"High Risk of Dropout ({proba:.2%})")
    else:
        st.success(f"Low Risk ({proba:.2%})")

    st.markdown("### 💡 Insight")

    if success_rate < 0.5:
        st.warning("Low academic success rate detected")
    if debtor == 1:
        st.warning("Student has financial debt")
    if tuition == 0:
        st.warning("Tuition not paid")


st.markdown("---")
st.subheader("Input Data Preview")
st.dataframe(input_df)
