--Exercise 1: DVD Rental
-- Get a list of all the languages, from the language table.
SELECT language_id, name FROM language;

-- Get a list of all films joined with their languages – select the following details : film title, description, and language name.
SELECT f.title, f.description, l.name as language
FROM film AS f
JOIN language AS l
  ON f.language_id = l.language_id;

-- Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.
SELECT f.title, f.description, l.name as language
FROM film AS f
FULL JOIN language AS l
  ON f.language_id = l.language_id;
  
-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.
CREATE TABLE new_film (
	new_film_id SERIAL PRIMARY KEY,
	new_film_name VARCHAR(100) NOT NULL);
INSERT INTO new_film (new_film_name)
VALUES
('Pirates of the Caribbean'),
('Lord of the rings'),
('Titanic');

-- Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.
CREATE TABLE customer_review (
    review_id    SERIAL PRIMARY KEY,
    film_id      INTEGER NOT NULL,
    language_id  INTEGER NOT NULL,
    title        VARCHAR(255) NOT NULL,
    score        INTEGER CHECK (score BETWEEN 1 AND 10),
    review_text  TEXT,
    last_update  TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT fk_review_film
        FOREIGN KEY (film_id)
        REFERENCES new_film (new_film_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_review_language
        FOREIGN KEY (language_id)
        REFERENCES language (language_id)
);

-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
SELECT * FROM new_film;
SELECT * FROM language;

INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES
    (1, 1, 'Pirates of the Caribbean', 9, 'Epic pirate adventure.'),
    (2, 1, 'Titanic', 9, 'Emotional classic.');
	
-- Delete a film that has a review from the new_film table, what happens to the customer_review table?
DELETE FROM new_film
WHERE new_film_id = 1;
SELECT * FROM customer_review;
--Because of ON DELETE CASCADE on customer_review(film_id), all reviews for film_id = 1 are automatically deleted from customer_review.

-- Exercise 2 : DVD Rental

-- Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film
SET language_id = 2
WHERE film_id IN (1,2,3);
SELECT * FROM film

-- Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
-- In dvdrental, customer has foreign keys to: store via store_id and to address via address_id
-- That means when inserting into customer, the store_id used must already exist in store.and the address_id must already exist in address.

-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
DROP TABLE customer_review
-- Easy because we used CASDADE creating it

-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
SELECT COUNT(*) AS outstanding_rentals
FROM rental
WHERE return_date IS NULL

-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
SELECT f.film_id,
       f.title,
       f.replacement_cost,
       r.rental_id,
       r.rental_date
FROM rental AS r
JOIN inventory AS i
  ON r.inventory_id = i.inventory_id
JOIN film AS f
  ON i.film_id = f.film_id
WHERE r.return_date IS NULL
ORDER BY f.replacement_cost DESC
LIMIT 30;

-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
SELECT f.film_id, f.title, f.description
FROM film AS f
JOIN film_actor AS fa
	ON f.film_id = fa.film_id
JOIN actor AS a
	ON a.actor_id = fa.actor_id
WHERE a.first_name = 'PENELOPE'
  AND a.last_name  = 'MONROE'
  AND f.description ILIKE '%sumo%';

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.
SELECT DISTINCT f.film_id,
       f.title,
       f.length,
       f.rating
FROM film AS f
JOIN film_category AS fc
  ON f.film_id = fc.film_id
JOIN category AS c
  ON fc.category_id = c.category_id
WHERE c.name = 'Documentary'
  AND f.length < 60
  AND f.rating = 'R';
  
-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
SELECT DISTINCT f.film_id,
       f.title,
       r.rental_date,
       r.return_date,
       p.amount
FROM customer AS c
JOIN rental   AS r ON c.customer_id = r.customer_id
JOIN payment  AS p ON r.rental_id   = p.rental_id
JOIN inventory AS i ON r.inventory_id = i.inventory_id
JOIN film      AS f ON i.film_id      = f.film_id
WHERE c.first_name = 'MATTHEW'
  AND c.last_name  = 'MAHAN'
  AND p.amount > 4.00
  AND r.return_date >= DATE '2005-07-28'
  AND r.return_date <  DATE '2005-08-02';

-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
SELECT DISTINCT f.film_id,
       f.title,
       f.description,
       f.replacement_cost
FROM customer  AS c
JOIN rental    AS r ON c.customer_id = r.customer_id
JOIN inventory AS i ON r.inventory_id = i.inventory_id
JOIN film      AS f ON i.film_id      = f.film_id
WHERE c.first_name = 'MATTHEW'
  AND c.last_name  = 'MAHAN'
  AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
  AND f.replacement_cost > 25
ORDER BY f.replacement_cost DESC;