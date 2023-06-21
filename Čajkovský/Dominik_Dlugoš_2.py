vek = int(input("Zadaj svôj vek: "))

if vek in (18, 100):
    print(f"MáŠ povolenie piť alkohol keďže je tvoj vek {vek} rokov ")

elif vek < 18:
    print("Si ešte decko máš čas :)")

elif vek > 100:
    print("No vzhľadom na to že máš viac ako 100 rokov nedoporučujem ti piť bo skapeš" )
