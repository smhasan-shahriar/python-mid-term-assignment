class Library:
    book_list = []
    def __init__(self) -> None:
        pass

    @classmethod
    def entry_book(self):
        pass

class Book:
    def __init__(self, book_id, title, author, availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability
