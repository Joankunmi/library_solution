class Book:
    def __init__(self, title, author, genre, copies):
        self.title = title
        self.author = author
        self.genre = genre
        self.copies = copies

class LiberoLibrary:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Copies: {book.copies}")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
        book = self.search_book(title)
        if book:
            if book.copies > 0:
                book.copies -= 1
                print(f"Successfully borrowed {book.title}")
            else:
                print("No copies available for borrowing.")
        else:
            print("Book not found in the library.")

    def return_book(self, title):
        book = self.search_book(title)
        if book:
            book.copies += 1
            print(f"Successfully returned {book.title}")
        else:
            print("Book not found in the library.")

def main():
    libero_library = LiberoLibrary()

    book1 = Book("Python Crash Course", "Eric Matthes", "Programming", 5)
    book2 = Book("The Alchemist", "Paulo Coelho", "Fiction", 3)
    book3 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Fantasy", 7)

    libero_library.add_book(book1)
    libero_library.add_book(book2)
    libero_library.add_book(book3)

    while True:
        print("\nMenu:")
        print("1. Display all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            libero_library.display_books()
        elif choice == 2:
            title = input("Enter the title of the book you want to borrow: ")
            libero_library.borrow_book(title)
        elif choice == 3:
            title = input("Enter the title of the book you want to return: ")
            libero_library.return_book(title)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
