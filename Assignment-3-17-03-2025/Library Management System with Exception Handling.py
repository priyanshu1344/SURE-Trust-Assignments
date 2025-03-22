class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title):
        self.books[title] = True
        print(f"Added: {title}")

    def borrow_book(self, title):
        if self.books.get(title, False):
            self.books[title] = False
            print(f"Borrowed: {title}")
        else:
            print(f"'{title}' is not available.")

    def return_book(self, title):
        if title in self.books:
            self.books[title] = True
            print(f"Returned: {title}")
        else:
            print(f"'{title}' not found.")

    def show_books(self):
        available = [title for title, available in self.books.items() if available]
        print("Available Books:", ", ".join(available) if available else "None")

library = Library()

while True:
    choice = input("\n1. Add Book\n2. Borrow Book\n3. Return Book\n4. Show Books\n5. Exit\nChoose: ")

    if choice == "1":
        library.add_book(input("Title: "))
    elif choice == "2":
        library.borrow_book(input("Title: "))
    elif choice == "3":
        library.return_book(input("Title: "))
    elif choice == "4":
        library.show_books()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
