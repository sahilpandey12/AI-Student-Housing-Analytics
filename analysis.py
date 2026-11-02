import pandas as pd
import sqlite3

# Load dataset
df = pd.read_csv("bookings.csv")

# Connect database
conn = sqlite3.connect("bookings.db")

df.to_sql(
    "bookings",
    conn,
    if_exists="replace",
    index=False
)

print("\nDATABASE CREATED SUCCESSFULLY!")

# QUERY 1: City-wise bookings
q1 = """
SELECT City,
COUNT(*) AS Total_Bookings
FROM bookings
WHERE Booking_Status = 'Booked'
GROUP BY City
ORDER BY Total_Bookings DESC;
"""

print("\n1. CITY-WISE BOOKINGS")
print(pd.read_sql_query(q1, conn))


# QUERY 2: Marketing channel conversion
q2 = """
SELECT
Marketing_Channel,
COUNT(*) AS Total_Leads,
SUM(CASE WHEN Booking_Status = 'Booked'
THEN 1 ELSE 0 END) AS Successful_Bookings,

ROUND(
100.0 * SUM(CASE WHEN Booking_Status = 'Booked'
THEN 1 ELSE 0 END) / COUNT(*), 2
) AS Conversion_Rate

FROM bookings
GROUP BY Marketing_Channel
ORDER BY Conversion_Rate DESC;
"""

print("\n2. MARKETING CHANNEL PERFORMANCE")
print(pd.read_sql_query(q2, conn))


# QUERY 3: Average rent by city
q3 = """
SELECT
City,
ROUND(AVG(Monthly_Rent), 2) AS Average_Rent
FROM bookings
WHERE Booking_Status = 'Booked'
GROUP BY City
ORDER BY Average_Rent DESC;
"""

print("\n3. AVERAGE RENT BY CITY")
print(pd.read_sql_query(q3, conn))


# QUERY 4: Popular property types
q4 = """
SELECT
Property_Type,
COUNT(*) AS Total_Bookings
FROM bookings
WHERE Booking_Status = 'Booked'
GROUP BY Property_Type
ORDER BY Total_Bookings DESC;
"""

print("\n4. PROPERTY TYPE PERFORMANCE")
print(pd.read_sql_query(q4, conn))


# QUERY 5: Monthly booking trends
q5 = """
SELECT
strftime('%Y-%m', Booking_Date) AS Month,
COUNT(*) AS Total_Bookings
FROM bookings
WHERE Booking_Status = 'Booked'
GROUP BY Month
ORDER BY Month;
"""

print("\n5. MONTHLY BOOKING TRENDS")
print(pd.read_sql_query(q5, conn))


conn.close()