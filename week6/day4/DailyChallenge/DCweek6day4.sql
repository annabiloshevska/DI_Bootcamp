--Exercise 1: Detailed Medal Analysis
--Task 1: Identify competitors who have won at least one medal in events spanning both Summer and Winter Olympics. Create a temporary table to store these competitors and their medal counts for each season, and then display the contents of this table.
CREATE TEMP TABLE medal_seasons AS
SELECT ce.competitor_id,
       g.season,
       COUNT(*) AS medal_count
FROM competitor_event ce
JOIN games_competitor gc ON gc.person_id = ce.competitor_id
JOIN games g ON g.id = gc.games_id
WHERE ce.medal_id <> 4
GROUP BY ce.competitor_id, g.season;

SELECT *
FROM medal_seasons
GROUP BY competitor_id
HAVING COUNT(DISTINCT season) = 2;

--Task 2: Create a temporary table to store competitors who have won medals in exactly two different sports, and then use a subquery to identify the top 3 competitors with the highest total number of medals across all sports. Display the contents of this table.
CREATE TEMP TABLE two_sport_medalists AS
SELECT ce.competitor_id,
       COUNT(DISTINCT e.sport_id) AS sport_count,
       COUNT(ce.medal_id) AS medal_count
FROM competitor_event ce
JOIN event e ON e.id = ce.event_id
WHERE ce.medal_id <> 4
GROUP BY ce.competitor_id
HAVING sport_count = 2;

SELECT *
FROM two_sport_medalists
ORDER BY medal_count DESC
LIMIT 3;


--Exercise 2: Region and Competitor Performance
--Task 1: Retrieve the regions that have competitors who have won the highest number of medals in a single Olympic event. Use a subquery to determine the event with the highest number of medals for each competitor, and then display the top 5 regions with the highest total medals.
SELECT r.region_name,
       SUM(medal_count) AS total_medals
FROM (
    SELECT ce.competitor_id,
           ce.event_id,
           COUNT(*) AS medal_count
    FROM competitor_event ce
    WHERE ce.medal_id <> 4
    GROUP BY ce.competitor_id,  ce.event_id
) t
JOIN person_region pr ON t.competitor_id = pr.person_id
JOIN noc_region r ON pr.region_id = r.id
GROUP BY r.region_name
ORDER BY total_medals DESC
LIMIT 5;

--Task 2: Create a temporary table to store competitors who have participated in more than three Olympic Games but have not won any medals. Retrieve and display the contents of this table, including their full names and the number of games they participated in.

CREATE TEMP TABLE no_medals_multi_games AS
SELECT gc.person_id,
	   p.full_name,	
       COUNT(DISTINCT games_id) AS games_played
FROM games_competitor gc
JOIN person p ON gc.person_id = p.id
WHERE gc.person_id NOT IN (
      SELECT competitor_id
      FROM competitor_event
      WHERE medal_id <> 4
)
GROUP BY gc.person_id
HAVING games_played > 3;

SELECT *
FROM no_medals_multi_games;

