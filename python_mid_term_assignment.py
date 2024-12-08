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
    
    @classmethod
    def view_book_info(self):
        for book in Library.book_list:
            print(f'ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Availability: {book.availability}')
    @classmethod
    def borrow_book(self, id):
        flag = 0
        for book in Library.book_list:
            if book.book_id == id and book.availability == True:
                book.availability = False
                flag = 1
                break
                
     
        if flag == 1:
            return f'Book {book.title} has been successfully issued'
        else:
            return f'Book {book.title} not available'
    
    @classmethod
    def return_book(self, id):
        flag = 0
        for book in Library.book_list:
            if book.book_id == id and book.availability == False:
                book.availability = True  
                flag = 1
        if flag == 1:
            return f'Book {book.title} returned successfully'
        else:
            return f'Wrong book ID'

book1 = Book("Basic Physics", "Alex Computon", True)
book2 = Book("Basic Data Structure", "John Doe", True)
book3 = Book("Programming the Virtual Machine", "Lisa Stackflow", True)
book4 = Book("Basic Artificial Intelligence", "Sophia Neuralson", True)
book5 = Book("The Art of Debugging", "John Cena", True)
book6 = Book("Internet of Things", "Oliver Twist", True)
book7 = Book("Principle of Chemistry", "Ava Trainwell", True)
book8 = Book("Magical World", "Harry Potter", True)
book9 = Book("Database Management", "Adam Smith", True)

# Book.view_book_info()
# print(Book.borrow_book(105))
# Book.view_book_info()
# print(Book.return_book(102))

while True:
    print("--------Welcome to the Library----------")
    print("1. View All Books")
    print("2. Borrow Books")
    print("3. Return Book")
    print("4. Exit")
    print("Enter your choice: ", end="")
    user_input = int(input())
    if user_input == 1:
        Book.view_book_info()
    elif user_input == 4:
        break
    else:
        print("wrong user input")



