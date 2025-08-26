import streamlit as st
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Google Trends Dashboard", layout="wide")

# Title
st.title("📊 Google Trends Insights Dashboard")

# Input keywords
keywords = st.text_input("Enter keywords (comma separated):", "AI, Data Science, Machine Learning")

if st.button("Fetch Trends"):
    kw_list = [k.strip() for k in keywords.split(",")]
    pytrends = TrendReq(hl='en-US', tz=330)
    pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='', gprop='')

    data = pytrends.interest_over_time()

    if not data.empty:
        st.subheader("📈 Trends Over Time")
        st.line_chart(data[kw_list])

        st.subheader("📊 Data Preview")
        st.write(data.head())
    else:
        st.warning("⚠️ No data found. Try different keywords.")
