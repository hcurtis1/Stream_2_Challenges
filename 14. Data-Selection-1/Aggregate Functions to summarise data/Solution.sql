select sum(amount) as 'Total Cost of All Orders', 
count(amount) as 'Number of Orders',
avg(amount) as 'Average of amounts'
from mydb.orders;