class PC:
    def __init__(self, značka, typ, RAM, CPU):
        self.značka = značka
        self.typ = typ
        self.RAM = RAM
        self.CPU = CPU
    
    def vypis_udaje(self):
        print(f"Značka je {self.značka}")
        print(f"Typ PC je {self.typ}")
        print(f"Veľkosť RAM je {self.RAM}")
        print(f"CPU je {self.CPU}")
    
pc = PC("DELL", "prenosný", "32GB", "5GHz")

pc.vypis_udaje()