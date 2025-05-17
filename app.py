import pandas as pd
import streamlit as st
import data_preprocessing as dp
from prediction import prediction

# Set page config
st.set_page_config(page_title='Student Dropout Predictor', layout='wide')

# Sidebar logo
with st.sidebar:
    st.image("asset/logo.png")

# Title
st.title("Student Dropout Prediction")
st.header("(Prototype)")

# Input Form
st.markdown("---")
st.markdown("<span style='color:#2FF3E0; font-size:24px'> General Information </span>", unsafe_allow_html=True)

data = pd.DataFrame()

# General Information
col1, col2, col3 = st.columns(3)
with col1:
    Age_at_enrollment = float(st.number_input(label='Age at Enrollment', value=19))
    data["Age_at_enrollment"] = [Age_at_enrollment]
with col2:
    Gender = st.selectbox(label='Gender', options=dp.encoder_Gender.classes_, index=0)
    data["Gender"] = [Gender]
with col3:
    Marital_status = st.selectbox(label='Marital Status', options=dp.encoder_Marital_status.classes_, index=3)
    data["Marital_status"] = [Marital_status]

col1, col2, col3 = st.columns(3)
with col1:
    International = st.selectbox(label='International Student', options=dp.encoder_International.classes_, index=0)
    data["International"] = [International]
with col2:
    Nacionality = st.selectbox(label='Nationality', options=dp.encoder_Nacionality.classes_, index=2)
    data["Nacionality"] = Nacionality

# Application Info
st.markdown("---")
st.markdown("<span style='color:#2FF3E0; font-size:24px'> Application Information </span>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    Course = st.selectbox(label='Course', options=dp.encoder_Course.classes_, index=14)
    data["Course"] = Course
with col2:
    Application_order = int(st.number_input(label='Application Order', value=1))
    data["Application_order"] = Application_order
with col3:
    Daytime_evening_attendance = st.selectbox(label='Attendance Shift', options=dp.encoder_Daytime_evening_attendance.classes_, index=0)
    data["Daytime_evening_attendance"] = [Daytime_evening_attendance]

col1, col2 = st.columns(2)
with col1:
    Application_mode = st.selectbox(label='Application Mode', options=dp.encoder_Application_mode.classes_, index=7)
    data["Application_mode"] = [Application_mode]
with col2:
    Admission_grade = int(st.number_input(label='Admission Grade', value=142.5))
    data["Admission_grade"] = Admission_grade

# Predict Button
st.markdown("---")
if st.button('Predict Dropout Status'):
    new_data = dp.data_preprocessing(data=data)
    st.write("### Prediction Result")
    st.success(f"Predicted Dropout Status: {prediction(new_data)}")

# Developer credit
st.caption('Faishal Anwar: IDCamp - Data Science (Expert Class)')
