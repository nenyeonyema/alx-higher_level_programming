-- a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city,
       AVG((temperature - 32) * 5/9) as avg_temperature_fahrenheit
FROM temperatures
GROUP BY city
ORDER BY avg_temperature_fahrenheit DESC;
