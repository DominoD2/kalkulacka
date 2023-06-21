from pstats import FunctionProfile


def scitaj(x,y):
    return x + y

#volanie funkcie print s argumentom 123123
print(123123)

# skladanie/kompozícia funkcii
print(scitaj(1,2))


# verzia 1
print(scitaj(scitaj(4,5),scitaj(2,3)))

# verzia 2
cislo1 = scitaj(4,5)
cislo2 = scitaj(2,3)
scitaj = (cislo1 + cislo2)
print(scitaj)

# ctrl + k + c - comment
# ctrl + k + u - uncomment


# tu som do premennej cislo1 priradil navratovu hodnotu funkcie scitaj
cislo1 = scitaj(4, 5) 

# tu som do premennej priradil vysledok operacie scitania
x = 2 + 3

# tu som do premennej y prieaniel obsah premennej x
y = x

"""
vstavane funkcie
print
round
"""
# funkcia "type()" určí typ premennej 

"""
- kľúčové slovíčka 
- funkcie: print(), type(), round()...
- kompozícia funkcie - print(scitaj(scitaj(4,5),scitaj(2,3)))
- meno funkcie - pred zátvorkami


"""
#stringy na uloženie textu ("Ahoj svet")

# Chceme nacitat 2 cisla a vypisat ich sucet
#
#pouzit input 2x (input vracia string)
#


x = input("Prvé číslo:")
x = int(x)
z = input("Druhé číslo:")
z = int(z)
print("Tvoj výsledok: ", x + z)




print("zadaj svoje meno:")
x = input()
print("Ahoj, " + x)

x = input("Zadaj svoje meno verzia 2: ")
print("ahoj, " + x)
