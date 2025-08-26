import os
import pandas as pd
import streamlit as st

# Get absolute path of this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "trends_data.csv")

# Load dataset safely
if os.path.exists(DATA_PATH):
    df = pd.read_csv(DATA_PATH, parse_dates=["date"])
else:
    st.error(f"❌ Data file not found at {DATA_PATH}. Please run fetch_data.py first.")
    st.stop()

# Streamlit Dashboard
st.title("📊 Google Trends Insights Dashboard")

# Show raw data
st.subheader("Raw Data")
st.dataframe(df.head())

# Show simple chart
st.subheader("Trends Over Time")
selected_keyword = st.selectbox("Choose a keyword", df.columns.drop("date"))
st.line_chart(df.set_index("date")[[selected_keyword]])

