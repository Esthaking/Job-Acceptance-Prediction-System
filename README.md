# 📊 Job Acceptance Prediction System

## 📌 Project Overview

The **Job Acceptance Prediction System** is an end-to-end Machine Learning project designed to predict whether a candidate will accept or reject a job offer based on academic performance, technical skills, interview performance, work experience, and job market conditions.

The project focuses on solving real-world recruitment challenges such as offer dropouts, inefficient hiring decisions, and candidate evaluation complexity by providing predictive insights and business analytics through an interactive Streamlit dashboard.

---

# 🎯 Business Problem

Recruitment and placement teams often deal with thousands of candidate profiles containing academic records, skills, certifications, interview scores, experience details, and company-related information.

However, not all selected candidates accept job offers, leading to:

- Increased hiring cycle time
- Offer dropouts
- Resource wastage
- Delayed onboarding
- Inefficient recruitment planning

This project helps organizations predict candidate job acceptance probability and identify the major factors influencing placement success.

---

# 🚀 Objectives

- Predict whether a candidate will accept or reject a job offer
- Analyze factors influencing placement outcomes
- Handle real-world noisy and missing data
- Generate business insights for recruitment optimization
- Build an interactive Streamlit dashboard for analytics and prediction

---

# 📂 Dataset Information

The dataset contains approximately **50,000 candidate records** and includes features related to:

- Academic performance
- Technical & aptitude scores
- Communication skills
- Skills match percentage
- Certifications
- Internship experience
- Work experience
- Salary expectations
- Company tier
- Interview performance
- Market competition level
- Placement status (Target Variable)

The dataset also contains intentionally introduced real-world data challenges such as:

- Missing values
- Inconsistent categorical labels
- Outliers
- Noisy records

---

# 🧹 Data Cleaning & Preprocessing

The following preprocessing techniques were applied:

### ✅ Missing Value Handling
- Median imputation for numerical features
- Context-based imputation for categorical features
- Logical analysis before filling missing values

### ✅ Outlier Handling
- IQR-based outlier detection
- Capping extreme values for selected numerical columns

### ✅ Data Standardization
- Corrected inconsistent categorical labels
- Converted object datatypes into proper numerical formats

### ✅ Encoding
- Label Encoding for binary categorical features
- One-Hot Encoding for multi-category features

### ✅ Feature Scaling
- StandardScaler used for continuous numerical features

---

# 🧠 Feature Engineering

New analytical features were created to improve model performance and business understanding:

- `academic_avg`
- `interview_score_total`
- `skills_level`
- `experience_level`
- `salary_gap`

These engineered features helped improve prediction capability and interpretability.

---

# 📊 Exploratory Data Analysis (EDA)

EDA was performed to uncover trends and business insights such as:

- Academic performance vs placement outcome
- Skills match vs interview performance
- Certifications impact on job acceptance
- Experience vs placement success
- Interview score vs placement probability
- Employability score analysis

Visualization techniques used:
- Boxplots
- Histograms
- Scatterplots
- Correlation Heatmaps
- Bar Charts

---

# 🤖 Machine Learning Modeling

The following machine learning models were implemented and compared:

- Logistic Regression
- Random Forest Classifier

### Model Optimization
- Pipeline-based preprocessing
- GridSearchCV for hyperparameter tuning
- Class imbalance handling using `class_weight='balanced'`

### Evaluation Metrics
- Accuracy Score
- Classification Report
- Feature Importance Analysis

---

# 📈 Streamlit Dashboard Features

An interactive Streamlit dashboard was developed to provide:

## 📌 Key KPIs
- Total Candidates
- Placement Rate (%)
- Job Acceptance Rate (%)
- Average Interview Score
- Average Skills Match (%)
- Offer Dropout Rate
- High-Risk Candidate Percentage

## 📊 Visual Analytics
- Academic Performance Analysis
- Interview Performance Analysis
- Skills Match Analysis
- Placement Trends

## 🤖 Prediction System
Users can provide candidate details and predict whether the candidate is likely to accept or reject the job offer.

---

# 🧠 Business Insights

- Higher interview scores strongly improve job acceptance probability
- Skills match percentage plays a critical role in placement success
- Candidates with low interview and skills scores fall under high-risk category
- Offer dropout rate indicates opportunities for improving candidate engagement strategies

---

# 🛠️ Technologies Used

| Category | Tools & Libraries |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Dashboard | Streamlit |
| Model Saving | Joblib |
| Development Environment | VS Code, Jupyter Notebook |

---

#
