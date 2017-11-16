import random
from time import sleep#for stein saks papir

def velkommen():
    print("§-----------------------------------------------------------§")
    print("§-----|        VELKOMMEN TIL STEIN/SAKS/PAPIR!        |-----§")
    print("§-----------------------------------------------------------§")
    print()

def valg(): #velg
    valget=str(input("Kommando: "))
    return valget



def valgmeny():
    print("    _______")
    print("---'   ____)")
    print("      (_____)")
    print("  [1] (_____)")
    print(" STEIN(____)")
    print("---.__(___)")

    print("    _______")
    print("---'   ____)____")
    print("          ______)")
    print("   [2] __________)")
    print("  SAKS(____)")
    print("---.__(___)")

    print("    _______")
    print("---'   ____)____")
    print("          ______)")
    print("   [3]    _______)")
    print("  PAPIR  _______)")
    print("---.__________)")

def revmaskinvalg(hvilken):
    if hvilken==1:
        print("  _______     ")
        print(" ( ____   '---")
        print("(_____)       ")
        print("(_____)       ")
        print("(____)        ")
        print(" (___)__.---- ")
    elif hvilken==2:
        print("      _______     ")
        print(" ____(____   '----")
        print("(______           ")
        print("(__________       ")
        print("      (____)      ")
        print("       (___)__.---")
    else:  
        print("       _______    ")
        print("  ____(____   '---")
        print(" (______          ")
        print("(_______          ")
        print("(_______          ")
        print("  (__________.--- ")
    



def choose():
    valgmeny()
    valg=eval(input("Velg[1-2-3]: "))
    return valg

def meny(): 
    print("1: 1vs1")
    print("2: 1vsCom")
    print("3: Help")
    print("4: Avslutt")

def comp():
    ran=random.randint(1,3)
    return ran

def konv(valg):
    if valg==1:
        res="stein"
    elif valg==2:
        res="saks"
    else:
        res="papir"
    return res
    

def game(valg1,valg2,Gtype): #Gtype viser funksjon hva slags game det er
    if Gtype==1:
        spiller="spiller 2"
    else:
        spiller="maskinen"
    if valg1==valg2:
        print("DRAW! Ingen vinnere!")

    elif valg1=="stein":
        if valg2=="saks":
            print("Spiller 1 vant mot",spiller)
        else:
            print("Spiller 1 tapte mot",spiller)
                
    elif valg1=="saks":
        if valg2=="papir":
            print("Spiller 1 vant mot",spiller)
        else:
            print("Spiller 1 tapte mot",spiller)
    else: #papir
        if valg2=="stein":
            print("Spiller 1 vant mot",spiller)
        else:
            print("Spiller 1 tapte mot",spiller)
    
