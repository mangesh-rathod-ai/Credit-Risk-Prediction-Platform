import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Model Performance Dashboard")
st.markdown("### Compare the performance of all Machine Learning models")

st.divider()

# -----------------------------
# KPI Cards
# -----------------------------

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        label="🏆 Best Model",
        value="LightGBM"
    )

with c2:
    st.metric(
        label="🎯 ROC-AUC",
        value="0.7684"
    )

with c3:
    st.metric(
        label="📊 Recall",
        value="67.17%"
    )

st.divider()

# -----------------------------
# Model Comparison Table
# -----------------------------

st.subheader("📊 Model Comparison")

comparison = pd.DataFrame({
    "Model":[
        "Random Forest",
        "XGBoost",
        "LightGBM"
    ],

    "Accuracy":[
        0.9202,
        0.7567,
        0.7216
    ],

    "Precision":[
        0.6627,
        0.1885,
        0.1771
    ],

    "Recall":[
        0.0222,
        0.6095,
        0.6717
    ],

    "F1 Score":[
        0.0429,
        0.2880,
        0.2803
    ],

    "ROC-AUC":[
        0.7678,
        0.7617,
        0.7684
    ]
})

st.dataframe(
    comparison,
    use_container_width=True
)

st.divider()

# -----------------------------
# Accuracy Comparison
# -----------------------------

st.subheader("📈 Accuracy Comparison")

fig = px.bar(
    comparison,
    x="Model",
    y="Accuracy",
    text="Accuracy",
    color="Model"
)

fig.update_layout(height=450)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# ROC-AUC Comparison
# -----------------------------

st.subheader("🎯 ROC-AUC Comparison")

fig = px.bar(
    comparison,
    x="Model",
    y="ROC-AUC",
    text="ROC-AUC",
    color="Model"
)

fig.update_layout(height=450)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# Recall Comparison
# -----------------------------

st.subheader("📌 Recall Comparison")

fig = px.bar(
    comparison,
    x="Model",
    y="Recall",
    text="Recall",
    color="Model"
)

fig.update_layout(height=450)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# -----------------------------
# Why LightGBM?
# -----------------------------

st.subheader("🏆 Why LightGBM was Selected")

st.success("""
✔ Highest Recall (67.17%)

✔ Highest ROC-AUC (0.7684)

✔ Best performance on Imbalanced Dataset

✔ Fast Training Time

✔ Industry Standard for Credit Risk Prediction
""")