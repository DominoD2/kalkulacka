def sucin(*cisla):
    vysledok = 1
    for cislo in cisla:
        vysledok = vysledok * cislo
    return vysledok
priklad = sucin(458526, 41254, 78963, 410)
print(priklad)