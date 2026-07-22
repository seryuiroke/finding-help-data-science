import plotly.express as px
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
df["date"] = pd.to_datetime(df["date"])

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
# calculate summary statistics
average_interest = df[selected_topic].mean()
highest_interest = df[selected_topic].max()
lowest_interest = df[selected_topic].min()

# display summary statistics
col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Search Interest",
    f"{average_interest:.1f}"
)

col2.metric(
    "Highest Search Interest",
    highest_interest
)

col3.metric(
    "Lowest Search Interest",
    lowest_interest
)

# interactive line chart
st.line_chart(
    df.set_index("date")[selected_topic]
)