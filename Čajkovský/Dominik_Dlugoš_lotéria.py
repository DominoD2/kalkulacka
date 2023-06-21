import random
from time import sleep

nahodne_cislo = random.randint(0, 10)

while True:
    hodnota_1 = int(input("Zadaj číslo od 0 po 10 a zisti či si vyhral (máš 2 pokusy): "))
    sleep(2)

    if hodnota_1 == nahodne_cislo:
        print("VYHRAL SI, super tipol si si správne číslo.")
        exit()

    elif hodnota_1 > 10:
        hodnota_2 = int(input("Zadal si číslo ktoré nie je v losovaní, prosím zadaj číslo od 0 do 10 (už len 1 pokus): "))
        sleep(2)
        if hodnota_2 == nahodne_cislo:
            print("VYHRAL SI, super tipol si si správne číslo.")
            exit()
        else:
            print("PREHRAL SI, prišiel si o všetky pokusy")
            print(f"Číslo ktoré program vylosoval bolo -{nahodne_cislo}-")

    elif hodnota_1 != nahodne_cislo:
        hodnota_3 = int(input("PREHRAL SI, nevadí skús to ešte raz: "))
        sleep(2)
        if hodnota_3 == nahodne_cislo:
            print("VYHRAL SI, super tipol si si správne číslo.")
            exit()
        else:
            print("PREHRAL SI, prišiel si o všetky pokusy.")
            print(f"Číslo ktoré program vylosoval bolo -{nahodne_cislo}-")
            sleep(3)
    
    
    