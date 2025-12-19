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
