import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

# Load model
model = joblib.load("models/XGBoost_salary_model.pkl")

st.set_page_config(page_title="Salary Predictor", layout="wide")
st.title("💼 Employee Salary Predictor")

st.markdown("Enter employee details to estimate monthly and yearly salary with insights:")

# === Input UI ===
with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("👤 Age", min_value=18, max_value=100, value=30)
        experience = st.slider("💼 Years of Experience", 0, 40, 5)

    with col2:
        gender = st.radio("⚧ Gender", ["Male", "Female"], horizontal=True)
        education_level = st.selectbox(
            "🎓 Education Level", ["High School", "Bachelor's", "Master's", "PhD", "Other"]
        )

    with col3:
        job_title = st.selectbox(
            "🧾 Job Title",
            [
                "Software Engineer", "Data Scientist", "Product Manager", "Sales Executive",
                "HR Specialist", "Marketing Analyst", "Business Analyst", "Designer",
                "Teacher", "Financial Analyst", "Engineer", "Consultant", "Other"
            ]
        )

    st.markdown("---")

# === Predict Button ===
if st.button("🔍 Predict Salary"):
    input_data = pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "Education Level": [education_level],
        "Job Title": [job_title],
        "Years of Experience": [experience]
    })

    try:
        monthly_salary = model.predict(input_data)[0]
        yearly_salary = monthly_salary * 12

        # ==== Salary Display ====
        st.markdown("## 💰 Salary Estimate")
        st.success(f"**Estimated Monthly Salary:** ₹{monthly_salary:,.0f}")
        st.success(f"**Estimated Yearly Salary:** ₹{yearly_salary:,.0f}")
        # --- Projection & Salary Breakdown side by side ---
        st.markdown("### 📊 Salary Projection & Breakdown")

        colA, colB = st.columns(2)

        with colA:
            st.subheader("📈 5-Year Projection")
            years = [f"Year {i}" for i in range(1, 6)]
            projected = [monthly_salary * (1.05 ** i) for i in range(1, 6)]

            fig3, ax3 = plt.subplots()
            ax3.plot(years, projected, marker='o', color='green')
            ax3.set_ylabel("Monthly Salary (₹)")
            ax3.set_title("Projected Monthly Salary Growth")
            st.pyplot(fig3)

        with colB:
            st.subheader("📎 Salary Breakdown")
            breakdown_labels = ["Basic Pay", "Allowances", "Bonus"]
            breakdown_values = [
                monthly_salary * 0.6,
                monthly_salary * 0.25,
                monthly_salary * 0.15
            ]
            dark_palette = ["#2E86AB", "#E07A5F", "#81B29A"]

            fig4, ax4 = plt.subplots()
            ax4.pie(
                breakdown_values,
                labels=breakdown_labels,
                autopct="%1.0f%%",
                colors=dark_palette,
                startangle=90
            )
            ax4.axis("equal")
            st.pyplot(fig4)

    except Exception as e:
        st.error(f"Prediction failed: {e}")
