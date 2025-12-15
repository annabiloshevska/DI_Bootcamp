CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
)

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar')

SELECT * FROM FirstTab

CREATE TABLE SecondTab (
    id integer 
)

INSERT INTO SecondTab VALUES
(5),
(NULL)


SELECT * FROM SecondTab

SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
--Answer: 0
--The subquery returns NULL. Any NOT IN (NULL) comparison is unknown, so no rows match.

SELECT COUNT(*) 
	FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
--Answer: 2
--The subquery returns '5'. Rows with id=6 and id=7 qualify. id=5 is excluded, id=NULL is excluded because comparisons with NULL are unknown.

SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
--Answer: 0
--The subquery returns '5', 'NULL'. Because the set includes NULL, every NOT IN comparison becomes unknown, so no rows match.

SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
--Answer: 2
--The subquery returns '5'. Rows with id=6 and id=7 qualify. id=5 is excluded, id=NULL excluded because of NULL comparison.

	