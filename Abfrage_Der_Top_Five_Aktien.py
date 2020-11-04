from yahoofinancials import YahooFinancials
import time
Shortname = input('Wie lautet das Symbol? \n')



def aktien_abfrage():
    for i in range(0,1000):
        i = i+1
        DatenDerAktie = YahooFinancials(Shortname)
        PreisDerAktie = DatenDerAktie.get_current_price()
        WaehrungAktie = DatenDerAktie.get_currency()
        print(str(PreisDerAktie) +' '+ WaehrungAktie  +" "+ time.asctime()+" New York")
        time.sleep(5)

def prozent_unterschied():
        for i in range(0,1000):
            i = i+1
            DatenDerAktie = YahooFinancials(Shortname)
            Prozentuale_Veraenderung = DatenDerAktie.get_current_percent_change()
            Prozentzeichen = str('%')
            print(str(Prozentuale_Veraenderung) + " " + Prozentzeichen +" "+ time.asctime())
            time.sleep(5)

aktien_abfrage()
