from yahoofinancials import YahooFinancials 
import time

def AktieAbfrage():
    Shortname = input('Wie lautet der Kurz? \n')
    DatenDerAktie = YahooFinancials(Shortname)
    PreisDerAktie = DatenDerAktie.get_current_price()
    Dollarzeichen = str('$')
    print(str(PreisDerAktie) + " " + Dollarzeichen)
    print(type(PreisDerAktie))




for i in range(0,60):
    print(appleAktie())
    i = i+1
    print(i)
    appleAktie() = aktuellerPreis
    type(aktuellerPreis)

    if int(aktuellerPreis) > 114: 
        print("Apple's Aktie hat 114$ überschritten")

    else:
        
         print("Apple's Aktie hat 114$ unterschritten")



