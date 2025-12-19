-- Exercise 1: Complex Subquery Analysis

-- Task 1: Find the average age of competitors who have won at least one medal, grouped by the type of medal they won. Use a correlated subquery to achieve this.
-- find average age 
-- who won the medal
-- group by medal type

SELECT m.medal_name,
       AVG(
         (
           SELECT gc.age
           FROM games_competitor gc
           WHERE gc.id = ce.competitor_id
         )
       ) AS avg_age
FROM competitor_event ce
JOIN medal m ON ce.medal_id = m.id
WHERE medal_name <> 'NA'
GROUP BY m.medal_name;

-- Task 2: Identify the top 5 regions with the highest number of unique competitors who have participated in more than 3 different events. Use nested subqueries to filter and aggregate the data.
--comp who participated in more than 3 different events
--comp regions
--COUNT competitors in the regions
--show top 5 regions                              
SELECT r.region_name, 
		COUNT(*) as unique_competitors
FROM noc_region r
JOIN person_region pr ON pr.region_id = r.id
WHERE pr.person_id IN (SELECT competitor_id
      					FROM competitor_event
      					GROUP BY competitor_id
      					HAVING COUNT(DISTINCT event_id > 3))
group by r.region_name
Order by unique_competitors DESC
LIMIT 5;  


-- Task 3: Create a temporary table to store the total number of medals won by each competitor and filter to show only those who have won more than 2 medals. Use subqueries to aggregate the data.
CREATE TEMP TABLE competitor_medals AS
SELECT competitor_id,
       COUNT(medal_id) AS medal_count
FROM competitor_event
WHERE medal_id <> 4
GROUP BY competitor_id;

SELECT *
FROM competitor_medals
WHERE medal_count > 2;

-- Task 4: Use a subquery within a DELETE statement to remove records of competitors who have not won any medals from a temporary table created for analysis.

DELETE FROM competitor_medals
WHERE competitor_id IN (
    SELECT competitor_id
    FROM competitor_medals
    WHERE medal_count = 0
);










