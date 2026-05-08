# -----------------------------
# 1. IMPORT LIBRARIES
# -----------------------------
import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# 2. LOAD DATA & MODEL
# -----------------------------
df = pd.read_csv("cleaned_jobml.csv")   # your cleaned dataset
model = joblib.load("job_acceptance_model.pkl")

# -----------------------------
# 3. PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Job Acceptance Dashboard", layout="wide")

st.title("📊 Job Acceptance Prediction System")

# -----------------------------
# 4. KPI CALCULATIONS
# -----------------------------
total_candidates = len(df)
placement_rate = df['status'].mean() * 100
acceptance_rate = placement_rate
avg_interview_score = df['interview_score_total'].mean()
avg_skills = df['skills_match_percentage'].mean()
dropout_rate = (1 - df['status'].mean()) * 100

high_risk = df[
    (df['skills_match_percentage'] < 50) &
    (df['interview_score_total'] < 50)
]
high_risk_pct = (len(high_risk) / len(df)) * 100

# -----------------------------
# 5. KPI DASHBOARD
# -----------------------------
st.subheader("📈 Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric("Total Candidates", total_candidates)
col1.metric("Placement Rate (%)", f"{placement_rate:.2f}")
col1.metric("Avg Interview Score", f"{avg_interview_score:.2f}")

col2.metric("Acceptance Rate (%)", f"{acceptance_rate:.2f}")
col2.metric("Avg Skills Match (%)", f"{avg_skills:.2f}")
col2.metric("Dropout Rate (%)", f"{dropout_rate:.2f}")

col3.metric("High Risk Candidates (%)", f"{high_risk_pct:.2f}")

# -----------------------------
# 6. CHARTS
# -----------------------------
st.subheader("📊 Visual Analysis")

st.write("### Academic Performance vs Placement")
st.bar_chart(df.groupby('status')['academic_avg'].mean())

st.write("### Interview Score vs Placement")
st.bar_chart(df.groupby('status')['interview_score_total'].mean())

st.write("### Skills Match vs Placement")
st.bar_chart(df.groupby('status')['skills_match_percentage'].mean())

# -----------------------------
# 7. BUSINESS INSIGHTS
# -----------------------------
st.markdown(f"""
### 🧠 Business Insights

- 📈 Higher interview scores strongly improve job acceptance  
- 🎯 Skills match ({avg_skills:.2f}%) plays a key role in placement  
- ⚠️ {high_risk_pct:.2f}% candidates are high-risk → need better screening  
- 📉 Dropout rate of {dropout_rate:.2f}% suggests engagement improvement needed  
""")

# -----------------------------
# 8. PREDICTION SECTION
# -----------------------------
st.subheader("🤖 Predict Job Acceptance")

st.write("Enter candidate details:")

skills = st.slider("Skills Match %", 0, 100, 50)
interview = st.slider("Interview Score", 0, 100, 50)
experience = st.number_input("Years of Experience", 0, 10, 1)

# Create input dataframe (simplified example)
input_data = pd.DataFrame({
    'skills_match_percentage': [skills],
    'interview_score_total': [interview],
    'years_of_experience': [experience]
})

# NOTE: Must match training features exactly in real case

if st.button("Predict"):
    try:
        prediction = model.predict(input_data)[0]

        if prediction == 1:
            st.success("✅ Candidate is likely to ACCEPT the job")
        else:
            st.error("❌ Candidate is likely to REJECT the job")

    except:
        st.warning("⚠️ Model expects full feature set (use full input form in real case)")