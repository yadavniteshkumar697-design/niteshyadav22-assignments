import csv


class Book:
    def __init__(self, title, book_id, author):
        self.title = title
        self.book_id = book_id
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.book_id} | {self.title} | {self.author} | {status}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to {self.name}")

    def show_books(self):
        print(f"\nBooks in {self.name}:")

        if len(self.books) == 0:
            print("No books available.")
        else:
            for book in self.books:
                print(book)


# Create multiple libraries
lib1 = Library("Central Library")
lib2 = Library("Computer Science Library")
lib3 = Library("Digital Library")


# Add multiple books to Library 1
lib1.add_book(Book("Python Basics", "B001", "John Smith"))
lib1.add_book(Book("Clean Code", "B002", "Robert Martin"))


# Add multiple books to Library 2
lib2.add_book(Book("Python Crash Course", "B003", "Eric Matthes"))
lib2.add_book(Book("Artificial Intelligence", "B004", "Stuart Russell"))


# Add multiple books to Library 3
lib3.add_book(Book("Machine Learning", "B005", "Tom Mitchell"))
lib3.add_book(Book("Deep Learning", "B006", "Ian Goodfellow"))


# Show books on screen
lib1.show_books()
lib2.show_books()
lib3.show_books()


# Save all libraries and books to CSV
with open("libraries.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # CSV header
    writer.writerow(["Library", "Book ID", "Title", "Author", "Status"])

    # Save Library 1
    for book in lib1.books:
        writer.writerow([
            lib1.name,
            book.book_id,
            book.title,
            book.author,
            "Borrowed" if book.is_borrowed else "Available"
        ])

    # Save Library 2
    for book in lib2.books:
        writer.writerow([
            lib2.name,
            book.book_id,
            book.title,
            book.author,
            "Borrowed" if book.is_borrowed else "Available"
        ])

    # Save Library 3
    for book in lib3.books:
        writer.writerow([
            lib3.name,
            book.book_id,
            book.title,
            book.author,
            "Borrowed" if book.is_borrowed else "Available"
        ])


print("\nData saved to libraries.csv")


# View entries from CSV
print("\nEntries in CSV file:")

with open("libraries.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)