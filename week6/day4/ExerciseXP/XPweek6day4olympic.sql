--PART 1

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


--PART 2

--Exercise 2: Advanced Data Manipulation and Optimization
--Task 1: Update the heights of competitors based on the average height of competitors from the same region. Use a correlated subquery within the UPDATE statement.

UPDATE person
SET height = (
    SELECT AVG(p2.height)
    FROM person p2
    JOIN person_region pr2 
         ON pr2.person_id = p2.id
    JOIN noc_region r
         ON pr2.region_id = r.id
    WHERE pr2.region_id IN (SELECT region_id
					  		FROM person_region pr
					  		WHERE pr.person_id = p2.id)
                			and p2.height <> 0)
	WHERE height = 0;    


CREATE INDEX IF NOT EXISTS idx_person_region_person_id
ON person_region(person_id);

CREATE INDEX IF NOT EXISTS idx_person_region_region_id
ON person_region(region_id);           
                      
--Task 2: Insert new records into a temporary table for competitors who participated in more than one event in the same games and list their total number of events participated. Use nested subqueries for filtering.
CREATE TEMP TABLE multi_event AS
SELECT competitor_id,
       games_id,
       COUNT(event_id) AS total_events
FROM games_competitor gc
JOIN competitor_event ce
     ON gc.person_id = ce.competitor_id
GROUP BY competitor_id, games_id
HAVING total_events > 1;


--Task 3: Identify regions where the average number of medals won per competitor is greater than the overall average. Use subqueries to calculate and compare averages.
SELECT region_name, ROUND(AVG(cm.medal_count)) as avg_medals
FROM noc_region r
JOIN person_region pr ON pr.region_id = r.id
JOIN (
     SELECT competitor_id,
            COUNT(medal_id) AS medal_count
     FROM competitor_event
     GROUP BY competitor_id
) cm ON cm.competitor_id = pr.person_id
GROUP BY r.region_name
HAVING AVG(cm.medal_count) >
       (SELECT AVG(medal_count)
        FROM (
           SELECT competitor_id,
                  COUNT(medal_id) AS medal_count
           FROM competitor_event
           WHERE medal_id <> 4
           GROUP BY competitor_id
        ));

--Task 4: Create a temporary table to track competitors’ participation across different seasons and identify those who have participated in both Summer and Winter games.

CREATE TEMP TABLE season_events AS
SELECT person_id,
	   COUNT(DISTINCT g.season) AS seasons_partisipated
FROM games_competitor gc
JOIN games g
     ON gc.games_id = g.id
GROUP BY person_id
HAVING COUNT(DISTINCT g.season) = 2;
SELECT * FROM season_events










