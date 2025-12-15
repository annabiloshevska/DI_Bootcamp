--Exercises XP week 6 day 2(PART 1)
--All items, ordered by price (lowest to highest)
--SELECT * FROM items ORDER BY price 

--Items with a price above 80 (80 included),
--ordered by price (highest to lowest).
-- SELECT * FROM items 
-- WHERE price > 80
-- ORDER BY price DESC

--The first 3 customers in alphabetical order of the first name (A-Z)
-- exclude the primary key column from the results.

-- SELECT name, price FROM items 
-- ORDER BY name 

--All last names (no other columns!), 
--in reverse alphabeticalorder (Z-A)

-- SELECT name FROM items
-- ORDER BY name DESC
