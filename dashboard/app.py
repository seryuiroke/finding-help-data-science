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

st.markdown("""
### A Data Science Analysis of Online Help-Seeking Patterns for Domestic Violence Resources
""")

st.divider()

st.subheader("About this Project")

#description
st.write(
    "This interactive dashboard explores Google Trends data related to domestic violence support searches in the United States from 2019–2025. It demonstrates how publicly available search data can help identify patterns in online help-seeking behavior while emphasizing careful and ethical interpretation."
)

st.divider()

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

fig = px.line(
    df,
    x="date",
    y=selected_topic,
    title=f"{selected_topic.title()} Search Interest Over Time",
    markers=True
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Search Interest",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

# long-term change analysis
st.subheader("Long-Term Change: 2019 to 2025")

df["year"] = df["date"].dt.year

yearly_averages = df.groupby("year")[topics].mean()

change_2019_2025 = (
    yearly_averages.loc[2025] - yearly_averages.loc[2019]
).sort_values()

change_df = change_2019_2025.reset_index()
change_df.columns = ["topic", "change"]

change_fig = px.bar(
    change_df,
    x="change",
    y="topic",
    orientation="h",
    title="Change in Average Search Interest from 2019 to 2025",
    labels={
        "change": "Change in Search Interest",
        "topic": "Search Topic"
    }
)

change_fig.update_layout(
    template="plotly_white",
    yaxis_title="",
    xaxis_title="Change in Average Search Interest"
)

st.plotly_chart(
    change_fig,
    use_container_width=True
)

st.subheader("Key Insights")

st.info("""
• Domestic violence help showed the largest increase in average search interest between 2019 and 2025.

• Women's shelter searches showed the largest decrease over the same period.

• Emotional abuse search interest increased over the study period. This may reflect increased awareness, changes in terminology, media attention, or other factors that cannot be identified through search data alone.

• Search behavior changed differently across topics, highlighting the importance of using multiple indicators when studying help-seeking behavior.
""")

st.divider()

st.subheader("Resources")

st.write(
    "These organizations provide confidential information, support, and educational resources related to domestic violence and interpersonal abuse."
)

st.markdown("""
- [National Domestic Violence Hotline](https://www.thehotline.org/)
- [Love Is Respect](https://www.loveisrespect.org/)
- [RAINN](https://www.rainn.org/)
""")