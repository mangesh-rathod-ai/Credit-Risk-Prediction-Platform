import streamlit as st
import pandas as pd
import joblib

from pathlib import Path

st.set_page_config(
    page_title="Credit Risk Prediction",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Credit Risk Prediction")

st.markdown("""
Predict whether a loan applicant is likely to default using the trained LightGBM model.
""")

st.divider()

ROOT_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = ROOT_DIR / "models" / "lightgbm_deployment.pkl"
FEATURE_PATH = ROOT_DIR / "models" / "deployment_feature_names.pkl"

model = joblib.load(MODEL_PATH)
feature_names = joblib.load(FEATURE_PATH)

st.success("✅ Deployment Model Loaded Successfully")

st.subheader("📋 Applicant Information")

col1, col2 = st.columns(2)

with col1:

    income = st.number_input(
        "Annual Income",
        min_value=0.0,
        value=150000.0,
        step=1000.0
    )

    credit = st.number_input(
        "Credit Amount",
        min_value=0.0,
        value=500000.0,
        step=1000.0
    )

    goods_price = st.number_input(
        "Goods Price",
        min_value=0.0,
        value=450000.0,
        step=1000.0
    )

    annuity = st.number_input(
        "Loan Annuity",
        min_value=0.0,
        value=25000.0,
        step=500.0
    )

    age = st.number_input(
        "Age (Years)",
        min_value=18,
        max_value=100,
        value=35
    )

with col2:

    years_employed = st.number_input(
        "Years Employed",
        min_value=0.0,
        value=5.0
    )

    ext1 = st.slider(
        "EXT_SOURCE_1",
        0.0,
        1.0,
        0.50
    )

    ext2 = st.slider(
        "EXT_SOURCE_2",
        0.0,
        1.0,
        0.50
    )

    ext3 = st.slider(
        "EXT_SOURCE_3",
        0.0,
        1.0,
        0.50
    )




    # =====================================================
# Create Engineered Features
# =====================================================

# Convert Age to Days
days_birth = -(age * 365)

# Convert Years Employed to Days
days_employed = -(years_employed * 365)

# Approximate remaining day-based features
days_registration = days_employed - 1000
days_id_publish = days_birth + 5000
days_last_phone_change = -1000

# Engineered Features
credit_income_ratio = credit / income if income > 0 else 0

annuity_income_ratio = annuity / income if income > 0 else 0

loan_burden = annuity / credit if credit > 0 else 0

employment_ratio = years_employed / age if age > 0 else 0

credit_per_person = credit

ext_source_mean = (ext1 + ext2 + ext3) / 3


# =====================================================
# Predict Button
# =====================================================

st.divider()

predict = st.button(
    "🔮 Predict Credit Risk",
    use_container_width=True
)


# =====================================================
# Prediction
# =====================================================
# ============================================================
# Predict Credit Risk
# ============================================================

if predict:

    # -----------------------------
    # Create Input Dictionary
    # -----------------------------
    input_data = {

        "AMT_INCOME_TOTAL": income,
        "AMT_CREDIT": credit,
        "AMT_GOODS_PRICE": goods_price,
        "AMT_ANNUITY": annuity,

        "AGE": age,
        "YEARS_EMPLOYED": years_employed,

        "EXT_SOURCE_1": ext1,
        "EXT_SOURCE_2": ext2,
        "EXT_SOURCE_3": ext3,

        "LOAN_BURDEN": loan_burden,
        "EMPLOYMENT_RATIO": employment_ratio,
        "ANNUITY_INCOME_RATIO": annuity_income_ratio,
        "CREDIT_INCOME_RATIO": credit_income_ratio,
        "CREDIT_PER_PERSON": credit_per_person,

        "EXT_SOURCE_MEAN": ext_source_mean,

        "DAYS_BIRTH": days_birth,
        "DAYS_EMPLOYED": days_employed,
        "DAYS_REGISTRATION": days_registration,
        "DAYS_ID_PUBLISH": days_id_publish,
        "DAYS_LAST_PHONE_CHANGE": days_last_phone_change,
    }

    # -----------------------------
    # Convert to DataFrame
    # -----------------------------
    input_df = pd.DataFrame([input_data])

    # Match training feature order
    input_df = input_df.reindex(
        columns=feature_names,
        fill_value=0
    )

    # -----------------------------
    # Prediction
    # -----------------------------
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    # -----------------------------
    # Recommendation
    # -----------------------------
    if probability >= 0.70:
        recommendation = "❌ Reject"
    elif probability >= 0.40:
        recommendation = "⚠️ Manual Review"
    else:
        recommendation = "✅ Approve"

    # -----------------------------
    # Risk Level
    # -----------------------------
    if probability >= 0.70:
        risk_level = "🔴 High Risk"
    elif probability >= 0.40:
        risk_level = "🟡 Medium Risk"
    else:
        risk_level = "🟢 Low Risk"

    # ============================================================
    # Prediction Result
    # ============================================================

    st.divider()
    st.subheader("📊 Prediction Result")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Prediction",
            "🔴 Default" if prediction == 1 else "🟢 Non-Default"
        )

    with col2:
        st.metric(
            "Default Probability",
            f"{probability*100:.2f}%"
        )

    with col3:
        st.metric(
            "Recommendation",
            recommendation
        )

    st.write("### Risk Level")
    st.info(risk_level)

    st.progress(float(probability))

    # ============================================================
    # Final Decision Message
    # ============================================================

    if prediction == 1:

        st.error("""
### ⚠️ High Credit Risk

The applicant is likely to default on the loan.

**Recommendation:** Reject or perform detailed manual verification.
""")

    else:

        st.success("""
### ✅ Low Credit Risk

The applicant is likely to repay the loan successfully.

**Recommendation:** Loan can be approved.
""")