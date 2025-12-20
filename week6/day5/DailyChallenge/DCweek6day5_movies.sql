--Daily Challenge : Advanced Movie Data Analysis

--Task 1: Calculate the Average Budget Growth Rate for Each Production Company
--Calculate the average budget growth rate for each production company across all movies they have produced. Use window functions to determine the budget growth rate and then calculate the average growth rate.

-- Get all movies with their production companies and budget info
SELECT pc.company_id,
       pc.company_name,
       m.movie_id,
       m.title,
       m.budget,
       m.release_date
FROM movies.movie m
JOIN movies.movie_company mc ON m.movie_id = mc.movie_id
JOIN movies.production_company pc ON mc.company_id = pc.company_id
WHERE m.budget > 0
ORDER BY pc.company_name, m.release_date;

--  Add the previous budget using LAG() function
SELECT pc.company_id,
       pc.company_name,
       m.title,
       m.budget,
       m.release_date,
       LAG(m.budget) OVER(PARTITION BY pc.company_id ORDER BY m.release_date) AS prev_budget
FROM movies.movie m
JOIN movies.movie_company mc ON m.movie_id = mc.movie_id
JOIN movies.production_company pc ON mc.company_id = pc.company_id
WHERE m.budget > 0
ORDER BY pc.company_name, m.release_date;

-- STEP 3: Calculate the growth rate for each movie
SELECT company_name,
       title,
       budget,
       prev_budget,
       CASE 
           WHEN prev_budget > 0 THEN ((budget - prev_budget) / prev_budget) * 100
           ELSE NULL
       END AS growth_rate
FROM (
    SELECT pc.company_name,
           m.title,
           m.budget,
           LAG(m.budget) OVER(PARTITION BY pc.company_id ORDER BY m.release_date) AS prev_budget
    FROM movies.movie m
    JOIN movies.movie_company mc ON m.movie_id = mc.movie_id
    JOIN movies.production_company pc ON mc.company_id = pc.company_id
    WHERE m.budget > 0
) AS company_budgets
ORDER BY company_name;

-- STEP 4: Calculate the average growth rate per company
SELECT company_name,
       ROUND(AVG(growth_rate), 2) AS avg_budget_growth_rate_percent,
       COUNT(*) AS num_movies_with_growth,
FROM (
    SELECT company_name,
           CASE 
               WHEN prev_budget > 0 THEN ((budget - prev_budget) / prev_budget) * 100
               ELSE NULL
           END AS growth_rate
    FROM (
        SELECT pc.company_name,
               m.budget,
               LAG(m.budget) OVER(PARTITION BY pc.company_id ORDER BY m.release_date) AS prev_budget
        FROM movies.movie m
        JOIN movies.movie_company mc ON m.movie_id = mc.movie_id
        JOIN movies.production_company pc ON mc.company_id = pc.company_id
        WHERE m.budget > 0
    ) AS company_budgets
) AS growth_rates
WHERE growth_rate IS NOT NULL
GROUP BY company_name
ORDER BY avg_budget_growth_rate_percent DESC;


--Task 2: Determine the Most Consistently High-Rated Actor
--Identify the actor who has appeared in the most movies that are rated above the average rating of all movies. Use window functions and CTEs to calculate the average rating and filter the actors based on this criterion.
-- STEP 1: Find the overall average rating of all movies
SELECT AVG(vote_average) AS overall_avg_rating
FROM movies.movie;

-- STEP 2: Get all actors and their movies with ratings
SELECT p.person_id,
       p.person_name,
       m.movie_id,
       m.title,
       m.vote_average
FROM movies.movie_cast mc
JOIN movies.person p ON p.person_id = mc.person_id
JOIN movies.movie m ON m.movie_id = mc.movie_id
ORDER BY p.person_name;

-- STEP 3: Filter for movies above average rating
SELECT p.person_name,
       m.title,
       m.vote_average,
       (SELECT AVG(vote_average) FROM movies.movie) AS overall_avg
FROM movies.movie_cast mc
JOIN movies.person p ON p.person_id = mc.person_id
JOIN movies.movie m ON m.movie_id = mc.movie_id
WHERE m.vote_average > (SELECT AVG(vote_average) FROM movies.movie)
ORDER BY p.person_name;

-- STEP 4: Count high-rated movies per actor and rank them (FINAL QUERY)
SELECT person_name,
       high_rated_movie_count,
       RANK() OVER(ORDER BY high_rated_movie_count DESC) AS actor_rank
FROM (
    SELECT p.person_name,
           COUNT(m.movie_id) AS high_rated_movie_count
    FROM movies.movie_cast mc
    JOIN movies.person p ON p.person_id = mc.person_id
    JOIN movies.movie m ON m.movie_id = mc.movie_id
    WHERE m.vote_average > (SELECT AVG(vote_average) FROM movies.movie)
    GROUP BY p.person_name
) AS high_rated_counts
ORDER BY actor_rank;

--Task 3: Calculate the Rolling Average Revenue for Each Genre
--Calculate the rolling average revenue for movies within each genre, considering only the last three movies released in the genre. Use window functions with the ROWS frame specification to achieve this.
SELECT g.genre_name,
       m.title,
       m.release_date,
       m.revenue,
       AVG(m.revenue) OVER(
           PARTITION BY g.genre_name 
           ORDER BY m.release_date 
           ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
       ) AS rolling_avg_revenue
FROM movies.movie m
JOIN movies.movie_genres mg ON m.movie_id = mg.movie_id
JOIN movies.genre g ON g.genre_id = mg.genre_id
WHERE m.revenue > 0
ORDER BY g.genre_name, m.release_date;
--Task 4: Identify the Highest-Grossing Movie Series
--Identify the movie series (based on shared keywords) with the highest total revenue. Use window functions and CTEs to group movies by their series and calculate the total revenue.
-- Exercise 2: Cast and Crew Performance Analysis (continued)

-- Task 2: Identify the Top Director by Average Movie Rating
-- Use a CTE and the RANK() function to find the director with the highest average movie rating. Display the director's name and their average rating.

WITH DirectorRatings AS (
    SELECT p.person_name,
           AVG(m.vote_average) AS avg_rating
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
-- Use the SUM() function to calculate the cumulative revenue of movies acted by each actor. Display the actor's name and the cumulative revenue.

SELECT p.person_name,
       SUM(m.revenue) AS cumulative_revenue
FROM movies.movie_cast mc
JOIN movies.person p ON p.person_id = mc.person_id
JOIN movies.movie m ON m.movie_id = mc.movie_id
GROUP BY p.person_name
ORDER BY cumulative_revenue DESC;

-- Task 4: Identify the Director Whose Movies Have the Highest Total Budget
-- Use a CTE and a window function to find the director whose movies have the highest total budget. Display the director's name and the total budget.

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
       total_budget,
       RANK() OVER(ORDER BY total_budget DESC) AS budget_rank
FROM DirectorBudget
ORDER BY budget_rank;

-- Part 2
-- Task 1: Calculate the Average Budget Growth Rate for Each Production Company
-- Calculate the average budget growth rate for each production company across all movies they have produced.

WITH CompanyBudgetGrowth AS (
    SELECT pc.company_name,
           m.title,
           m.budget,
           m.release_date,
           LAG(m.budget) OVER(PARTITION BY pc.company_id ORDER BY m.release_date) AS prev_budget
    FROM movies.movie m
    JOIN movies.movie_company mc ON m.movie_id = mc.movie_id
    JOIN movies.production_company pc ON mc.company_id = pc.company_id
    WHERE m.budget > 0
),
GrowthRates AS (
    SELECT company_name,
           title,
           budget,
           prev_budget,
           CASE 
               WHEN prev_budget > 0 THEN ((budget - prev_budget) / prev_budget) * 100
               ELSE NULL
           END AS growth_rate
    FROM CompanyBudgetGrowth
)
SELECT company_name,
       AVG(growth_rate) AS avg_budget_growth_rate
FROM GrowthRates
WHERE growth_rate IS NOT NULL
GROUP BY company_name
ORDER BY avg_budget_growth_rate DESC;

-- Task 2: Determine the Most Consistently High-Rated Actor
-- Identify the actor who has appeared in the most movies that are rated above the average rating of all movies.

WITH AvgRating AS (
    SELECT AVG(vote_average) AS overall_avg_rating
    FROM movies.movie
),
HighRatedMovies AS (
    SELECT p.person_name,
           COUNT(m.movie_id) AS high_rated_movie_count
    FROM movies.movie_cast mc
    JOIN movies.person p ON p.person_id = mc.person_id
    JOIN movies.movie m ON m.movie_id = mc.movie_id
    CROSS JOIN AvgRating ar
    WHERE m.vote_average > ar.overall_avg_rating
    GROUP BY p.person_name
)
SELECT person_name,
       high_rated_movie_count,
       RANK() OVER(ORDER BY high_rated_movie_count DESC) AS actor_rank
FROM HighRatedMovies
ORDER BY actor_rank;

-- Task 3: Calculate the Rolling Average Revenue for Each Genre
-- Calculate the rolling average revenue for movies within each genre, considering only the last three movies released.

SELECT g.genre_name,
       m.title,
       m.release_date,
       m.revenue,
       AVG(m.revenue) OVER(
           PARTITION BY g.genre_name 
           ORDER BY m.release_date 
           ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
       ) AS rolling_avg_revenue
FROM movies.movie m
JOIN movies.movie_genres mg ON m.movie_id = mg.movie_id
JOIN movies.genre g ON g.genre_id = mg.genre_id
WHERE m.revenue > 0
ORDER BY g.genre_name, m.release_date;

-- Task 4: Identify the Highest-Grossing Movie Series
-- Identify the movie series (based on shared keywords) with the highest total revenue.

WITH MovieSeries AS (
    SELECT mk.keyword_id,
           k.keyword_name,
           m.title,
           m.revenue,
           COUNT(m.movie_id) OVER(PARTITION BY mk.keyword_id) AS movies_in_series,
           SUM(m.revenue) OVER(PARTITION BY mk.keyword_id) AS total_series_revenue
    FROM movies.movie_keywords mk
    JOIN movies.keyword k ON k.keyword_id = mk.keyword_id
    JOIN movies.movie m ON m.movie_id = mk.movie_id
    WHERE m.revenue > 0
)
SELECT DISTINCT keyword_name AS series_name,
       movies_in_series,
       total_series_revenue,
       RANK() OVER(ORDER BY total_series_revenue DESC) AS series_rank
FROM MovieSeries
WHERE movies_in_series > 1  -- Only consider actual series with multiple movies
ORDER BY series_rank
LIMIT 10;
