SELECT a.* 
FROM a 
JOIN ( 
  SELECT a.alias, MAX(a.year) as max_year 
  FROM a 
  GROUP BY a.alias
) b 
ON a.alias=b.alias and a.year=b.max_year