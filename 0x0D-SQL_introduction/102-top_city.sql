--  a script that displays the top 3 of cities temperature
-- during July and August ordered by temperature (descending)
SELECT city,
       MAX(value) as max_temperature
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY max_temperature DESC
LIMIT 3;
