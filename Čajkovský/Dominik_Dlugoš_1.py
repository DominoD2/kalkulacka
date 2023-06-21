import random

den = random.randint(1, 31)
mesiac = random.randint(1, 12)
rok = random.randint(2000, 2022)


if mesiac == 2 and den > 28:
    mesiac = mesiac + 1

#if mesiac == 2 and den > 28:
#    print("Prepáč nastala chyba, dal som zlý dátum, skú to znovu")

if mesiac in [4, 6, 9, 11] and den == 31 :
    den = den - 1


print(f"Ahoj dnešný dátum je: {den}.{mesiac}.{rok}")

