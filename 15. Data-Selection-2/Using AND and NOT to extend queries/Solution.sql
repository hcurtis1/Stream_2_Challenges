USE mydb;

SELECT * FROM orders
WHERE person_id
NOT BETWEEN
'2'
AND
'3'
AND
created_at > '2017-06-08 00:00:00';

SELECT * FROM articles WHERE title LIKE '%article%'
AND title NOT LIKE '%2';