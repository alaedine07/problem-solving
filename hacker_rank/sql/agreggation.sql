/* count function */ 
SELECT COUNT(name)
FROM CITY 
WHERE population > 100000 ; 
/* sum function */ 
SELECT SUM(population) 
FROM CITY 
WHERE DISTRICT = 'California';
/* AVG funciton */ 
SELECT AVG(population) 
FROM CITY 
WHERE DISTRICT = 'California' ; 
/* FLOOR */ 
SELECT FLOOR(AVG(population))
FROM CITY ; 
/* japan population */ 
SELECT SUM(population)
FROM CITY 
WHERE COUNTRYCODE = 'JPN' ; 
/*min and max */
SELECT MAX(population) - MIN(population) 
FROM CITY ;
/* the blunder */  
SELECT
CEIL(AVG(Salary) - AVG(REPLACE(SALARY, '0', '')))
FROM EMPLOYEES;
/* top earners */ 
SELECT MONTHS * SALARY AS EARNINGS, COUNT(*)
FROM EMPLOYEE
GROUP BY EARNINGS DESC
LIMIT 1;
/*weather obeservation 2 */ 
SELECT round(SUM(LAT_N),2), ROUND(SUM(LONG_W), 2)
FROM STATION;
/* Weather observation 3 */ 
SELECT SUM(LAT_N) 
FROM STATION
WHERE LAT_N > 38.7880 AND LAT_N < 137.2345 ; 
/* weather observation 14 */ 
SELECT TRUNCATE(max(LAT_N),4)
FROM STATION
WHERE LAT_N < 137.2345;
/* weather 16 */ 
SELECT ROUND(MIN(LAT_N), 4)
FROM STATION
WHERE LAT_N > 38.7780;
/* Weather observation 18 */
SELECT ROUND(LONG_W, 4)
FROM STATION
WHERE LAT_N > 38.7780
ORDER BY LAT_N
LIMIT 1;