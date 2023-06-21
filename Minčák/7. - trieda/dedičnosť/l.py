class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def display_info(self):
        print(f"-{self.title}, {self.author}, {self.year}")

class FictionBook(Book):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre
    
    def display_info(self):
        super().display_info()
        print(f"Žáner knihy je {self.genre}")

class NonFictionBook(Book):
    def __init__(self, title, author, year, topic):
        super().__init__(title, author, year)
        self.topic = topic
    
    def display_info(self):
        super().display_info()
        print(f"Téma knihy je {self.topic}")

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def display_available_books(self):
        if len(self.books) == 0:
            print("-- V knižnici nie sú žiadne dostupné knihy.")
        else:
            print("-- Dostupné knihy v knižnici:")
            for book in self.books:
                book.display_info()
    
    def search_by_author(self, author):
        matching_books = [book for book in self.books if book.author == author]
        if len(matching_books) == 0:
            print(f"-- V knižnici nie sú žiadne knihy od autora {author}.")
        else:
            print(f"-- Knihy od autora {author}:")
            for book in matching_books:
                book.display_info()

book1 = FictionBook("Hra o tróny", "George R. R. Martin", 1996, "fantasy")
book2 = FictionBook("Harry Potter a Kameň mudrcov", "J. K. Rowling", 1997, "fantasy")
book3 = NonFictionBook("Clean Code", "Robert C. Martin", 2008, "programovanie")
book4 = NonFictionBook("Sapiens: Krátka história ľudstva", "Yuval Noah Harari", 2011, "antropológia")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

library.display_available_books()

library.search_by_author("George R. R. Martin")
