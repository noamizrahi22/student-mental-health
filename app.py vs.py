import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Mental Health", layout="centered")

st.title("📊 Student Mental Health Dashboard")

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv("Student Mental Health Analysis During Online Learning.csv")

df = load_data()

# Preview
st.header("Dataset Preview")
st.dataframe(df.head())

# --- Insight 1: Screen Time ---
st.subheader("🕒 Screen Time Distribution")
fig1, ax1 = plt.subplots()
sns.histplot(data=df, x='Screen Time (hrs/day)', bins=20, kde=True, color='skyblue', ax=ax1)
ax1.set_title("Distribution of Daily Screen Time")
st.pyplot(fig1)
st.markdown("**Insight:** Most students spend between 6–9 hours on screens per day, indicating high digital exposure during online learning.")

# --- Insight 2: Sleep vs Stress ---
st.subheader("😴 Sleep Duration by Stress Level")
fig2, ax2 = plt.subplots()
sns.boxplot(data=df, x='Stress Level', y='Sleep Duration (hrs)', palette='pastel', ax=ax2)
ax2.set_title("Sleep Duration by Stress Level")
st.pyplot(fig2)
st.markdown("**Insight:** Students with higher stress tend to sleep less on average, suggesting a possible negative relationship between stress and sleep quality.")

# --- Insight 3: Physical Activity Distribution ---
st.subheader("🏃 Physical Activity Distribution")
fig3, ax3 = plt.subplots()
sns.histplot(data=df, x='Physical Activity (hrs/week)', bins=15, kde=True, color='seagreen', ax=ax3)
ax3.set_title("Weekly Physical Activity")
st.pyplot(fig3)
st.markdown("**Insight:** Physical activity levels vary, with some students reporting zero activity, which may be linked to higher stress or lower wellness.")

# --- Insight 4: Stress Level Count ---
st.subheader("📈 Stress Level Distribution")
fig4, ax4 = plt.subplots()
sns.countplot(data=df, x='Stress Level', palette='Set2', ax=ax4)
ax4.set_title("Stress Levels Among Students")
st.pyplot(fig4)
st.markdown("**Insight:** Most students report medium stress levels, while high stress is less common.")

# Footer
st.markdown("---")
st.caption("Created by Noa – Data Science Midterm Project 🧠")
