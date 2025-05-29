import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="NYC Restaurant Dashboard", layout="wide")

st.title("🌆 NYC Emerging Restaurant Dashboard")

df = pd.read_csv("cleaned_restaurants.csv")
df['Time of Submission'] = pd.to_datetime(df['Time of Submission'])

recent_df = df.copy() 

st.sidebar.header("Filters")
boroughs = st.sidebar.multiselect("Select Borough(s):", options=df['Borough'].unique(), default=df['Borough'].unique())

filtered_df = recent_df[recent_df['Borough'].isin(boroughs)]

st.subheader("📍 Restaurant Locations (Last 60 Days)")
fig_map = px.scatter_mapbox(
    filtered_df,
    lat='Latitude',
    lon='Longitude',
    hover_name='Restaurant Name',
    color='Borough',
    zoom=10,
    mapbox_style="open-street-map"
)
st.plotly_chart(fig_map, use_container_width=True)

st.subheader("📊 Seating Type Breakdown")
seating_count = filtered_df['Seating Interest (Sidewalk/Roadway/Both)'].value_counts()
st.bar_chart(seating_count)
