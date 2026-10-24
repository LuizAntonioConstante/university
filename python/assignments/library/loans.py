from datetime import datetime

from books import find_book
from validations import read_integer


def find_loan(loans, loan_id):
    for loan in loans:
        if loan["loan_id"] == loan_id:
            return loan

    return None


def make_loan(books, loans):
    print("\nBOOK LOAN")

    isbn = input("Enter the book ISBN: ").strip()
    isbn = isbn.replace("-", "")

    book = find_book(books, isbn)

    if book == None:
        print("Invalid! Book not found.")
        return

    if book["available"] <= 0:
        print("Invalid! No copies are available.")
        return

    loan_id = read_integer("Loan ID: ", 1)

    if find_loan(loans, loan_id) != None:
        print("Invalid! This loan ID already exists.")
        return

    student_id = input("Student ID (4 digits): ").strip()

    if len(student_id) != 4 or not student_id.isdigit():
        print("Invalid! Student ID must contain 4 digits.")
        return

    date = input("Loan date (DD/MM/YYYY): ").strip()
    date_parts = date.split("/")

    if len(date_parts) != 3:
        print("Invalid date.")
        return

    day, month, year = date_parts

    if len(day) != 2 or len(month) != 2 or len(year) != 4:
        print("Invalid date.")
        return

    if not day.isdigit() or not month.isdigit() or not year.isdigit():
        print("Invalid date.")
        return

    day = int(day)
    month = int(month)
    year = int(year)

    if day < 1 or day > 31 or month < 1 or month > 12 or year < 1:
        print("Invalid date.")
        return

    try:
        datetime.strptime(date, "%d/%m/%Y")
    except ValueError:
        print("Invalid date.")
        return

    loan_period = read_integer("Loan period in days: ", 1)

    loan = {
        "loan_id": loan_id,
        "student_id": student_id,
        "isbn": isbn,
        "date": date,
        "loan_period": loan_period,
        "returned": False
    }

    loans.append(loan)
    book["available"] = book["available"] - 1

    print("Loan created successfully. Loan ID:", loan_id)


def return_book(books, loans):
    print("\nBOOK RETURN")

    loan_id = read_integer("Loan ID: ", 1)
    loan = find_loan(loans, loan_id)

    if loan == None:
        print("Loan not found.")
        return

    if loan["returned"] == True:
        print("This loan has already been returned.")
        return

    book = find_book(books, loan["isbn"])

    if book == None:
        print("The book for this loan was not found.")
        return

    print("Loan ID:", loan["loan_id"])
    print("Title:", book["title"])
    print("Student ID:", loan["student_id"])
    print("Date:", loan["date"])

    confirmation = input("Confirm return? (Y/N): ").strip().upper()

    if confirmation != "Y":
        print("Return cancelled.")
        return

    loan["returned"] = True
    book["available"] = book["available"] + 1

    print("Book returned successfully.")
