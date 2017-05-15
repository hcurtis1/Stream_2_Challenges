# Safe Refactoring Challenge 

Try using the decimal module (https://docs.python.org/2/library/decimal.html) to deal with the floating point issues and make the tests pass. An example of its use is given in the python console screenshot below:


1 >>> from decimal import *
2 >>> Decimal('0.1') + Decimal('0.2')
3 Decimal('0.3')


You’ll have to convert the Decimal back to a float, otherwise the test will be comparing Decimals to ints. In the same way that int is shorthand for Integer, float is shorthand for Floating Point number.