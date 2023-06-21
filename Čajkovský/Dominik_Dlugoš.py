from time import sleep


meno = input("Zadaj svoje meno: ")
pismeno = input("Zadaj ľubovolné písmeno v tvojom mene: ")
txt = str(meno)
x = txt.find(pismeno)

if meno == "Dominik":
    print("Ahoj Dominik: " + meno.upper())
    sleep(2.5)
    print("Funkcia lower(): " + meno.lower())
    sleep(2.5)
    print("Poradie písmena: " + str(x))

else:
    print("Ahoj " + meno + ", toto je tvoje meno vo funkcii upper(): " + meno.upper())
    sleep(2.5)
    print("A toto zas vo funkcii lower(): " + meno.lower()) 
    sleep(2.5)
    print("A nakoniec toto je poradie písmena ktoré si zadal :  " + str(x))
