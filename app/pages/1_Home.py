import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Home | Credit Risk Prediction",
    page_icon="🏦",
    layout="wide"
)

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.title("🏦 Credit Risk Prediction Dashboard")

st.markdown("---")

st.header("Welcome")

st.write(
    """
Welcome to the **Credit Risk Prediction Dashboard**.

This application predicts whether a loan applicant is likely to
default using Machine Learning models.

The dashboard provides:

- 📊 Exploratory Data Analysis
- 🤖 Loan Default Prediction
- 📈 Model Performance
- 📉 Feature Importance
- 📋 Project Documentation
- ℹ About the Project
"""
)

st.markdown("---")

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Model",
        value="LightGBM"
    )

with col2:
    st.metric(
        label="ROC-AUC",
        value="0.768"
    )

with col3:
    st.metric(
        label="Accuracy",
        value="92%"
    )

with col4:
    st.metric(
        label="Status",
        value="Ready"
    )

st.markdown("---")

# --------------------------------------------------
# DASHBOARD FEATURES
# --------------------------------------------------

st.subheader("Dashboard Modules")

c1, c2 = st.columns(2)

with c1:

    st.info("🏠 Home")

    st.success("🤖 Prediction")

    st.warning("📈 Analytics")

with c2:

    st.info("📊 Model Performance")

    st.success("📋 Documentation")

    st.warning("ℹ About")

st.markdown("---")

# --------------------------------------------------
# PROJECT OVERVIEW
# --------------------------------------------------

st.subheader("Project Overview")

st.write(
    """
The objective of this project is to predict whether
a customer will default on a loan using historical
loan application data.

The project includes:

• Data Cleaning

• Exploratory Data Analysis

• Feature Engineering

• Machine Learning Models

• Hyperparameter Tuning

• Model Evaluation

• Explainable AI

• Streamlit Dashboard
"""
)

st.markdown("---")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.caption(
    "Credit Risk Prediction Dashboard | Final Year Project | AI & Data Science"
)