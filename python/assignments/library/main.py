from validations import read_integer
from books import register_book
from loans import make_loan, return_book
from reports import books_report, active_loans_report

books = []
loans = []

option = -1

while option != 0:
    print("\n LIBRARY SYSTEM ")
    print("1 - Register book")
    print("2 - Make a loan")
    print("3 - Return book")
    print("4 - Books report")
    print("5 - Active loans report")
    print("0 - Exit")

    option = read_integer("Choose an option: ", 0)

    if option == 1:
        register_book(books)
    elif option == 2:
        make_loan(books, loans)
    elif option == 3:
        return_book(books, loans)
    elif option == 4:
        books_report(books)
    elif option == 5:
        active_loans_report(loans)
    elif option == 0:
        print("Closing system.")
    else:
        print("Invalid option.")
