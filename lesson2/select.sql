SELECT * FROM flights;
SELECT origin, destination FROM flights;
SELECT * FROM flights WHERE id = 3;
SELECT * FROM flights WHERE origin = 'New York';
SELECT * FROM flights WHERE duration > 500;

SELECT * FROM flights
WHERE destination = 'Paris' AND duration > 500;

SELECT * FROM flights
WHERE destination = 'Paris' OR duration > 500;

SELECT AVG(duration) FROM flights;

SELECT AVG(duration) FROM flights WHERE origin = 'New York';


SELECT COUNT(*) FROM flights;

SELECT COUNT(*) FROM flights WHERE origin = 'New York';

SELECT COUNT(*) FROM flights WHERE origin = 'Moscow';

SELECT MIN(duration) FROM flights;

SELECT * FROM flights WHERE duration = 245;

SELECT * FROM flights
WHERE origin IN ('New York', 'Lima');

SELECT * FROM flights
WHERE origin LIKE '%a%';
