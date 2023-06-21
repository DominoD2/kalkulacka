class Student:
    def __init__(self, meno, vek):
        self.meno = meno
        self.vek = vek

    def vypis_udaje(self):
        print("Meno: ", self.meno)
        print("vek: ", self.vek)

student1 = Student("Dominik", 17)
student2 = Student("Daniel", 16)



class Film:
    def __init__(self, _nazov,):
        self._nazov = _nazov
        self._hodnotenie = None
    
    def ziskaj_nazov(self):
        print(f"Názov filmu je {self._nazov}")
    
    def ziskaj_hodnotenie(self):
        print(f"Hodnotenie je {self._hodnotenie}")

    def nastav_hodnotenie(self, hodnota):
        self.hodnota = hodnota
        if hodnota < 0 or hodnota >10:
            ValueError("Zadal si nesprávnu hodnotu")
    
Inception = Film("Inception", 12)
Inception2 = Film("Inception", 8,7)

Inception.ziskaj_nazov()
Inception.ziskaj_hodnotenie()
Inception2.ziskaj_nazov()
Inception2.ziskaj_hodnotenie()