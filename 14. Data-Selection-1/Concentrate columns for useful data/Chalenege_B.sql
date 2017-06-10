INSERT INTO mydb.people (
	first_name,
    surname,
    DOB
) VALUES 
	('Clive', 'Sinclair', STR_TO_DATE('03/08/1995', '%d/%m/%Y')),
    ('Mat', 'Olive', STR_TO_DATE('31/07/1991', '%d/%m/%Y')),
    ('Jack', 'McKenna', str_to_date('11/08/1990', '%d/%m/%Y'));

INSERT INTO mydb.orders (
	amount,
    person_id
) VALUES
	(7052, 6),
    (354, 6),
    (546.52, 6),
    (48.32, 7),
    (509.36, 7),
    (459.02, 7),
    (25.99, 8),
    (45.33, 8),
    (78952.33, 8);

SELECT DISTINCT(person_id) FROM mydb.orders