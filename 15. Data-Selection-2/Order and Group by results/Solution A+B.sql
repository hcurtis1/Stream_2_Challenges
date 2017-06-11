SELECT * FROM mydb.orders
WHERE created_at
BETWEEN
'2015-09-08 00:00:00'
AND
'2017-06-10 00:00:00'
AND NOT
amount < 12.00
ORDER BY amount DESC;

SELECT person_id, COUNT(amount) FROM mydb.orders;