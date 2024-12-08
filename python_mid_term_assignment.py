class Library:
    book_list = []
    def __init__(self) -> None:
        pass

    @classmethod
    def entry_book(self, newBook):
        Library.book_list.append(newBook)


class Book:
    def __init__(self, title, author, availability):
        id = len(Library.book_list) + 101
        self.book_id = id
        self.title = title
        self.author = author
        self.availability = availability
        Library.entry_book(self)

    def view_book_info(self):
        for book in Library.book_list:
            print(f'ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Availability: {book.availability}')

book1 = Book("Basic Physics", "Alex Computon", True)
book2 = Book("Basic Data Structure", "John Doe", True)
book3 = Book("Programming the Virtual Machine", "Lisa Stackflow", True)
book4 = Book("Basic Artificial Intelligence", "Sophia Neuralson", True)
book5 = Book("The Art of Debugging", "John Cena", True)
book6 = Book("Internet of Things", "Oliver Twist", True)
book7 = Book("Principle of Chemistry", "Ava Trainwell", True)
book8 = Book("Magical World", "Harry Potter", True)
book9 = Book("Database Management", "Adam Smith", True)

book1.view_book_info()

