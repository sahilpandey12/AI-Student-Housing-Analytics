import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3
from ai_insights import generate_insights

# Page configuration
st.set_page_config(
    page_title="AI Booking Analytics",
    page_icon="🏠",
    layout="wide"
)

# Load dataset
df = pd.read_csv("bookings.csv")

df["Booking_Date"] = pd.to_datetime(
    df["Booking_Date"]
)

# Connect to database
conn = sqlite3.connect("bookings.db")

df.to_sql(
    "bookings",
    conn,
    if_exists="replace",
    index=False
)

# Dashboard title
st.title("🏠 Student Housing Analytics")
st.caption(
    "AI-powered business intelligence dashboard"
)

# Sidebar
st.sidebar.header("Dashboard Filters")

cities = st.sidebar.multiselect(
    "Select Cities",
    df["City"].unique(),
    default=df["City"].unique()
)

filtered = df[df["City"].isin(cities)]

# SQL KPI calculation
if cities:

    placeholders = ",".join(
        ["?"] * len(cities)
    )

    query = f"""
    SELECT
        COUNT(*) AS Total_Records,

        SUM(
            CASE WHEN Booking_Status = 'Booked'
            THEN 1 ELSE 0 END
        ) AS Total_Bookings,

        ROUND(
            AVG(
                CASE WHEN Booking_Status = 'Booked'
                THEN Monthly_Rent END
            ), 0
        ) AS Average_Rent

    FROM bookings

    WHERE City IN ({placeholders})
    """

    metrics = pd.read_sql_query(
        query,
        conn,
        params=cities
    ).iloc[0]

else:

    metrics = {
        "Total_Records": 0,
        "Total_Bookings": 0,
        "Average_Rent": 0
    }

# KPI cards
st.subheader("Business Overview")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Total Records",
    int(metrics["Total_Records"])
)

c2.metric(
    "Confirmed Bookings",
    int(metrics["Total_Bookings"])
)

c3.metric(
    "Average Monthly Rent",
    f"₹{metrics['Average_Rent']:,.0f}"
    if pd.notna(metrics["Average_Rent"])
    else "₹0"
)

st.divider()

# City analysis
st.subheader("📍 City-wise Booking Analysis")

city_data = filtered[
    filtered["Booking_Status"] == "Booked"
].groupby("City").size().reset_index(
    name="Bookings"
)

fig1 = px.bar(
    city_data,
    x="City",
    y="Bookings",
    title="Confirmed Bookings by City",
    text="Bookings"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# Marketing analysis
st.subheader("📢 Marketing Channel Performance")

channel_data = filtered.groupby(
    "Marketing_Channel"
).agg(
    Total_Leads=("Booking_ID", "count"),
    Successful_Bookings=(
        "Booking_Status",
        lambda x: (x == "Booked").sum()
    )
).reset_index()

channel_data["Conversion_Rate"] = (
    channel_data["Successful_Bookings"]
    / channel_data["Total_Leads"] * 100
)

fig2 = px.bar(
    channel_data,
    x="Marketing_Channel",
    y="Conversion_Rate",
    title="Marketing Conversion Rate (%)",
    text="Conversion_Rate"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# Property analysis
st.subheader("🏠 Property Type Analysis")

property_data = filtered[
    filtered["Booking_Status"] == "Booked"
].groupby("Property_Type").size().reset_index(
    name="Bookings"
)

fig3 = px.pie(
    property_data,
    names="Property_Type",
    values="Bookings",
    hole=0.4,
    title="Popular Accommodation Types"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# Monthly trends
st.subheader("📅 Monthly Booking Trends")

monthly = filtered[
    filtered["Booking_Status"] == "Booked"
].copy()

monthly["Month"] = (
    monthly["Booking_Date"].dt.strftime("%Y-%m")
)

monthly_data = monthly.groupby(
    "Month"
).size().reset_index(name="Bookings")

fig4 = px.line(
    monthly_data,
    x="Month",
    y="Bookings",
    markers=True,
    title="Monthly Confirmed Bookings"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# Dataset preview
st.subheader("📊 Booking Data")

st.dataframe(
    filtered,
    use_container_width=True
)

# GEMINI AI BUSINESS ANALYST

st.divider()

st.header("🤖 AI Business Analyst")

st.write(
    "Generate AI-powered business insights "
    "using your filtered booking data."
)

if st.button("✨ Generate AI Business Analysis"):

    if filtered.empty:

        st.warning("Please select at least one city.")

    else:

        booked = filtered[
            filtered["Booking_Status"] == "Booked"
        ]

        if booked.empty:

            st.warning("No confirmed bookings found for the selected cities.")

        else:

            # City performance
            city_analysis = (
                booked.groupby("City")
                .size()
                .to_dict()
            )

            # Marketing performance
            channel_analysis = filtered.groupby(
                "Marketing_Channel"
            ).agg(
                Total_Records=("Booking_ID", "count"),
                Bookings=(
                    "Booking_Status",
                    lambda x: (x == "Booked").sum()
                )
            )

            channel_analysis["Conversion_Rate"] = (
                channel_analysis["Bookings"]
                / channel_analysis["Total_Records"] * 100
            )

            # Property performance
            property_analysis = (
                booked.groupby("Property_Type")
                .size()
                .to_dict()
            )

            # Verified metrics
            ai_metrics = {
                "Total Records": len(filtered),
                "Confirmed Bookings": len(booked),
                "Average Monthly Rent": round(
                    booked["Monthly_Rent"].mean(), 2
                ),
                "City-wise Bookings": city_analysis,
                "Marketing Channel Performance":
                    channel_analysis.round(2).to_dict("index"),
                "Property Performance": property_analysis
            }

            # Generate Gemini analysis
            with st.spinner("Gemini AI is analysing your booking data..."):

                try:

                    result = generate_insights(ai_metrics)

                    st.success("AI Analysis Generated Successfully!")

                    st.subheader("📊 Business Insights")

                    st.markdown(result)

                    st.download_button(
                        "Download AI Report",
                        result,
                        file_name="AI_Business_Analysis.txt"
                    )

                except Exception:

                    st.error(
                        "Unable to generate AI analysis. "
                        "Please try again later."
                    )

conn.close()