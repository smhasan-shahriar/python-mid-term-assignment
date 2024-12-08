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
        self.__book_id = id
        self.__title = title
        self.__author = author
        self.__availability = availability
        Library.entry_book(self)
    
    @classmethod
    def view_book_info(self):
        print("Library Books:")
        for book in Library.book_list:
            status = "Available"
            if book.__availability == False:
                status = "Not Available"
            else:
                status = "Available"
            print(f'ID: {book.__book_id}, Title: {book.__title}, Author: {book.__author}, Availability: {status}')
    @classmethod
    def borrow_book(self, id):
        flag = 0
        signal = 0
        for book in Library.book_list:
            if book.__book_id == id:
                signal = 1
                if book.__availability == True:
                    book.__availability = False
                    flag = 1
                    break
        if signal == 1:
            if flag == 1:
                return f"Book '{book.__title}' borrowed successfully"
            else:
                return f"Book '{book.__title}' is already borrowed"
        else:
            return f"Invalid Book ID"
    
    @classmethod
    def return_book(self, id):
        flag = 0
        signal = 0
        for book in Library.book_list:
            if book.__book_id == id:
                signal = 1
                if book.__availability == False:
                    book.__availability = True
                    flag = 1
                    break
        if signal == 1:
            if flag == 1:
                return f"Book '{book.__title}' returned successfully"
            else:
                return f"Book '{book.__title}' is not borrowed. Check your Book ID"
        else:
            return f"Invalid Book ID"
       

book1 = Book("Basic Physics", "Alex Computon", True)
book2 = Book("Basic Data Structure", "John Doe", True)
book3 = Book("Programming the Virtual Machine", "Lisa Stackflow", True)
book4 = Book("Basic Artificial Intelligence", "Sophia Neuralson", True)
book5 = Book("The Art of Debugging", "John Cena", True)
book6 = Book("Internet of Things", "Oliver Twist", True)
book7 = Book("Principle of Chemistry", "Ava Trainwell", True)
book8 = Book("Magical World", "Harry Potter", True)
book9 = Book("Database Management", "Adam Smith", True)


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
    elif user_input == 2:
        print("Enter Book ID to borrow: ", end="")
        entry = int(input())
        result = Book.borrow_book(entry)
        print(result)
    elif user_input == 3:
        print("Enter Book ID to return: ", end="")
        entry = int(input())
        result = Book.return_book(entry)
        print(result)
    elif user_input == 4:
        break
    else:
        print("wrong user input")



