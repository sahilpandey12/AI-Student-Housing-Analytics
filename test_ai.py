from ai_insights import generate_insights

metrics = {
    "Total Records": 1000,
    "Confirmed Bookings": 541,
    "Average Rent": 21663,

    "City-wise Bookings": {
        "Pune": 115,
        "Delhi": 113,
        "Hyderabad": 109,
        "Bangalore": 104,
        "Mumbai": 100
    },

    "Marketing Channel Performance": {
    "Paid Search": {"Bookings": 129, "Conversion Rate": 54.43},
    "Social Media": {"Bookings": 139, "Conversion Rate": 54.30},
    "Referral": {"Bookings": 131, "Conversion Rate": 53.91},
    "Organic": {"Bookings": 142, "Conversion Rate": 53.79}
    },

    "Popular Property": "Studio"
}

print("Connecting to Gemini AI...")

result = generate_insights(metrics)

print("\n========== AI BUSINESS ANALYSIS ==========\n")

print(result)