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

