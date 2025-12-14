-- CREATE TABLE actors(
-- actors_id SERIAL PRIMARY KEY,
-- first_name VARCHAR(50) NOT NULL,
-- last_name VARCHAR(100) NOT NULL,
-- birth_date DATE NOT NULL,
-- number_oscars SMALLINT	
-- )

-- SELECT * FROM actors

-- INSERT INTO actors(first_name, last_name, birth_date, number_oscars)
-- VALUES ('Matt', 'Damon', '08/10/1970', 5)
-- INSERT INTO actors(first_name, last_name, birth_date, number_oscars)
-- VALUES ('Meryl', 'Streep', '22/06/1949', 3)
-- INSERT INTO actors(first_name, last_name, birth_date, number_oscars)
-- VALUES ('Emma', 'Stone', '06/10/1988', 2)
-- INSERT INTO actors(first_name, last_name, birth_date, number_oscars)
-- VALUES  
-- 		('Kate', 'Winslet', '05/10/1975', 1),
-- 		('Leonardo', 'DiCaprio', '11/10/1974', 1),
-- 		('Brad', 'Pitt', '18/12/1963', 2);

--SELECT * FROM actors
--SELECT first_name, number_oscars FROM actors
--SELECT * FROM actors WHERE number_oscars > 2 
--SELECT * FROM actors WHERE number_oscars = 2 AND first_name = 'Brad'
--SELECT * FROM actors WHERE (number_oscars = 2 AND first_name = 'Brad')AND last_name = 'Pitt'
--SELECT * FROM actors WHERE number_oscars IS NULL
--SELECT first_name FROM actors WHERE last_name LIKE '%t'
--SELECT first_name FROM actors WHERE last_name LIKE 'D%'
--SELECT first_name FROM actors WHERE last_name ILIKE 'd%'
--SELECT * FROM actors LIMIT 4
--SELECT * FROM actors WHERE number_oscars = 3 LIMIT 1
--SELECT first_name FROM actors ORDER BY first_name DESC
--DELETE FROM actors WHERE actor_id = 6
--ALTER TABLE actors RENAME COLUMN number_oscars TO oscars
--SELECT count(*) FROM actors 
-- INSERT INTO actors(first_name, last_name, birth_date, oscars)
-- VALUES ('George', 'Clooney', '05/06/1961', NULL)


