import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Finding Help",
    page_icon="📊",
    layout="wide"
)

# title
st.title("Finding Help")
st.subheader("A Data Science Analysis of Online Help-Seeking Patterns for Domestic Violence Resources")

# description
st.write("""
This interactive dashboard explores Google Trends data related to domestic violence support
searches in the United States from 2019–2025.
""")

# loading the cleaned dataset
df = pd.read_csv("data/raw/cleaned/google_trends_cleaned.csv")

# choose a topic
st.subheader("Explore Search Trends")

topics = [
    "domestic violence help",
    "abuse hotline",
    "women's shelter",
    "emotional abuse",
    "teen dating violence"
]

selected_topic = st.selectbox(
    "Select a search topic:",
    topics
)

# interactive line chart
st.line_chart(
    df.set_index("date")[selected_topic]
)