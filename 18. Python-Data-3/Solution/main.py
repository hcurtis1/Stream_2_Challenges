from database.mysql_db1 import MySQLDatabase
from settings import db_config
import random

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
                   
'''
CHALLENGE A:
Using the AVG(), select a person from your people table and get the average amount they 
spend and, at the same time, create a column that reads, “[first_name] spends “. Then 
print out the columns to provide the answers in the terminal.
'''
people = db.select('people', columns=['first_name', 'AVG(amount)''AS average_spent'],
                                      named_tuples=True, where="people.id=1",
                   join="orders ON people.id=orders.person_id")

for person in people:
    print person.first_name, " spends a total of ",person.average_spent
    
'''
CHALLENGE B:
Create a new person in the people table and add in a profile row and two orders of 
random value.
'''
# Inserting Frank Brown Into the Database
db.insert('people', first_name="Frank", surname="Brown", DOB='STR_TO_DATE("02-07-1992", "%d-%m-%Y")')

# Selecting Person ID for Frank
frank = db.select('people', ['id', 'first_name'], where='first_name = "Frank"', named_tuples=True)

# Only need the first name from the list retrieved
frank = frank[0]

# Inserting new row in profiles table
db.insert('profiles', person_id="%s" % frank.id,
          address="New York City")

# Inserting orders into orders table from frank
# 2 order inserts
db.insert('orders', person_id="%s" % frank.id, amount="%s" % random.randint(1, 200))

db.insert('orders', person_id="%s" % frank.id, amount="%s" % random.randint(1, 200))

orders = db.select('orders', where='person_id=%s' % frank.id)

for order in orders:
    print order
    
'''
CHALLENGE C:
Once you’ve added them in use select to get their full name and the minimum amount 
they have spent.
'''

