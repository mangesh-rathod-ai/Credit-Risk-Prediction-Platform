import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="About | Credit Risk Prediction",
    page_icon="ℹ️",
    layout="wide"
)

# --------------------------------------------------
# PAGE TITLE
# --------------------------------------------------

st.title("ℹ️ About Project")

st.markdown("---")

# --------------------------------------------------
# PROJECT DESCRIPTION
# --------------------------------------------------

st.header("Credit Risk Prediction")

st.write("""
The **Credit Risk Prediction Dashboard** is a Machine Learning
application that predicts whether a loan applicant is likely
to default on a loan.

The project helps financial institutions reduce financial risk
by identifying high-risk applicants before approving loans.

The prediction is performed using the **LightGBM Machine Learning Model**.
""")

st.markdown("---")

# --------------------------------------------------
# PROJECT OBJECTIVES
# --------------------------------------------------

st.subheader("🎯 Project Objectives")

st.write("""
✔ Predict loan default

✔ Reduce financial risk

✔ Improve loan approval decisions

✔ Increase banking efficiency

✔ Assist financial analysts

✔ Support explainable AI
""")

st.markdown("---")

# --------------------------------------------------
# TECHNOLOGIES
# --------------------------------------------------

st.subheader("🛠 Technologies Used")

col1, col2 = st.columns(2)

with col1:

    st.success("Python")

    st.success("Pandas")

    st.success("NumPy")

    st.success("Scikit-Learn")

    st.success("LightGBM")

with col2:

    st.info("Matplotlib")

    st.info("Seaborn")

    st.info("SHAP")

    st.info("Streamlit")

    st.info("Git & GitHub")

st.markdown("---")

# --------------------------------------------------
# MACHINE LEARNING PIPELINE
# --------------------------------------------------

st.subheader("🤖 Machine Learning Workflow")

st.write("""
1. Data Collection

2. Data Cleaning

3. Exploratory Data Analysis

4. Feature Engineering

5. Data Preprocessing

6. Train-Test Split

7. Model Training

8. Hyperparameter Tuning

9. Model Evaluation

10. Prediction

11. Explainable AI (SHAP)

12. Streamlit Dashboard
""")

st.markdown("---")

# --------------------------------------------------
# MODEL INFORMATION
# --------------------------------------------------

st.subheader("📊 Model Information")

metric1, metric2, metric3 = st.columns(3)

with metric1:
    st.metric("Algorithm", "LightGBM")

with metric2:
    st.metric("ROC-AUC", "0.768")

with metric3:
    st.metric("Status", "Production Ready")

st.markdown("---")

# --------------------------------------------------
# DATASET INFORMATION
# --------------------------------------------------

st.subheader("📁 Dataset")

st.write("""
Dataset contains historical loan applications and customer
information used to train the prediction model.

The dataset includes:

• Applicant Information

• Income Details

• Credit History

• Employment Information

• Family Information

• Loan Details

• Previous Loan Records

• Engineered Features
""")

st.markdown("---")

# --------------------------------------------------
# DEVELOPER
# --------------------------------------------------

st.subheader("👨‍💻 Developer")

st.write("""
**Name:** Mangesh Rathod

**Role:** AI & Data Science Student

**Project:** Credit Risk Prediction Dashboard

**Machine Learning Model:** LightGBM

**Framework:** Streamlit
""")

st.markdown("---")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.caption(
    "Credit Risk Prediction Dashboard | Final Year Project | AI & Data Science"
)