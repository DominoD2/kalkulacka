class Auto:
    def __init__(self, znacka, model, rok_vyroby, stav_km):
        self.znacka = znacka
        self.model = model
        self.rok_vyroby = rok_vyroby
        self.stav_km = stav_km

    def zobraz_info(self):
        print("Informácie o aute:")
        print("Značka: ", self.znacka)
        print("Model: ", self.model)
        print("Rok výroby: ", self.rok_vyroby)
        print("Stav km: ", self.stav_km)

    def prejazd_km(self, kilometry):
        self.stav_km += kilometry

auto1 = Auto("Škoda", "Rapid", 2014, 159000)

auto1.zobraz_info()

auto1.prejazd_km(100)

auto1.zobraz_info()
