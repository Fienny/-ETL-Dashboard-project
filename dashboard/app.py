import streamlit as st
import sqlite3
import pandas as pd
import os

# Page configuration
st.set_page_config(page_title="Customer Dashboard", layout="wide")

# Database connection
DB_PATH = os.path.join("database", "customers.db")
conn = sqlite3.connect(DB_PATH)

# Load data
df = pd.read_sql("SELECT * FROM customers", conn)

# Title
st.title("📊 Customer Dashboard")

# Top metric
st.metric("Total Customers", len(df))

# List of countries
countries = ["All"] + sorted(df['Country'].dropna().unique().tolist())

# Initialize session state
if "selected_country" not in st.session_state:
    st.session_state.selected_country = "All"

# Reset button comes before the selectbox to apply updates correctly
col1, col2 = st.columns([3, 1])
with col2:
    if st.button("🔄 Reset"):
        st.session_state.selected_country = "All"

# Country selectbox
with col1:
    selected_country = st.selectbox(
        "Select a Country",
        countries,
        index=countries.index(st.session_state.selected_country),
        key="selected_country"
    )

# Filter data by selected country
if selected_country != "All":
    df = df[df['Country'] == selected_country]

# Group by country for bar chart
country_df = df.groupby("Country").size().reset_index(name="Customers").sort_values("Customers", ascending=False)

# Bar chart by country
st.subheader("Customers by Country")
st.bar_chart(country_df.set_index("Country"))

# Convert date column and group by subscription date
df["Subscription Date"] = pd.to_datetime(df["Subscription Date"])
date_df = df.groupby("Subscription Date").size().reset_index(name="Subscriptions")

# Line chart by subscription date
st.subheader("Subscriptions Over Time")
st.line_chart(date_df.set_index("Subscription Date"))

# Full customer table
st.subheader("Customer Table")
st.dataframe(df)

# Close DB connection
conn.close()
