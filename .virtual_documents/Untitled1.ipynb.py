print('Test')


import pandas_datareader as web
import datetime
import matplotlib.pyplot as plt
import numpy as np


start = datetime.datetime(2010,1,1)
end = datetime.datetime(2020,11,5)

tesla = web.DataReader("TSLA", "yahoo", start,end)
ford = web.DataReader("F", 'yahoo',start, end)
gm = web.DataReader('GM','yahoo',start, end)


#tesla.to_csv('Tesla_Stock.csv')

tesla.head()
tesla['Open'].plot()




