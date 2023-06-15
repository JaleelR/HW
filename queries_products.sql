-- Comments in SQL Start with dash-dash --
--PART 3--
--1--
INSERT INTO products
  (name, price, can_be_returned)
VALUES
  ('chair', 44.00, FALSE);



--2--
INSERT INTO products 
(name, price, can_be_returned)
VALUES
 ('stool', 25.99, TRUE);


--3--
INSERT INTO products 
(name, price, can_be_returned)
VALUES 
('table', 124.00, FALSE);



--4--
SELECT * FROM products;



--5--
SELECT name FROM products;



--6--
SELECT name, price  FROM products;


--7--
INSERT INTO products 
(name, price, can_be_returned)
VALUES
('Fancy mirror', 200.99, TRUE);




--8--
SELECT * FROM products WHERE can_be_returned = TRUE;



--9--
SELECT * FROM products WHERE price < 44.00;



--10--
SELECT * FROM products WHERE price BETWEEN 22.50 AND 99.99 



--11--
UPDATE products SET price = price - 20; 

--12--
DELETE FROM products WHERE price < 25;


--13--
UPDATE products SET price = price + 20;



--14--
UPDATE products SET can_be_returned = TRUE;
SELECT * FROM products;







--part 4--
--1--


SELECT app_name FROM analytics 
WHERE ID = 1880;


--2--
SELECT id, app_name FROM analytics 
WHERE last_updated = '2018-08-01';


--3--
SELECT category, COUNT(app_name) FROM analytics 
GROUP BY category;



--4--
SELECT app_name, reviews FROM analytics 
GROUP BY app_name, reviews ORDER BY reviews DESC LIMIT 5;



--5--
SELECT app_name, reviews FROM analytics
 WHERE rating >= 4.8 GROUP by app_name, reviews 
 ORDER BY reviews DESC LIMIT 1;


--6--
SELECT category, AVG(rating) FROM analytics
GROUP BY category 
ORDER BY AVG DESC;


--7--
SELECT app_name, price, rating FROM analytics 
WHERE rating < 3 GROUP BY app_name, price, rating
ORDER BY price 
DESC LIMIT 1;



--8--
SELECT * FROM analytics
WHERE min_installs <= 50 AND rating > 0
ORDER BY rating DESC;



--9--
SELECT app_name FROM analytics 



--10--
SELECT app_name FROM analytics 
WHERE rating < 3 AND reviews >= 1000;



--11--
SELECT * FROM analytics 
WHERE price BETWEEN .10 AND 1
 LIMIT 10;



--12--
 SELECT app_name, MAX(last_updated) FROM analytics 
 GROUP BY app_name
 ORDER BY MAX
 LIMIT 1;


--13--
 SELECT  * FROM analytics
 WHERE price = (SELECT MAX(price) FROM analytics)

--14--
SELECT SUM(reviews)  FROM analytics;

--15
SELECT category, COUNT(app_name) FROM analytics 
GROUP BY category
HAVING COUNT(app_name) > 300;

--16--
SELECT  app_name, reviews, min_installs,  MAX(min_installs / reviews) FROM analytics 
WHERE min_installs >= 100000
GROUP BY app_name, reviews, min_installs
ORDER BY MAX DESC
LIMIT 1;