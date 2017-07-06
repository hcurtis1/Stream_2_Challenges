from database.mysql_db1 import MySQLDatabase
from settings import db_config

"""
Retrieve the settings from the
`db_config` dictionary to connect to
our database so we can instantiate our
MySQLDatabase object
"""
db = MySQLDatabase(db_config.get('db_name'),
                   db_config.get('user'),
                   db_config.get('pass'),
                   db_config.get('host'))
                   
# Select data using LIMIT clause
limit_expression_records = db.select('people', limit='2')
print '________________________'
print 'First 2 Results'
print '________________________'

for result in limit_expression_records:
    print result

# Select data using LIMIT clause with 5 results
limit_expression_records = db.select('orders', limit='5')
print 'FIRST 5 RESULTS'

for result in limit_expression_records:
    print result

# Select data using ORDER BY clause
order_records = db.select('articles', order_by='title')
print 'Articles ordered by title:'
print str(order_records)


# Select data using ORDER BY clause
order_records = db.select('people', order_by='first_name')
print '______________'
print 'People order by their first name:'
print str(order_records)