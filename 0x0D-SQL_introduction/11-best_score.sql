-- List all records where score is >= 10 in second table
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;