USE mydb;

INSERT INTO orders (
	amount,
    person_id
) VALUES 
	(215.32, 1),
    (360.33, 2),
    (752.25, 2),
    (4788.36, 3),
    (455.85, 3),
    (486.65, 3),
    (735232.33, 4);
    
SELECT * FROM orders
WHERE person_id
BETWEEN
'2'
AND
'3';