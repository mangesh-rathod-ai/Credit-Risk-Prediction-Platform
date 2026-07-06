import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import json
from streamlit_lottie import st_lottie

# ==========================
# Page Configuration
# ==========================

st.set_page_config(
    page_title="Data Analysis",
    page_icon="📊",
    layout="wide"
)



# ==========================
# Title
# ==========================

st.title("📊 Exploratory Data Analysis")
st.markdown("---")

# ==========================
# Dataset Path
# ==========================

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_PATH = BASE_DIR / "data" / "processed" / "deployment_dataset.csv"

# ==========================
# Load Dataset
# ==========================

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

try:
    df = load_data()

except FileNotFoundError:
    st.error(f"Dataset not found:\n\n{DATA_PATH}")
    st.stop()

# ==========================
# Dataset Overview
# ==========================

st.subheader("📌 Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Rows", f"{df.shape[0]:,}")
col2.metric("Columns", df.shape[1])
col3.metric("Missing Values", int(df.isna().sum().sum()))
col4.metric("Duplicate Rows", int(df.duplicated().sum()))

st.markdown("---")

# ==========================
# Dataset Preview
# ==========================

st.subheader("📋 Dataset Preview")

st.dataframe(df.head(), use_container_width=True)

st.markdown("---")

# ==========================
# Target Distribution
# ==========================

if "TARGET" in df.columns:

    st.subheader("🎯 Target Distribution")

    target = df["TARGET"].value_counts().reset_index()
    target.columns = ["Target", "Count"]

    target["Target"] = target["Target"].replace({
        0: "Non-Default",
        1: "Default"
    })

    fig = px.pie(
        target,
        names="Target",
        values="Count",
        hole=0.5,
        title="Loan Default Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

# ==========================
# Missing Values
# ==========================

st.subheader("📉 Top Missing Features")

missing = (
    df.isna()
      .sum()
      .sort_values(ascending=False)
)

missing = missing[missing > 0].head(20)

if len(missing):

    fig = px.bar(
        x=missing.values,
        y=missing.index,
        orientation="h",
        labels={
            "x": "Missing Values",
            "y": "Feature"
        },
        title="Top 20 Missing Features"
    )

    st.plotly_chart(fig, use_container_width=True)

else:

    st.success("✅ No Missing Values Found")

st.markdown("---")

# ==========================
# Feature Distribution
# ==========================

numeric_cols = df.select_dtypes(include="number").columns.tolist()

if len(numeric_cols):

    st.subheader("📈 Feature Distribution")

    feature = st.selectbox(
        "Select Numerical Feature",
        numeric_cols
    )

    fig = px.histogram(
        df,
        x=feature,
        nbins=40,
        title=f"{feature} Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================
# Correlation Heatmap
# ==========================

st.subheader("🔥 Correlation Heatmap")

corr = df.select_dtypes(include="number").corr()

fig = px.imshow(
    corr,
    aspect="auto",
    color_continuous_scale="RdBu_r",
    title="Correlation Matrix"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================
# Summary Statistics
# ==========================

st.subheader("📋 Summary Statistics")

st.dataframe(df.describe(), use_container_width=True)

st.markdown("---")

# ==========================
# Dataset Information
# ==========================

st.subheader("📄 Dataset Information")

info_df = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str),
    "Missing Values": df.isna().sum().values
})

st.dataframe(info_df, use_container_width=True)

st.success("✅ Data Analysis Loaded Successfully")