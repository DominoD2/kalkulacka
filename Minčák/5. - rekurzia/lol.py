def parneCislo(cislo):
    print(cislo)
    if cislo % 2 != 0:
        print("Zadaj znova")
        return
    if cislo == 2:
        return cislo
    else:
        return parneCislo(cislo - 2)
    
parneCislo(99)