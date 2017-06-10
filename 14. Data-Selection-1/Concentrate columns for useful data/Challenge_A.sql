select concat('Wally spent a total of ') as 'action',
SUM(amount) as 'Total' from mydb.orders WHERE person_id=1;