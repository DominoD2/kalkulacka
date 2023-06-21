class Kniha:
    def __init__(self, nazov, mnozstvo, autor, __cena):
        self.nazov = nazov
        self.mnozstvo = mnozstvo
        self.autor = autor
        self.__cena = __cena
        self.__zlava = None

    def set_zlava(self, zlava):
        self.__zlava = zlava

    def get_cena(self):
        if self.__zlava:
            return self.__cena * (1-self.__zlava)
        return self.__cena
    
    def __repr__(self):
        return f"Kniha {self.nazov}, Množstvo {self.mnozstvo}, Autor {self.autor}, Cena {self.get_cena()}"
    

jedna_kniha = Kniha("Kde bolo tam bolo", 1, "Janko Hraško", 200)

viacero_knih = Kniha("Kde bolo tam bolo", 25, "Janko Hraško", 200)
viacero_knih.set_zlava(0.20)

print(jedna_kniha.get_cena())
print(viacero_knih.get_cena())
print(jedna_kniha)
print(viacero_knih)
