import funk
from time import sleep
import os
clear = lambda: os.system('cls')
valg = 0

while (valg!="avslutt"):
    sleep(1)
    print()
    funk.velkommen()
    funk.meny()
    print()
    valg = funk.valg()
    clear()
    if valg=="1":
        print("--------------Spiller 1's tur--------------")
        pvalg=funk.choose()
        p1=funk.konv(pvalg)
        print("Takk! Nå er det spiller2's tur")
        sleep(2)
        clear()
        print("--------------Spiller 2's tur--------------")
        pvalg=funk.choose()
        p2=funk.konv(pvalg)
        funk.game(p1,p2,1)
        time(5)
        clear()
    elif valg=="2":
        print("--------------Spiller 1's tur--------------")
        pvalg=funk.choose()
        p=funk.konv(pvalg)
        print("Du valgte",p,"! Nå er det maskinens tur")
        sleep(3)
        clear()
        print("--------------Terminator's tur-------------")
        com=funk.comp()
        funk.revmaskinvalg(com)
        cp=funk.konv(com)
        print()
        print("TERMINATOR VALGTE:",cp.upper())
        funk.game(p,cp,2) #Type 2
        sleep(5)
        clear()
    elif valg==3:
        print("3")
    elif valg=="help":
        print("help")
        c=funk.comp()
        print(c)
    else:
        print("Wrong, try again ")

clear()
print("Farvel!")
time.sleep(10)


