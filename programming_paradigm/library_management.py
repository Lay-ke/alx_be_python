class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
    
    def check_out_book(self, title):
        book = next((book for book in self._books if book.title == title), None)
        if book and not book._Book__is_checked_out:
            book._Book__is_checked_out = True
            return f"{title} has been checked out."
        return f"{title} is not available for checkout."
    
    def return_book(self):
        book = next((book for book in self._books if book._is_checked_out), None)
        if book:
            book._is_checked_out = False
            return f"{book.title} has been returned."
        return "No books are currently checked out."
    
    def list_available_books(self):
        available_books = [book.title for book in self._books if not book._Book__is_checked_out]
        return available_books
