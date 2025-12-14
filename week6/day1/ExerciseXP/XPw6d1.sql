--XP week 6 day 1

-- CREATE TABLE items(
-- 	items_id SERIAL PRIMARY KEY,
-- 	name VARCHAR(50) NOT NULL,
-- 	price BIGINT NOT NULL
-- )
-- SELECT * FROM items

-- CREATE TABLE customers(
-- 	items_id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR(50) NOT NULL,
-- 	last_name VARCHAR(100) NOT NULL
-- )

-- INSERT INTO items (name, price)
-- VALUES 
-- ('Small Desk',  100),
-- ('Large desk', 300),
-- ('Fan', 80);
-- SELECT * FROM items

-- INSERT INTO customers (first_name, last_name)
-- VALUES 
-- ('Greg', 'Jones'),
-- ('Sandra', 'Jones'),
-- ('Scott', 'Scott'),
-- ('Trevor', 'Green'),
-- ('Melanie', 'Johnson');
--SELECT * FROM customers

--ALTER TABLE customers RENAME COLUMN items_id TO customers_id

-- SELECT * FROM items
-- SELECT * FROM items WHERE price > 80 
-- SELECT * FROM items WHERE price < 300
-- SELECT * FROM customers WHERE last_name = 'Smith' --outcome is the empty table, just column names
-- SELECT * FROM customers WHERE last_name = 'Jones'
-- SELECT * FROM customers WHERE last_name != 'Scott'