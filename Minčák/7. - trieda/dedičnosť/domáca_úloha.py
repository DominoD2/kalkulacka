class Book:
    def __init__(self, nazov, autor, rok_vydania):
        self.nazov = nazov
        self.autor = autor
        self.rok_vydania = rok_vydania
        
    def display_info(self):
        print(f"-{self.nazov}, {self.autor}, {self.rok_vydania}")

class FictionBook(Book):
    def __init__(self, nazov, autor, rok_vydania, zaner):
        super().__init__(nazov, autor, rok_vydania)
        self.zaner = zaner

    def display_info(self):
        super().display_info()
        print(f" Žáner knihy {self.nazov} je {self.zaner}")

class NonFictionBook(Book):
    def __init__(self, nazov, autor, rok_vydania, tema):
        super().__init__(nazov, autor, rok_vydania)
        self.tema = tema

    def display_info(self):
        super().display_info()
        print(f"Téma knihy {self.nazov} je {self.tema}")

class Library(Book):
    def __init__(self):
        self.knihy = []

    def add_book(self, kniha):
        self.knihy.append(kniha)
    
    def display_available_books(self):
        print("-- Dostupné knihy v knižnici:")
        for kniha in self.knihy:
            kniha.display_info()
    
    def search_by_author(self, autor):
        zodpovedajúce_knihy = [kniha for kniha in self.knihy if kniha.autor == autor]
        print(f"-- Knihy od autora {autor}:")
        for kniha in zodpovedajúce_knihy:
            kniha.display_info()






kniha = FictionBook("Naveky tvoja", "Jana Pronská", 2023, "román")
kniha1 = FictionBook("Nočný dom", "Jo Nesbo", 2023, "detektívka/horor")
kniha2 = NonFictionBook("Rýchlokurz geniality", "Ľudovít Ódor", 2022, "genialita")
kniha3 = NonFictionBook("Stopy stredoveku", "Tomáš Gális...", 2023, "stredovek")
l = Library()
l.add_book(kniha)
l.add_book(kniha1)
l.add_book(kniha2)
l.add_book(kniha3)

l.display_available_books()
l.search_by_author("Jo Nesbo")
