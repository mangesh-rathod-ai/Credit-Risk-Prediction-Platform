# 💳 Credit Risk Prediction using Machine Learning

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-Web%20Application-FF4B4B?logo=streamlit" />
  <img src="https://img.shields.io/badge/LightGBM-Model-success" />
  <img src="https://img.shields.io/badge/XGBoost-Model-orange" />
  <img src="https://img.shields.io/badge/Random%20Forest-Model-green" />
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen" />
</p>

---

## 📌 Project Overview

**Credit Risk Prediction** is an end-to-end Machine Learning project that predicts whether a loan applicant is likely to repay a loan or default.

The project combines **data preprocessing, feature engineering, model training, model comparison, business analytics, and deployment** into an interactive Streamlit web application.

The objective is to help financial institutions make better lending decisions by identifying high-risk applicants before approving loans.

---

# 🚀 Features

- 📊 Interactive Streamlit Dashboard
- 🤖 Credit Risk Prediction
- 📈 Data Analysis Dashboard
- 📉 Model Performance Comparison
- 📋 Feature Engineering Pipeline
- 📊 Feature Importance Analysis
- 📉 Confusion Matrix Visualization
- 📈 ROC Curve
- 🎨 Professional UI Design
- 📱 Responsive Layout

---

# 🧠 Machine Learning Models

The project compares multiple machine learning algorithms.

- LightGBM
- XGBoost
- Random Forest

Models are evaluated using multiple performance metrics to select the best-performing model for deployment.

---

# 📂 Project Structure

```text
Credit-Risk-Prediction/
│
├── app/
│   ├── assets/
│   ├── pages/
│   ├── utils/
│   ├── app.py
│   └── main_prediction.py
│
├── models/
│
├── notebooks/
│
├── src/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# ⚙️ Technologies Used

## Programming Language

- Python

## Machine Learning

- Scikit-learn
- LightGBM
- XGBoost
- Random Forest

## Data Analysis

- Pandas
- NumPy

## Data Visualization

- Plotly
- Matplotlib

## Deployment

- Streamlit

## Development Tools

- VS Code
- Git
- GitHub

---

# 📊 Dataset

This project uses the **Home Credit Default Risk** dataset.

The dataset is **not included** in this repository because of GitHub file size limitations.

Download the dataset from:

https://www.kaggle.com/competitions/home-credit-default-risk

Place the downloaded CSV files inside the `data/` directory before running the application.

---

# 📈 Machine Learning Workflow

```text
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Engineering
      │
      ▼
Data Preprocessing
      │
      ▼
Train-Test Split
      │
      ▼
Model Training
      │
      ▼
Hyperparameter Tuning
      │
      ▼
Model Evaluation
      │
      ▼
Prediction
```

---

# 📊 Model Evaluation Metrics

The models are evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix

---

# 💻 Installation

## Clone Repository

```bash
git clone https://github.com/maggi-2231/Credit-Risk-Prediction.git
```

## Move into Project

```bash
cd Credit-Risk-Prediction
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Virtual Environment

Windows

```bash
.venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app/app.py
```

---

# 📷 Application Pages

### 🏠 Home

Project introduction and overview.

### 📊 Data Analysis

Exploratory data analysis with interactive visualizations.

### 📈 Model Performance

Performance comparison of machine learning models.

### 🔮 Prediction

Predicts whether a customer is likely to default on a loan.

### 👨‍💻 About

Project information and developer details.

---

# 🎯 Business Problem

Banks and financial institutions face significant losses due to loan defaults.

This project helps organizations by:

- Identifying high-risk customers
- Supporting loan approval decisions
- Reducing financial risk
- Improving lending strategies
- Enabling data-driven decision making

---

# 📌 Future Improvements

- SHAP Explainability
- Docker Deployment
- FastAPI REST API
- Cloud Deployment
- Model Monitoring
- CI/CD Pipeline
- User Authentication
- Database Integration

---

# 👨‍💻 Author

**Mangesh Rathod**

B.Tech – Artificial Intelligence & Data Science

Machine Learning Engineer | Data Scientist | AI Engineer

### GitHub

https://github.com/maggi-2231

### LinkedIn

Add your LinkedIn profile link here.

---

# ⭐ Show Your Support

If you found this project helpful, please give it a ⭐ on GitHub.