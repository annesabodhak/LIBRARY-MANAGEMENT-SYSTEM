#DEVELOP A MENU DRIVEN PROGRAM FOR LIBRARY MANAGEMENT SYSTEM USING PYTHON THAT ALLOWS A LIBRARIAN TO MANAGE BOOKS, TRACK THEIR AVAILABILITY AND HANDLE BOOK BORROWING AND RETURNING USING PYTHON
from abc import ABC, abstractmethod

_builtin_print = print


class print(ABC):
    @abstractmethod
    def add_book(self):
        """Add a new book to the library."""
        raise NotImplementedError

    @abstractmethod
    def display(self):
        """Display all books in the library."""
        raise NotImplementedError

    @abstractmethod
    def borrow_book(self):
        """Borrow a book from the library."""
        raise NotImplementedError

    @abstractmethod
    def return_book(self):
        """Return a borrowed book to the library."""
        raise NotImplementedError

    @abstractmethod
    def search(self):
        """Search for a book by title."""
        raise NotImplementedError


class Book:
    def __init__(self, title, author, book_id, available=True):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.available = available

    def __str__(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.available}"


class s(print):
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        bid = int(input("Enter the book ID: "))

        if any(book.book_id == bid for book in self.books):
            print("A book with this ID already exists.")
            return

        self.books.append(Book(title, author, bid, True))
        print(f"Book '{title}' added successfully.")

    def display(self):
        if not self.books:
            print("No books are available in the library.")
            return

        print("Displaying all books in the library:")
        for book in self.books:
            print(book)

    def borrow_book(self):
        bid = int(input("Enter the book ID to borrow: "))

        for i in self.books:
            if i.book_id == bid:
                if i.available:
                    i.available = False
                    print(f"Book '{i.title}' has been borrowed successfully.")
                    return
                print(f"Book '{i.title}' is already borrowed.")
                return

        print("Book not found.")

    def return_book(self):
        bid = int(input("Enter the book ID to return: "))

        for i in self.books:
            if i.book_id == bid:
                if not i.available:
                    i.available = True
                    print(f"Book '{i.title}' has been returned successfully.")
                    return
                print(f"Book '{i.title}' is already available.")
                return

        print("Book not found.")

    def search(self):
        d= str(input("Enter the book title to search: "))
        for i in self.books:
            if i.title.lower() == d.lower():
                print("Book is available:" , i.title , "Book ID is:" , i.book_id , "Author is:" , i.author)
                return

        print("Book is not available in the library.")
        
    def available(self):
        for i in self.books:
            if i.available == True:
                print("Book is available:" , i.title , "Book ID is:" , i.book_id , "Author is:" , i.author)
            else: 
                print("Book is not available")

print = _builtin_print

library = s()
print("Welcome to the Library Management System!")

while True:
    print("\n1. Add book")
    print("2. Display books")
    print("3. Borrow book")
    print("4. Return book")
    print("5. Search book")
    print("6. Available books")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if  choice == '1':
        library.add_book()
    elif choice == '2':
        library.display()
    elif choice == '3':
        library.borrow_book()
    elif choice == '4':
        library.return_book()
    elif choice == '5':
        library.search()
    elif choice == '6':
        library.available()
    elif choice == '7':
        print("Exiting... Thank you for using the Library Management System. Goodbye!")    


        break


    else:
        print("Invalid choice. Please try again.")
    
