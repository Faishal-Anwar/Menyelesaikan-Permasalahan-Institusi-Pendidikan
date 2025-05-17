import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import streamlit as st
from streamlit_option_menu import option_menu
import data_preprocessing as dp
from prediction import prediction

sns.set(style='dark')

# Sidebar menu
with st.sidebar:
    st.image("asset/education logo.png")
    selected = option_menu(
        menu_title='Menu',
        options=['Predict'],
        icons=['calculator'],
        menu_icon='menu-up',
        default_index=0
    )

# Main application
if selected == 'Predict':
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image("asset/predict_white.png", width=130)
    with col2:
        st.title('Student Dropout Prediction')
        st.header('(Prototype)')

    with st.form("student_form"):
        data = pd.DataFrame()

        # General
        st.markdown("### 🧑‍🎓 General")
        col1, col2, col3 = st.columns(3)
        with col1:
            Age_at_enrollment = float(st.number_input('Age at Enrollment', value=19.0))
            data["Age_at_enrollment"] = [Age_at_enrollment]
        with col2:
            Gender = st.selectbox('Gender', dp.encoder_Gender.classes_, index=0)
            data["Gender"] = [Gender]
        with col3:
            Marital_status = st.selectbox('Marital Status', dp.encoder_Marital_status.classes_, index=3)
            data["Marital_status"] = [Marital_status]
        col1, col2, col3 = st.columns(3)
        with col1:
            International = st.selectbox('International', dp.encoder_International.classes_, index=0)
            data["International"] = [International]
        with col2:
            Nacionality = st.selectbox('Nationality', dp.encoder_Nacionality.classes_, index=2)
            data["Nacionality"] = [Nacionality]

        # Application
        st.markdown("### 📄 Application")
        col1, col2, col3 = st.columns(3)
        with col1:
            Course = st.selectbox('Course', dp.encoder_Course.classes_, index=14)
            data["Course"] = [Course]
        with col2:
            Application_order = int(st.number_input('Application Order', value=1))
            data["Application_order"] = [Application_order]
        with col3:
            Daytime_evening_attendance = st.selectbox('Daytime/Evening Attendance', dp.encoder_Daytime_evening_attendance.classes_, index=0)
            data["Daytime_evening_attendance"] = [Daytime_evening_attendance]
        col1, col2 = st.columns(2)
        with col1:
            Application_mode = st.selectbox('Application Mode', dp.encoder_Application_mode.classes_, index=7)
            data["Application_mode"] = [Application_mode]
        with col2:
            Admission_grade = float(st.number_input('Admission Grade', value=142.5))
            data["Admission_grade"] = [Admission_grade]
        col1, col2 = st.columns(2)
        with col1:
            Previous_qualification = st.selectbox('Previous Qualification', dp.encoder_Previous_qualification.classes_, index=8)
            data["Previous_qualification"] = [Previous_qualification]
        with col2:
            Previous_qualification_grade = float(st.number_input('Previous Qualification Grade', value=160.0))
            data["Previous_qualification_grade"] = [Previous_qualification_grade]

        # Additional
        st.markdown("### 📌 Additional Info")
        col1, col2, col3 = st.columns(3)
        with col1:
            Tuition_fees_up_to_date = st.selectbox('Tuition Fees Up to Date', dp.encoder_Tuition_fees_up_to_date.classes_, index=1)
            data["Tuition_fees_up_to_date"] = [Tuition_fees_up_to_date]
        with col2:
            Debtor = st.selectbox('Debtor', dp.encoder_Debtor.classes_, index=0)
            data["Debtor"] = [Debtor]
        with col3:
            Scholarship_holder = st.selectbox('Scholarship Holder', dp.encoder_Scholarship_holder.classes_, index=1)
            data["Scholarship_holder"] = [Scholarship_holder]
        col1, col2, col3 = st.columns(3)
        with col1:
            Displaced = st.selectbox('Displaced', dp.encoder_Displaced.classes_, index=1)
            data["Displaced"] = [Displaced]
        with col2:
            Educational_special_needs = st.selectbox('Educational Special Needs', dp.encoder_Educational_special_needs.classes_, index=0)
            data["Educational_special_needs"] = [Educational_special_needs]

        # Parents
        st.markdown("### 👪 Parents")
        col1, col2 = st.columns(2)
        with col1:
            Fathers_occupation = st.selectbox('Father\'s Occupation', dp.encoder_Fathers_occupation.classes_, index=5)
            data["Fathers_occupation"] = [Fathers_occupation]
        with col2:
            Fathers_qualification = st.selectbox('Father\'s Qualification', dp.encoder_Fathers_qualification.classes_, index=4)
            data["Fathers_qualification"] = [Fathers_qualification]
        col1, col2 = st.columns(2)
        with col1:
            Mothers_occupation = st.selectbox('Mother\'s Occupation', dp.encoder_Mothers_occupation.classes_, index=4)
            data["Mothers_occupation"] = [Mothers_occupation]
        with col2:
            Mothers_qualification = st.selectbox('Mother\'s Qualification', dp.encoder_Mothers_qualification.classes_, index=8)
            data["Mothers_qualification"] = [Mothers_qualification]

        # Demographics
        st.markdown("### 🌍 Demographics")
        col1, col2, col3 = st.columns(3)
        with col1:
            Unemployment_rate = float(st.number_input('Unemployment Rate', value=13.9))
            data["Unemployment_rate"] = [Unemployment_rate]
        with col2:
            Inflation_rate = float(st.number_input('Inflation Rate', value=-0.3))
            data["Inflation_rate"] = [Inflation_rate]
        with col3:
            GDP = float(st.number_input('GDP', value=0.79))
            data["GDP"] = [GDP]

        # Curricular Units 1st Semester
        st.markdown("### 📚 Curricular Units - 1st Semester")
        col1, col2, col3 = st.columns(3)
        with col1:
            data["Curricular_units_1st_sem_credited"] = [int(st.number_input('1st Credited', value=0))]
        with col2:
            data["Curricular_units_1st_sem_enrolled"] = [int(st.number_input('1st Enrolled', value=6))]
        with col3:
            data["Curricular_units_1st_sem_evaluations"] = [int(st.number_input('1st Evaluations', value=6))]
        col1, col2, col3 = st.columns(3)
        with col1:
            data["Curricular_units_1st_sem_approved"] = [float(st.number_input('1st Approved', value=6.0))]
        with col2:
            data["Curricular_units_1st_sem_grade"] = [float(st.number_input('1st Grade', value=14.0))]
        with col3:
            data["Curricular_units_1st_sem_without_evaluations"] = [float(st.number_input('1st Without Evaluations', value=0.0))]

        # Curricular Units 2nd Semester
        st.markdown("### 📘 Curricular Units - 2nd Semester")
        col1, col2, col3 = st.columns(3)
        with col1:
            data["Curricular_units_2nd_sem_credited"] = [int(st.number_input('2nd Credited', value=0))]
        with col2:
            data["Curricular_units_2nd_sem_enrolled"] = [int(st.number_input('2nd Enrolled', value=6))]
        with col3:
            data["Curricular_units_2nd_sem_evaluations"] = [int(st.number_input('2nd Evaluations', value=6))]
        col1, col2, col3 = st.columns(3)
        with col1:
            data["Curricular_units_2nd_sem_approved"] = [float(st.number_input('2nd Approved', value=6.0))]
        with col2:
            data["Curricular_units_2nd_sem_grade"] = [float(st.number_input('2nd Grade', value=13.67))]
        with col3:
            data["Curricular_units_2nd_sem_without_evaluations"] = [float(st.number_input('2nd Without Evaluations', value=0.0))]

        submitted = st.form_submit_button("Predict")

    # Display and Predict
    if submitted:
        with st.expander("📄 View Raw Data"):
            st.dataframe(data)

        new_data = dp.data_preprocessing(data)
        with st.expander("🛠️ View Preprocessed Data"):
            st.dataframe(new_data)

        result = prediction(new_data)
        st.success(f"🎯 Dropout Status: {result}")

# Footer
st.caption('Faishal Anwar: IDCamp - Data Science (Expert Class)')
