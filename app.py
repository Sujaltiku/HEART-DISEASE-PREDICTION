import streamlit as st
import numpy as np
import joblib

st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="centered"
)

@st.cache_resource
def load_model():
    model = joblib.load("HEART-DISEASE-PREDICTION/logistic_model.joblib")
    return model

model = load_model()

st.markdown(
    """
    <h1 style='text-align: center; color: #E63946;'>
        Heart Disease Prediction System
    </h1>
    <p style='text-align: center; font-size:18px;'>
        Enter patient clinical details to predict risk of heart defect.
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

st.subheader("📋 Patient Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 1, 120, 45)
    sex = st.selectbox("Sex", [0, 1], help="0 = Female, 1 = Male")
    cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120)
    chol = st.number_input("Cholesterol", 100, 600, 200)
    fbs = st.selectbox("Fasting Blood Sugar > 120", [0, 1])

with col2:
    restecg = st.selectbox("Resting ECG", [0, 1, 2])
    thalach = st.number_input("Max Heart Rate (thalach)", 60, 220, 150)
    exang = st.selectbox("Exercise Induced Angina", [0, 1])
    oldpeak = st.number_input("Oldpeak (ST Depression)", 0.0, 10.0, 1.0)
    slope = st.selectbox("Slope", [0, 1, 2])
    ca = st.selectbox("Number of Major Vessels (ca)", [0, 1, 2, 3, 4])
    thal = st.selectbox("Thal", [0, 1, 2, 3])

st.divider()

if st.button("🔍 Predict", use_container_width=True):

    input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                            restecg, thalach, exang, oldpeak,
                            slope, ca, thal]])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("🩺 Prediction Result")

    if prediction == 1:
        st.error(f"⚠️ High Risk of Heart Defect\n\nProbability: {probability:.2%}")
    else:
        st.success(f"✅ No Significant Risk Detected\n\nProbability: {probability:.2%}")

    st.progress(float(probability))


st.markdown(
    """
    <hr>
    <p style='text-align: center;'>
        Built with Streamlit • Logistic Regression Model
    </p>
    """,
    unsafe_allow_html=True
)