from yahoofinancials import YahooFinancials 
import time
from Abfrage_Der_Top_Five_Aktien import AktieAbfrage

def appleAktie():
    appleshortname = 'AAPL'
    apple = YahooFinancials(appleshortname)
    applePreis=apple.get_current_price()
    Dollarzeichen = str('$')
    print(str(applePreis) + " " + Dollarzeichen)



def Aktie1Abfrage():
    Shortname = input('Wie lautet der Kurz? \n')
    DatenDerAktie = YahooFinancials(Shortname)
    PreisDerAktie = DatenDerAktie.get_current_price()
    Dollarzeichen = str('$')
    print(str(PreisDerAktie) + " " + Dollarzeichen)
    print(type(PreisDerAktie))

Aktie1Abfrage()