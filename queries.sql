-- write your queries here
--1--
SELECT * FROM owners o
FULL OUTER JOIN vehicles v
ON o.id = v.owner_id;


--2--
SELECT o.first_name, o.last_name, COUNT(*) 
FROM owners o 
JOIN vehicles v
ON o.id = v.owner_id
GROUP BY o.first_name, o.last_name 
ORDER BY first_name;


--3--
SELECT o.first_name, o.last_name, COUNT(*), CEILING(AVG(v.price))  
FROM owners o 
JOIN vehicles v 
ON o.id = v.owner_id
GROUP BY o.first_name, o.last_name
HAVING COUNT(*) > 1 AND  AVG(v.price) > 10000
ORDER BY first_name DESC;