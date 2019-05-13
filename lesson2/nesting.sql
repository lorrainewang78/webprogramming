SELECT flight_id FROM passengers
GROUP BY flight_id HAVING COUNT(*) > 1;

SELECT * FROM flights WHERE id
IN (SELECT flight_id FROM passengers
    GROUP BY flight_id HAVING COUNT(*) > 1);
