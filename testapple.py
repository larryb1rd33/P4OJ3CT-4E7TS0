from yahoofinancials import YahooFinancials 
import time

def appleAktie():
    appleshortname = 'AAPL'
    apple = YahooFinancials(appleshortname)
    applePreis=apple.get_current_price()
    Dollarzeichen = str('$')
    print(str(applePreis) + " " + Dollarzeichen)



def AktieAbfrage():
    Shortname = input('Wie lautet der Kurz? \n')
    DatenDerAktie = YahooFinancials(Shortname)
    PreisDerAktie = DatenDerAktie.get_current_price()
    Dollarzeichen = str('$')
    print(str(PreisDerAktie) + " " + Dollarzeichen)
    print(type(PreisDerAktie))