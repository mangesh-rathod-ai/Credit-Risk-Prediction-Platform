import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

from pathlib import Path
import json
from streamlit_lottie import st_lottie

animation_path = Path("app/assets/animations/analytics/counter.json")

with open(animation_path, "r") as f:
    counter_animation = json.load(f)

st_lottie(counter_animation, height=250, key="counter")





st.set_page_config(
    page_title="Data Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Exploratory Data Analysis")

st.markdown("---")

# Load Dataset
from pathlib import Path

# Project root folder
BASE_DIR = Path(__file__).resolve().parents[2]

# Dataset path
from pathlib import Path

# Project root folder
BASE_DIR = Path(__file__).resolve().parents[2]

# Dataset path
DATA_PATH = BASE_DIR / "data" / "processed" / "application_train_feature_engineered.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

# ==========================
# Dataset Overview
# ==========================

st.subheader("📌 Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Rows", f"{df.shape[0]:,}")
col2.metric("Columns", df.shape[1])
col3.metric("Missing Values", int(df.isna().sum().sum()))
col4.metric("Duplicate Rows", df.duplicated().sum())

st.markdown("---")

# ==========================
# Dataset Preview
# ==========================

st.subheader("📋 Dataset Preview")

st.dataframe(df.head())

st.markdown("---")

# ==========================
# Target Distribution
# ==========================

st.subheader("🎯 Target Distribution")

target = df["TARGET"].value_counts().reset_index()
target.columns = ["Target", "Count"]

target["Target"] = target["Target"].map({
    0: "Non-Default",
    1: "Default"
})

fig = px.pie(
    target,
    names="Target",
    values="Count",
    hole=0.5,
    color="Target",
    title="Loan Default Distribution"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================
# Missing Values
# ==========================

st.subheader("📉 Top Missing Features")

missing = (
    df.isna().sum()
      .sort_values(ascending=False)
      .head(20)
)

missing = missing[missing > 0]

if len(missing) > 0:

    fig = px.bar(
        missing,
        orientation="h",
        title="Top Missing Features"
    )

    st.plotly_chart(fig, use_container_width=True)

else:

    st.success("✅ No Missing Values Found!")

st.markdown("---")

# ==========================
# Numerical Feature
# ==========================

st.subheader("📈 Feature Distribution")

numeric_cols = df.select_dtypes(include="number").columns.tolist()

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
# Summary Statistics
# ==========================

st.subheader("📋 Summary Statistics")

st.dataframe(df.describe())