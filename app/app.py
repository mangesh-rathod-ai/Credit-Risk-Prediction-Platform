import streamlit as st
from pathlib import Path

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Credit Risk Prediction Dashboard",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Load CSS
# --------------------------------------------------

def load_css():

    css_path = Path("assets")

    css = ""

    for file in css_path.glob("*.css"):
        css += file.read_text(encoding="utf-8")

    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

load_css()

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.markdown("""
<div class="hero-section">

<div class="hero-left">

<h1>🏦 Credit Risk Prediction Platform</h1>

<p>
AI Powered Loan Default Risk Assessment using Machine Learning
</p>

<div class="hero-badges">

<span class="badge-primary">LightGBM</span>

<span class="badge-success">Version 2.0</span>

<span class="badge-warning">Explainable AI</span>

</div>

</div>

</div>
""", unsafe_allow_html=True)

st.write("")

# --------------------------------------------------
# DASHBOARD METRICS
# --------------------------------------------------

st.subheader("📊 Dashboard Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("🤖 Model", "LightGBM")

with c2:
    st.metric("📈 ROC AUC", "0.768")

with c3:
    st.metric("🧠 Features", "18")

with c4:
    st.metric("✅ Status", "Ready")

st.write("")

# --------------------------------------------------
# FEATURE CARDS
# --------------------------------------------------

st.subheader("🚀 Dashboard Features")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
<div class="feature-card">

<h3>📊 Exploratory Data Analysis</h3>

<p>
Understand customer behavior through visualizations,
missing value analysis, correlations and distributions.
</p>

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="feature-card">

<h3>🤖 Credit Risk Prediction</h3>

<p>
Predict whether a loan applicant is likely
to default using a trained LightGBM model.
</p>

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="feature-card">

<h3>📈 Model Performance</h3>

<p>
Evaluate Accuracy, ROC Curve,
Confusion Matrix,
Precision,
Recall,
F1 Score and more.
</p>

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="feature-card">

<h3>📄 Project Documentation</h3>

<p>
Business Problem,
Feature Engineering,
Model Selection,
Evaluation,
Deployment.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# --------------------------------------------------
# PROJECT OVERVIEW
# --------------------------------------------------

st.subheader("📌 Project Overview")

left, right = st.columns([2,1])

with left:

    st.info("""

This dashboard predicts whether a loan applicant is likely
to default using an Explainable Artificial Intelligence model.

The project includes

• Exploratory Data Analysis

• Feature Engineering

• Machine Learning

• Explainable AI

• Model Evaluation

• Business Recommendations

• Interactive Dashboard

""")

with right:

    st.markdown("""
<div class="glass-card">

<h2>🏆 Highlights</h2>

<p>✔ LightGBM Model</p>

<p>✔ Feature Engineered Dataset</p>

<p>✔ Interactive Dashboard</p>

<p>✔ Explainable AI</p>

<p>✔ Banking Style UI</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# --------------------------------------------------
# ROADMAP
# --------------------------------------------------

st.subheader("🛣 Roadmap")

st.progress(35)

st.caption("Current Development Progress : 35%")

st.write("")

# --------------------------------------------------
# UPCOMING FEATURES
# --------------------------------------------------

st.subheader("⭐ Upcoming Features")

a, b, c = st.columns(3)

with a:

    st.success("""
SHAP Explainability

PDF Reports

Feature Importance
""")

with b:

    st.success("""
Prediction History

Eligibility Score

Business Insights
""")

with c:

    st.success("""
Probability Gauge

Risk Dashboard

Analytics
""")

st.write("")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.markdown(
"""
<div style='text-align:center;'>

<h4>Credit Risk Prediction Platform</h4>

Developed by <b>Mangesh Rathod</b>

Version 2.0

</div>
""",
unsafe_allow_html=True
)