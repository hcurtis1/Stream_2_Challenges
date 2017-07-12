import datetime
import pandas
import matplotlib.pyplot as plt
from matplotlib import style
from pandas_datareader import data

style.use('fivethirtyeight')
'''
start = datetime.datetime(2010, 3, 21)
end = datetime.datetime(2015, 6, 13)

df = data.DataReader("XOM", "google", start, end)

print df.head()

df['High'].plot()
plt.legend()
plt.show()
'''
web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

df = pandas.DataFrame(web_stats)

df.set_index('Day', inplace=True)

print df.head()
print df.tail()
print df[['Visitors', 'Bounce Rate']]

df.plot()
plt.show()
