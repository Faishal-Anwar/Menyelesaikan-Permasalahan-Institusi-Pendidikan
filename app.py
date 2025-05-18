import pandas as pd
import numpy as np
import streamlit as st
import data_preprocessing as dp
from prediction import prediction

# Set page config with title, icon, and wide layout
st.set_page_config(page_title="Student Dropout Prediction", page_icon="🎓", layout="wide")

# Sidebar logo and menu
with st.sidebar:
    st.image("asset/logo.png", width=150)
    st.markdown("<h2 style='text-align: center; color: #2FF3E0;'>Menu</h2>", unsafe_allow_html=True)
    selected = st.radio("Pilih Halaman", ["Predict"])

if selected == 'Predict':
    st.title('Student Dropout Prediction')
    st.header('(Prototype)')
    st.markdown("<hr>", unsafe_allow_html=True)

    data = pd.DataFrame()

    # General Information Section
    st.markdown("<h3 style='color:#2FF3E0;'>General Information</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        Age_at_enrollment = float(st.number_input(label='Age at Enrollment', value=19, min_value=15, max_value=100))
        data["Age_at_enrollment"] = [Age_at_enrollment]
    with col2:
        Gender = st.selectbox(label='Gender', options=dp.encoder_Gender.classes_, index=0)
        data["Gender"] = [Gender]
    with col3:
        Marital_status = st.selectbox(label='Marital Status', options=dp.encoder_Marital_status.classes_, index=3)
        data["Marital_status"] = [Marital_status]
    col1, col2 = st.columns(2)
    with col1:
        International = st.selectbox(label='International', options=dp.encoder_International.classes_, index=0)
        data["International"] = [International]
    with col2:
        Nacionality = st.selectbox(label='Nationality', options=dp.encoder_Nacionality.classes_, index=2)
        data["Nacionality"] = [Nacionality]

    # Application Details Section
    st.markdown("<h3 style='color:#2FF3E0;'>Application Details</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        Course = st.selectbox(label='Course', options=dp.encoder_Course.classes_, index=14)
        data["Course"] = [Course]
    with col2:
        Application_order = int(st.number_input(label='Application Order', value=1, min_value=0, max_value=9))
        data["Application_order"] = [Application_order]
    with col3:
        Daytime_evening_attendance = st.selectbox(label='Attendance Type', options=dp.encoder_Daytime_evening_attendance.classes_, index=0)
        data["Daytime_evening_attendance"] = [Daytime_evening_attendance]
    col1, col2 = st.columns(2)
    with col1:
        Application_mode = st.selectbox(label='Application Mode', options=dp.encoder_Application_mode.classes_, index=7)
        data["Application_mode"] = [Application_mode]
    with col2:
        Admission_grade = float(st.number_input(label='Admission Grade', value=142.5, min_value=0, max_value=200))
        data["Admission_grade"] = [Admission_grade]
    col1, col2 = st.columns(2)
    with col1:
        Previous_qualification = st.selectbox(label='Previous Qualification', options=dp.encoder_Previous_qualification.classes_, index=8)
        data["Previous_qualification"] = [Previous_qualification]
    with col2:
        Previous_qualification_grade = float(st.number_input(label='Previous Qualification Grade', value=160.0, min_value=0, max_value=200))
        data["Previous_qualification_grade"] = [Previous_qualification_grade]

    # Additional Information Section
    st.markdown("<h3 style='color:#2FF3E0;'>Additional Information</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        Tuition_fees_up_to_date = st.selectbox(label='Tuition Fees Up To Date', options=dp.encoder_Tuition_fees_up_to_date.classes_, index=1)
        data["Tuition_fees_up_to_date"] = [Tuition_fees_up_to_date]
    with col2:
        Debtor = st.selectbox(label='Debtor Status', options=dp.encoder_Debtor.classes_, index=0)
        data["Debtor"] = [Debtor]
    with col3:
        Scholarship_holder = st.selectbox(label='Scholarship Holder', options=dp.encoder_Scholarship_holder.classes_, index=1)
        data["Scholarship_holder"] = [Scholarship_holder]
    col1, col2, col3 = st.columns(3)
    with col1:
        Displaced = st.selectbox(label='Displaced', options=dp.encoder_Displaced.classes_, index=1)
        data["Displaced"] = [Displaced]
    with col2:
        Educational_special_needs = st.selectbox(label='Educational Special Needs', options=dp.encoder_Educational_special_needs.classes_, index=0)
        data["Educational_special_needs"] = [Educational_special_needs]

    # Parents Information Section
    st.markdown("<h3 style='color:#2FF3E0;'>Parents Information</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        Fathers_occupation = st.selectbox(label='Father’s Occupation', options=dp.encoder_Fathers_occupation.classes_, index=5)
        data["Fathers_occupation"] = [Fathers_occupation]
    with col2:
        Fathers_qualification = st.selectbox(label='Father’s Qualification', options=dp.encoder_Fathers_qualification.classes_, index=4)
        data["Fathers_qualification"] = [Fathers_qualification]
    col1, col2 = st.columns(2)
    with col1:
        Mothers_occupation = st.selectbox(label='Mother’s Occupation', options=dp.encoder_Mothers_occupation.classes_, index=4)
        data["Mothers_occupation"] = [Mothers_occupation]
    with col2:
        Mothers_qualification = st.selectbox(label='Mother’s Qualification', options=dp.encoder_Mothers_qualification.classes_, index=8)
        data["Mothers_qualification"] = [Mothers_qualification]

    # Demographic Section
    st.markdown("<h3 style='color:#2FF3E0;'>Demographic</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        Unemployment_rate = float(st.number_input(label='Unemployment Rate (%)', value=13.9, min_value=0.0, max_value=100.0))
        data["Unemployment_rate"] = [Unemployment_rate]
    with col2:
        Inflation_rate = float(st.number_input(label='Inflation Rate (%)', value=-0.3, min_value=-100.0, max_value=100.0))
        data["Inflation_rate"] = [Inflation_rate]
    with col3:
        GDP = float(st.number_input(label='GDP Growth Rate (%)', value=0.79, min_value=-100.0, max_value=100.0))
        data["GDP"] = [GDP]

    # Curricular Units 1st Semester Section
    st.markdown("<h3 style='color:#2FF3E0;'>Curricular Units 1st Semester</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        data["Curricular_units_1st_sem_credited"] = [int(st.number_input(label='1st Sem Credited', value=0, min_value=0))]
    with col2:
        data["Curricular_units_1st_sem_enrolled"] = [int(st.number_input(label='1st Sem Enrolled', value=6, min_value=0))]
    with col3:
        data["Curricular_units_1st_sem_evaluations"] = [int(st.number_input(label='1st Sem Evaluations', value=6, min_value=0))]
    col1, col2, col3 = st.columns(3)
    with col1:
        data["Curricular_units_1st_sem_approved"] = [float(st.number_input(label='1st Sem Approved', value=6.0, min_value=0.0))]
    with col2:
        data["Curricular_units_1st_sem_grade"] = [float(st.number_input(label='1st Sem Grade', value=14.0, min_value=0.0, max_value=20.0))]
    with col3:
        data["Curricular_units_1st_sem_without_evaluations"] = [float(st.number_input(label='1st Sem Without Evaluations', value=0.0, min_value=0.0))]

    # Curricular Units 2nd Semester Section
    st.markdown("<h3 style='color:#2FF3E0;'>Curricular Units 2nd Semester</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        data["Curricular_units_2nd_sem_credited"] = [int(st.number_input(label='2nd Sem Credited', value=0, min_value=0))]
    with col2:
        data["Curricular_units_2nd_sem_enrolled"] = [int(st.number_input(label='2nd Sem Enrolled', value=6, min_value=0))]
    with col3:
        data["Curricular_units_2nd_sem_evaluations"] = [int(st.number_input(label='2nd Sem Evaluations', value=6, min_value=0))]
    col1, col2, col3 = st.columns(3)
    with col1:
        data["Curricular_units_2nd_sem_approved"] = [float(st.number_input(label='2nd Sem Approved', value=6.0, min_value=0.0))]
    with col2:
        data["Curricular_units_2nd_sem_grade"] = [float(st.number_input(label='2nd Sem Grade', value=13.67, min_value=0.0, max_value=20.0))]
    with col3:
        data["Curricular_units_2nd_sem_without_evaluations"] = [float(st.number_input(label='2nd Sem Without Evaluations', value=0.0, min_value=0.0))]

    # Show raw data input
    with st.expander("View the Raw Data"):
        st.dataframe(data=data, width=800)

    # Predict button and result
    if st.button('Predict'):
        new_data = dp.data_preprocessing(data=data)
        with st.expander("View the Preprocessed Data"):
            st.dataframe(data=new_data, width=800)
        result = prediction(new_data)
        st.markdown(f"<h3 style='color:#2FF3E0;'>Dropout Status Prediction: <strong>{result}</strong></h3>", unsafe_allow_html=True)

st.caption('Faishal Anwar: IDCamp - Data science (expert class)')

