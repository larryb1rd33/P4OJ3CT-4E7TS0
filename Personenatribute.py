
from yahoofinancials import YahooFinancials
import time


DatenDerAktie = YahooFinancials('AAPL')
x = DatenDerAktie.get_dividend_rate()
print(x)
