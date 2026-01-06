import os
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Supermart Retail Intelligence", layout="wide")

st.title("🛒 Supermart Retail Intelligence Dashboard")

# Load data
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

daily_sales = pd.read_csv(os.path.join(BASE_DIR, "outputs", "daily_sales.csv"), index_col=0)
monthly_sales = pd.read_csv(os.path.join(BASE_DIR, "outputs", "monthly_sales.csv"), index_col=0)
forecast = pd.read_csv(os.path.join(BASE_DIR, "outputs", "30_day_forecast.csv"), header=None, names=["Forecast"])
restock = pd.read_csv(os.path.join(BASE_DIR, "outputs", "restock_recommendations.csv"), index_col=0)

# Display data
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Daily Sales Trend")
    st.line_chart(daily_sales)

with col2:
    st.subheader("📆 Monthly Sales Trend")
    st.line_chart(monthly_sales)


st.subheader("🔮 30-Day Demand Forecast")
st.line_chart(forecast)

st.subheader("📦 Restocking Recommendations")
st.dataframe(restock)