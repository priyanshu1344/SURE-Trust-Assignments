
class BookNotAvailableException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True 

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' by {author} added to the library.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print(f"Book '{title}' has been borrowed.")
                    return
                else:
                    raise BookNotAvailableException(f"Book '{title}' is not available.")
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.available = True
                print(f"Book '{title}' has been returned.")
                return
        print(f"Book '{title}' not found in the library.")

    def display_books(self):
        available_books = [book.title for book in self.books if book.available]
        if available_books:
            print("\n Available Books:")
            for book in available_books:
                print(f"- {book}")
        else:
            print("\n No books available right now.")

def main():
    library = Library()

    while True:
        print("\n Library Management System")
        print("1 Add Book")
        print("2 Borrow Book")
        print("3 Return Book")
        print("4 Display Available Books")
        print("5 Exit")
        
        choice = input("Enter your choice (1-5): ")

        try:
            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter author name: ")
                library.add_book(title, author)

            elif choice == "2":
                title = input("Enter book title to borrow: ")
                library.borrow_book(title)

            elif choice == "3":
                title = input("Enter book title to return: ")
                library.return_book(title)

            elif choice == "4":
                library.display_books()

            elif choice == "5":
                print("Exiting Library System")
                break

            else:
                print(" Invalid choice! Please enter a number between 1 and 5.")

        except BookNotAvailableException as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
