from time import sleep
loop = True

while loop:
    x = input("Zadaj prvé číslo: ")
    x = float(x)
    y = input("Zadaj druhé číslo: ")
    y = float(y)

    if x == 666 and y == 666:
        print("vytajte v politickej sieti")

    elif x + y == 69:
        print("Mi povedz o čo sa snažíš")

    elif x == 69 and y == 69:
        print("Nerob debiliny ty sviňa")

    else:
        print("Výsledok násobenia je: ", x * y)
        sleep(1.5)
        print("Výsledok sčítania je: ", x + y )
        sleep(1.5)
        print("Výsledok mocnenia je: ", round(x ** y, 5))
        sleep(1.5)
        print("Výsledok celočísleného delenia je: ", x // y)


