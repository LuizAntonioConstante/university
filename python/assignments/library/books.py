from validations import read_integer, is_valid_isbn


def find_book(books, isbn):
    for book in books:
        if book["isbn"] == isbn:
            return book

    return None


def register_book(books):
    print("\nBOOK REGISTRATION")

    isbn = input("Enter ISBN: ").strip()
    isbn = isbn.replace("-", "")

    if is_valid_isbn(isbn) == False:
        print("Invalid! ISBN must contain 13 digits.")
        return

    if find_book(books, isbn) != None:
        print("Invalid! This book is already registered.")
        return

    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()

    if title == "" or author == "":
        print("Invalid! Title and author are required.")
        return

    quantity = read_integer("Number of copies: ", 0)

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "quantity": quantity,
        "available": quantity
    }

    books.append(book)
    print("Book registered successfully.")
