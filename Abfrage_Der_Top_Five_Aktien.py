from yahoofinancials import YahooFinancials 
import time

def AktienAbfrage():
    Shortname = input('Wie lautet das Symbol? \n')

    for i in range(0,1000):
        i = i+1
        DatenDerAktie = YahooFinancials(Shortname)
        PreisDerAktie = DatenDerAktie.get_current_price()
        Dollarzeichen = str('$')
        print(str(PreisDerAktie) + " " + Dollarzeichen +" "+ time.asctime()+" New York")                

        """
        if PreisDerAktie > 114.0 : 
            print("Apple's Aktie hat 114$ überschritten")
        else:
         print("Apple's Aktie hat 114$ unterschritten")
        """    
        time.sleep(5)

AktienAbfrage()
