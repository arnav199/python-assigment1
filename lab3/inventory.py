

import json
import os
from .book import Book

DEFAULT_CATALOG = "catalog.json"

class LibraryInventory:
    def __init__(self, json_path=DEFAULT_CATALOG):
        self.json_path = json_path
        self.books = []
        self.load()

    def load(self):
        """Load books from JSON file if it exists, otherwise start empty."""
        self.books = []
        if not os.path.exists(self.json_path):
            return
        try:
            with open(self.json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            for item in data:
         
                title = item.get("title", "")
                author = item.get("author", "")
                isbn = item.get("isbn", "")
                status = item.get("status", "available")
                self.books.append(Book(title, author, isbn, status))
        except Exception:
       
            self.books = []

    def save(self):
        """Save current books list to JSON file."""
        data = [b.to_dict() for b in self.books]
        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def add_book(self, title, author, isbn):
        """Add a book if ISBN not already present."""
        if self.search_by_isbn(isbn) is not None:
            raise ValueError("ISBN already exists")
        book = Book(title, author, isbn)
        self.books.append(book)
        self.save()
        return book

    def search_by_title(self, query):
        """Return list of books that contain query string in title (case-insensitive)."""
        q = query.lower()
        return [b for b in self.books if q in b.title.lower()]

    def search_by_isbn(self, isbn):
        """Return book with exact ISBN or None."""
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        return list(self.books)

    def issue_book(self, isbn):
        book = self.search_by_isbn(isbn)
        if not book:
            raise LookupError("Book not found")
        book.issue()
        self.save()
        return book

    def return_book(self, isbn):
        book = self.search_by_isbn(isbn)
        if not book:
            raise LookupError("Book not found")
        book.return_book()
        self.save()
        return book

