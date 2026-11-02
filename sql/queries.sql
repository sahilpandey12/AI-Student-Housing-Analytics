SELECT
    City,
    COUNT(*) AS Total_Bookings
FROM bookings
WHERE Booking_Status = 'Booked'
GROUP BY City
ORDER BY Total_Bookings DESC;