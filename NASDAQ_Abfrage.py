import pandas_datareader as web
import datetime
import matplotlib.pyplot as plt
import numpy as np

#%matpolotlib inline

start = datetime.datetime(2020,1,1)
end = datetime.datetime(2020,11,5)

google = web.DataReader('GOOGL', 'yahoo', start,end)

print(google.head())
open = 'GOOGL Open Price'
close = 'GOOGL Close Price'


google['Open'].plot(figsize=(20,7))
google['Close'].plot(figsize=(20,7))
google['High'].plot(figsize=(20,7))
google['Low'].plot(figsize=(20,7))
plt.legend()
plt.title('Google Stock Price')
plt.ylabel('Stock Price in Dollar')

#google['Volume'].plot(figsize=(17,5))

plt.show()


start = datetime.datetime(2010,1,1)
end = datetime.datetime(2020,11,5)

tesla = web.DataReader("TSLA", "yahoo", start,end)
ford = web.DataReader("F", 'yahoo',start, end)
gm = web.DataReader('GM','yahoo',start, end)


tesla.to_csv('Tesla_Stock.csv')

tesla.head()
tesla['Open'].plot()
