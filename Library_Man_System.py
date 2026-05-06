import json

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"[{self.book_id}] {self.title} by {self.author} ({status})"


class Library:
    def __init__(self):
        self.books = []
        self.load_data()

    def add_book(self, title, author):
        book_id = len(self.books) + 1
        book = Book(book_id, title, author)
        self.books.append(book)
        self.save_data()
        print("✅ Book added successfully!")

    def show_books(self):
        if not self.books:
            print("No books available.")
            return
        for book in self.books:
            print(book)

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_issued:
                    book.is_issued = True
                    self.save_data()
                    print("📚 Book issued!")
                    return
                else:
                    print("❌ Already issued!")
                    return
        print("Book not found!")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    book.is_issued = False
                    self.save_data()
                    print("🔁 Book returned!")
                    return
                else:
                    print("❌ Book was not issued!")
                    return
        print("Book not found!")

    def search_book(self, title):
        found = False
        for book in self.books:
            if title.lower() in book.title.lower():
                print(book)
                found = True
        if not found:
            print("No matching book found.")

    def delete_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                self.save_data()
                print("🗑️ Book deleted!")
                return
        print("Book not found!")

    def save_data(self):
        data = []
        for book in self.books:
            data.append({
                "id": book.book_id,
                "title": book.title,
                "author": book.author,
                "issued": book.is_issued
            })

        with open("library.txt", "w") as f:
            json.dump(data, f)

    def load_data(self):
        try:
            with open("library.txt", "r") as f:
                data = json.load(f)
                for item in data:
                    book = Book(item["id"], item["title"], item["author"])
                    book.is_issued = item["issued"]
                    self.books.append(book)
        except:
            pass


def main():
    lib = Library()

    while True:
        print("\n==== Library Menu ====")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Delete Book")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            lib.add_book(title, author)

        elif choice == "2":
            lib.show_books()

        elif choice == "3":
            book_id = int(input("Enter Book ID: "))
            lib.issue_book(book_id)

        elif choice == "4":
            book_id = int(input("Enter Book ID: "))
            lib.return_book(book_id)

        elif choice == "5":
            title = input("Enter title to search: ")
            lib.search_book(title)

        elif choice == "6":
            book_id = int(input("Enter Book ID to delete: "))
            lib.delete_book(book_id)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()