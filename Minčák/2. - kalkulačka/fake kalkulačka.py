from time import sleep

a = float(input("Zadaj prvé číslo: "))

b = float(input("Zadaj druhé číslo: "))
print("Zadajte jednu z operácií: ")
print("1 - súčet")
print("2 - rozdiel")
print("3 - súčin")
print("4 - podiel")
operácia = int(input(""))
if (operácia == 1):
    výsledok = a + b
elif (operácia == 2):
    výsledok = a - b
elif (operácia == 3):
    výsledok = a * b
elif (operácia == 4):
    výsledok = a / b
if operácia > 0 and operácia < 5:
    print("výsledok: %f" % (výsledok))
else:
    print("chybná voľba")







print(f"súčet: {súčet}")
sleep()
print(f"rozdiel: {rozdiel}")
sleep()
print(f"súčin: {súčin}")
sleep()
print(f"podiel: {podiel}")
