# SOURCE:
# poorsql.com --> use to auto indentation

# >>>>>>>>>>>>>>>>> CREATE NEW DATABASE <<<<<<<<<<<<<<<
CREATE DATABASE dvdrental;

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>> SECTION 2: STATEMENT FUNDAMENTAL <<<<<<<<<<<<

###### SELECT ###############

SELECT COLUMN1, COLUMN2, COLUMN3 FROM table_name; # select specific column
SELECT * FROM table_name; # select the entire table: all cols

SELECT * FROM actor;
SELECT first_name, last_name FROM actor;

SELECT DISTINCT column1, column2 FROM table_name; # SELECT DISTINCT
SELECT DISTINCT rental_rate FROM film;

##### QUERY PARTICULAR ROWS - WHERE #####
SELECT column1, column2, column3, ...
FROM table_name
WHERE conditions; # = > < >= <= != AND OR

SELECT last_name, first_name
FROM customer
WHERE first_name = 'Jamie' AND last_name = 'Rice';

SELECT customer_id, amount, payment_date
FROM payment
WHERE amount <= 1 OR amount >= 8;

SELECT amount, payment_date
FROM payment
WHERE amount != 4.99;

SELECT amount, payment_date
FROM payment
WHERE amount = 4.99 AND amount = 1.99; # return EMPTY!

SELECT amount, payment_date
FROM payment
WHERE amount = 4.99 OR amount = 1.99; # return BOTH!

SELECT phone FROM address
WHERE address = "237 CORRIE CRESCENT";

###### COUNT ###############
SELECT COUNT(column) FROM table_name;
SELECT COUNT(DISTINCT column) FROM table_name;

SELECT COUNT(*) FROM payment; # count how many rows
SELECT COUNT(DISTINCT amount) FROM payment; # COUNT unique values under amount column FROM payment table

###### LIMIT: limit number of rows you get back ###############
SELECT * FROM customer LIMIT 5; # get back 6 rows


###### ORDER BY: sort the result ###############
SELECT column1, column2
FROM table_name
ORDER BY column1 ASC/DESC; # work with both numerical and alphabetical order. ASC is default

SELECT first_name, last_name FROM customer
ORDER BY first_name ASC; # A to Z

SELECT first_name, last_name FROM customer
ORDER BY first_name ASC, last_name DESC; # MULITPLE "ORDER BY" separated by ","

SELECT first_name
FROM customer
ORDER BY last_name DESC
LIMIT 10;

# get titles of the movie with film id 1 to 5
SELECT film_id, title, year_release FROM film
ORDER BY id ASC
LIMIT 5;

###### BETWEEN - NOT BETWEEN ###############
WHERE value BETWEEN low AND high; # or value >= low AND value <= high

SELECT customer_id, amount FROM payment
WHERE amount BETWEEN 8 AND 9;

# Check range of dates:
SELECT amount, payment_date FROM payment
WHERE payment_date BETWEEN '2007-02-07' AND '2007-02-15';

###### IN - NOT IN ###############
WHERE value IN (value1, value2, ...);
# using SUB QUERY
value IN (SELECT value FROM table_name);

SELECT customer_id, rental_id, return_date
FROM rental
WHERE customer_id NOT IN (1,2,3)
ORDER BY return_date DESC;

###### LIKE - NOT LIKE with "%" and "_": NOT EXACT SEARCH ###############
# USING "%" for PATTERN SEARCH
SELECT first_name, last_name
FROM customer
WHERE first_name LIKE 'Jen%'; # search for first name that STARTS with Jen. could be Jenny, Jenna, etc

SELECT first_name, last_name
FROM customer
WHERE first_name LIKE '%y'; # search for first name that ENDS with y. Jenny, Johny

SELECT first_name, last_name
FROM customer
WHERE first_name LIKE '%er%'; # search for first name that has "er" in BETWEEN or ENDS or STARTS. Jennif"er", "Er"rosi, T"er"isa, etc

# USING "_" for SINGLE CHARACTER SEARCH
SELECT first_name, last_name
FROM customer
WHERE first_name LIKE '_her%'; # one single character in front of "her%" replaced by "_". Return: "Cheryl", "Theresa", "Sherry", etc

# CASE INsensitiviy with "ILIKE"
SELECT first_name, last_name
FROM customer
WHERE first_name ILIKE 'BAR%'; # return "Barcelona" --> REGARDLESS of LOWER/UPPER case

## Some examples:
SELECT COUNT(amount) FROM payment
WHERE amount > 5;

# first name start with P
SELECT COUNT(*) FROM actor
WHERE first_name LIKE "P%";

# Find all the customer emails that start with "J" and are from gmail.com.
SELECT Email
FROM Customers
WHERE Email LIKE 'J%gmail%'

# how many unique district
SELECT COUNT(DSTINCT(district)) from address
# Get the names of the distinct district
SELECT DSTINCT(district) from address;

# how many films have a rating of R AND cost BETWEEN 5 and 15
SELECT COUNT(*) FROM film
WHERE rating = "R"
AND replacement_cost BETWEEN 5 AND 15;

# How many films have the word "Beau" in the title
SELECT COUNT(*) FROM film
WHERE title LIKE "%Beau%";

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>> SECTION 3: AVG, MIN/MAX, SUM, GROUP BY, HAVING <<<<<<<<<<<<

## AVG with ROUND:
SELECT ROUND(AVG(amount), 2) FROM payment; # ROUND the AVG to 2 dec places

## MIN/MAX/SUM
SELECT MIN/MAX/SUM(amount) FROM payment
ORDER BY amount DESC;

## GROUP BY:
SELECT column1, agg_function(column2), column3
FROM table_name
GROUP BY column3;

SELECT customer_id, MIN(amount), AVG(amount), MAX(amount), SUM(amount), COUNT(amount)
FROM payment
GROUP BY customer_id
ORDER BY SUM(amount) DESC;

SELECT rating, COUNT(rating)
FROM film
GROUP BY rating;

## HAVING: using as WHERE in conjunction with GROUP BY. called AFTER the GROUP BY
SELECT customer_id, MIN(amount), AVG(amount), MAX(amount), SUM(amount), COUNT(amount)
FROM payment
GROUP BY customer_id
ORDER BY SUM(amount) DESC
HAVING SUM(amount) > 300;
# NOTE** WHERE only works on rows basis and does not work with GROUP so use HAVING
# REMEMBER: WHERE BEFORE GROUP BY and HAVING AFTER GROUP BY
SELECT customer_id, COUNT(*) as orders
FROM Orders
GROUP BY customer_id
HAVING orders >= 2;

# use ORDER BY to make out put alphabetically sorted --> increase readability
SELECT SupplierID, COUNT(*) as Num_Prod
FROM Products
WHERE UnitPrice >= 4
GROUP BY SupplierID
HAVING Num_Prod >= 2
ORDER BY SupplierID;

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>> SECTION 4 : JOIN, AS, UNION <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

## AS: using to make an ALIAS of a column
SELECT customer_id, SUM(amount) AS total_spent
FROM payment
GROUP BY customer_id
ORDER BY total_spent;

SELECT vendor_name, product_name, product_price
FROM Vendors AS v, Products AS p
WHERE v.vendor_id = p.vendor_id;

# IMPORTANT: professionally, RELACE("AS", " ") should give the same result

## JOIN: INNER JOIN, FULL OUTER JOIN, LEFT OUTER JOIN (2 TYPES), CROSS JOIN (No Venn Diagram)
# References:https://blog.codinghorror.com/a-visual-explanation-of-sql-joins/

SELECT *
FROM TableA
LEFT OUTER JOIN TableB
ON TableA.id = TableB.id; # Join on primary and foreign key

# Primary Key and Foreigne Key (a primary from another table):
# TableA: user_id (primary: pkA), full name
# TableB: product_id (primary: pkB), cost, user_id (foreign key from TableA: fkA)

SELECT A.pkA, A.c1, B.pkB, B.c2 # call a column from a specific table
# NOTE: if a column is uniquely defined in a table then just call the column
# WITHOUT using table.column_name method
FROM A # Always go FROM the MAIN table
INNER JOIN B # By default, JOIN using INNER JOIN
ON A.pkA = B.fkA;

# Check to see how many of each film title is in store 1:
# JOIN 2 tables
SELECT title, COUNT(title) as num_title
FROM inventory # Main table
# We can also use AS for JOIN: to make it simple in case of long db name
INNER JOIN film AS movie on inventory.film_id = movie.film_id
WHERE store_id = 1
GROUP BY title;


# Join more than 2 tables with short form names
# o = Orders; c = Customers; e = Employees
SELECT o.OrderID, c.CompanyName, e.Lastname
FROM ((Orders o INNER JOIN Customers c ON o.CustomerId = c.CustomerId)
INNER JOIN Employees e ON o.CustomerId = e.CustomerId);
# DO NOT FUCK UP THE BRACKETS!!!!!

## UNION: Combine 2 "same structured" (same col data struct, # of cols) dataframes
# examples: UNION/CONCAT quarterly sales together
# Note: UNION will remove duplicate rows
# TO SHOW DUPLICATE RESULT AS WELL: use "UNION ALL"

SELECT column1, column2
FROM table_name1
UNION # or UNION ALL
SELECT column1, column2
FROM table_name2;

# map relationship between customers and suppliers
SELECT City, Country
FROM Customers
WHERE Country = 'Germany' # NOTE: ORDER OF COLS ARE SAME
UNION
SELECT City, Country
FROM Suppliers
WHERE Country='Germany'
ORDER BY City;

## TODO: review the JOIN Challenge

# >>>>>>> SUB QUERIES <<<<<<<<<<<<<<<<<<<<<<<<<
# start with the inner query becuase thats how DBMS operates
# NOTES: subquery only works with 1 single col at a time

SELECT CustomerId, CompanyName
FROM Customers
WHERE CustomerId IN (SELECT
      CustomerId
      FROM Orders
      WHERE Freight > 100);

# HARD ONE:
# customers.customer_name | customers.customer_state | total(orders.order)
SELECT customer_name, customer_state,
      (SELECT COUNT(*)
        FROM Orders
        WHERE Orders.customer_id = Customers.customer_id) AS total_orders
FROM Customers
ORDER BY customer_name DESC;

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>> SECTION 5 : ADVANCED SQL COMMANDS <<<<<<<<<<<<<<<<<<<<<<<<<

-- Advanced SQL Commands
-- In this section of the course we will go over a few topics that will be
-- useful for you to know. These topics are:

-- Mathematical Functions
-- Timestamps and the extract function
-- String Functions and Operators
-- SubQuery
-- Self-Join
-- -----------------------------------

-- 1 -- Timestamp

# >>>>>> WHY AND WHEN TO USE SELF JOIN <<<<<<<<<<<
# https://stackoverflow.com/questions/3362038/what-is-self-join-and-when-would-you-use-it#:~:text=You%20use%20a%20self%20join,boss%20of%20the%20current%20employee.&text=It's%20basically%20used%20where%20there,employees.

select e1.EmployeeID,
    e1.FirstName,
    e1.LastName,
    e1.SupervisorID,
    e2.FirstName as SupervisorFirstName,
    e2.LastName as SupervisorLastName
from Employee e1
left outer join Employee e2 on e1.SupervisorID = e2.EmployeeID


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>> SECTION 6 : CREATING TABLES <<<<<<<<<<<<<<<<<<<<<<<<<

CREATE TABLE account(
user_id serial PRIMARY KEY,
username VARCHAR (50) UNIQUE NOT NULL,
password VARCHAR (50) NOT NULL,
email VARCHAR (355) UNIQUE NOT NULL,
created_on TIMESTAMP NOT NULL,
last_login TIMESTAMP
);

CREATE TABLE role(
role_id serial PRIMARY KEY,
role_name VARCHAR (255) UNIQUE NOT NULL
)
INHERITS existing_table;


CREATE TABLE account_role
(
  user_id integer NOT NULL,
  role_id integer NOT NULL,
  grant_date timestamp without time zone,
  PRIMARY KEY (user_id, role_id),
  CONSTRAINT account_role_role_id_fkey FOREIGN KEY (role_id)
      REFERENCES role (role_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT account_role_user_id_fkey FOREIGN KEY (user_id)
      REFERENCES account (user_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)

# >>>>>>> INSERT TABLES <<<<<<<<<<<<<<<<<<<<<<<<<
INSERT INTO role (
	role_id,
	role_name
) VALUES (
	1,
	'data scientist'
);
