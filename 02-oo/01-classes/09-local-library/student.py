class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for library_book in self.books:
            if library_book.title == book.title and library_book.author == book.author:
                self.books.remove(library_book)

    def search_books(self, search_string):
        results = []
        for i in self.books:
            if str(search_string).lower() in str(i.title).lower() or str(search_string).lower() in str(i.author).lower():
                results.append(i.title)
        return results
