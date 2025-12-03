

class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status 

    def __str__(self):
        return self.title + " by " + self.author + " (ISBN: " + self.isbn + ") - " + self.status

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def is_available(self):
        return self.status == "available"

    def issue(self):
        if self.status == "issued":
            raise ValueError("Book already issued")
        self.status = "issued"

    def return_book(self):
        if self.status == "available":
            raise ValueError("Book is not issued")
        self.status = "available"

