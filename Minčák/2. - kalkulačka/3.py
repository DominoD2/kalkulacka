def kalkulačka(cislo1, cislo2, operator):
    if operator == "+":
        vysledok = cislo1 + cislo2
    elif operator == "-":
        vysledok == cislo1 - cislo2
    elif operator == "*":
        vysledok == cislo1 * cislo2
    elif operator == "/":
        vysledok == cislo1 / cislo2
    else:
        print("Neplatný operátor! Musíš zadať '+', '-', '*' alebo '/'")
        return None
    
    return vysledok
    