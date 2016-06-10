-- https://leetcode.com/discuss/26113/accepted-solution-with-subqueries-and-group-by
-- Really tricky answer.
-- The inner select is:
-- 	for i in Scores:
-- 		for j in Scores:
-- 			if i <= j:
-- 				count++
-- Interesting to see the count(*) here
SELECT Scores.Score, Q3.Rank
FROM(
    SELECT Q1.Score as Score, COUNT(Q1.Score) as Rank
    FROM 
        (SELECT DISTINCT Score from Scores) as Q1,
        (SELECT DISTINCT Score from Scores) as Q2
    WHERE Q1.Score <= Q2.Score
    GROUP BY Q1.Score
    ) as Q3, Scores
WHERE Q3.Score = Scores.Score
ORDER BY Scores.Score DESC