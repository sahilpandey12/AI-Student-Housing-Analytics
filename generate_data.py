import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

data = {
    "Booking_ID": range(1001, 1001 + n),

    "Booking_Date": np.random.choice(
    pd.date_range(
        start="2025-01-01",
        end="2025-12-31"
        ),
    size=n
    ),

    "City": np.random.choice(
        ["Pune", "Mumbai", "Bangalore",
         "Delhi", "Hyderabad"], n
    ),

    "University": np.random.choice(
        ["University A", "University B",
         "University C"], n
    ),

    "Property_Type": np.random.choice(
        ["Studio", "PG", "Shared Room",
         "Private Room"], n
    ),

    "Marketing_Channel": np.random.choice(
        ["Organic", "Paid Search",
         "Referral", "Social Media"], n
    ),

    "Booking_Status": np.random.choice(
        ["Booked", "Cancelled", "Enquiry"],
        n,
        p=[0.55, 0.15, 0.30]
    ),

    "Monthly_Rent": np.random.randint(
        8000, 35000, n
    ),

    "Lead_Time": np.random.randint(
        1, 60, n
    )
}

df = pd.DataFrame(data)

df.to_csv("bookings.csv", index=False)

print("Dataset created successfully!")
print(df.head())