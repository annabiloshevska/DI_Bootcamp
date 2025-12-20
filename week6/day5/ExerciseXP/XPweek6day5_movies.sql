-- Exercise 1: Movie Rankings and Analysis

-- Task 1: Rank Movies by Popularity within Each Genre
-- Use the RANK() function to rank movies by their popularity within each genre. Display the genre name, movie title, and their rank based on popularity.

SELECT * FROM movies.movie
SELECT * FROM movies.movie_genres

SELECT mg.genre_id, 
	   g.genre_name, 
	   m.title,
	   m.popularity,
	   RANK() OVER(PARTITION BY g.genre_name ORDER BY m.popularity DESC) AS rank_by_popularity 
FROM movies.movie m
JOIN movies.movie_genres mg 
	ON m.movie_id = mg.movie_id
JOIN movies.genre g 
	ON g.genre_id = mg.genre_id;
	
-- Task 2: Identify the Top 3 Movies by Revenue within Each Production Company
-- Use the NTILE() function to divide the movies produced by each production company into quartiles based on revenue. Display the company name, movie title, revenue, and quartile.
SELECT pc.company_name,
	   m.title,
	   m.revenue,
	   NTILE(4) OVER(PARTITION BY pc.company_id ORDER BY m.revenue DESC) AS quartile
FROM movies.movie m
JOIN movies.movie_company mc
	ON m.movie_id = mc.movie_id
JOIN movies.production_company pc 
	ON mc.company_id = pc.company_id;

-- Task 3: Calculate the Running Total of Movie Budgets for Each Genre
-- Use the SUM() function with the ROWS frame specification to calculate the running total of movie budgets within each genre. Display the genre name, movie title, budget, and running total budget.
SELECT COUNT(*) FROM movies.movie_genres;
SELECT g.genre_name, 
	   m.title,
	   m.budget,
	   SUM(m.budget) OVER(PARTITION BY g.genre_name ORDER BY m.title  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS run_total_budget
FROM movies.movie m
JOIN movies.movie_genres mg 
	ON m.movie_id = mg.movie_id
JOIN movies.genre g 
	ON g.genre_id = mg.genre_id
ORDER BY g.genre_name, m.movie_id;

-- Task 4: Identify the Most Recent Movie for Each Genre
-- Use the FIRST_VALUE() function to find the most recent movie within each genre based on the release date. Display the genre name, movie title, and release date.
SELECT DISTINCT g.genre_name,
	   FIRST_VALUE(m.release_date) OVER(PARTITION BY g.genre_name ORDER BY m.release_date DESC) AS first_release,
	   FIRST_VALUE(m.title) OVER(PARTITION BY g.genre_name ORDER BY m.release_date DESC) AS most_recent
FROM movies.movie m	   
JOIN movies.movie_genres mg 
	ON m.movie_id = mg.movie_id
JOIN movies.genre g 
	ON g.genre_id = mg.genre_id
ORDER BY g.genre_name;

-- Exercise 2: Cast and Crew Performance Analysis


-- Task 1: Rank Actors by Their Appearance in Movies
-- Use the DENSE_RANK() function to rank actors based on the number of movies they have appeared in. Display the actor’s name and their rank.
SELECT * FROM movies.movie_cast
SELECT * FROM movies.person

SELECT p.person_name,
	   COUNT(mc.movie_id) AS num_movie_appeared,
	   DENSE_RANK() OVER(ORDER BY COUNT(mc.movie_id) DESC) AS actor_rank
FROM movies.movie_crew mc
JOIN movies.person p ON p.person_id = mc.person_id
JOIN movies.department d ON d.department_id = mc.department_id
WHERE d.department_name = 'Actors'
GROUP BY p.person_name
ORDER BY actor_rank

-- Task 2: Identify the Top Director by Average Movie Rating
-- Use a CTE and the RANK() function to find the director with the highest average movie rating. Display the director’s name and their average rating.
SELECT * FROM movies.department

WITH DirectorRatings AS (
		SELECT p.person_name,
        ROUND(AVG(m.vote_average)) AS avg_rating
    FROM movies.movie_crew mc
    JOIN movies.person p ON p.person_id = mc.person_id
    JOIN movies.movie m ON m.movie_id = mc.movie_id
    JOIN movies.department d ON d.department_id = mc.department_id
    WHERE d.department_name = 'Directing'
    GROUP BY p.person_name
)
SELECT person_name,
       avg_rating,
       RANK() OVER(ORDER BY avg_rating DESC) AS director_rank
FROM DirectorRatings
ORDER BY director_rank;

-- Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor
-- Use the SUM() function to calculate the cumulative revenue of movies acted by each actor. Display the actor’s name and the cumulative revenue.

SELECT p.person_name,
       SUM(m.revenue) AS cumulative_revenue
FROM movies.movie_cast mc
JOIN movies.person p ON p.person_id = mc.person_id
JOIN movies.movie m ON m.movie_id = mc.movie_id
GROUP BY p.person_name
ORDER BY cumulative_revenue DESC;

-- Task 4: Identify the Director Whose Movies Have the Highest Total Budget
-- Use a CTE and a window function to find the director whose movies have the highest total budget. Display the director’s name and the total budget.

WITH DirectorBudget AS (
		SELECT p.person_name,
        SUM(m.budget) AS total_budget
    FROM movies.movie_crew mc
    JOIN movies.person p ON p.person_id = mc.person_id
    JOIN movies.movie m ON m.movie_id = mc.movie_id
    JOIN movies.department d ON d.department_id = mc.department_id
    WHERE d.department_name = 'Directing'
    GROUP BY p.person_name
)
SELECT person_name,
	   total_budget
FROM DirectorBudget	   
ORDER BY total_budget DESC