def books_report(books):
    print("\nBOOKS REPORT")

    if len(books) == 0:
        print("No books registered.")
        return

    for book in books:
        print("\nTitle:", book["title"])
        print("Author:", book["author"])
        print("ISBN:", book["isbn"])
        print("Quantity:", book["quantity"])
        print("Available:", book["available"])


def active_loans_report(loans):
    print("\nACTIVE LOANS REPORT")
    found = 0

    for loan in loans:
        if loan["returned"] == False:
            print("\nLoan ID:", loan["loan_id"])
            print("Student ID:", loan["student_id"])
            print("ISBN:", loan["isbn"])
            print("Date:", loan["date"])
            print("Loan period in days:", loan["loan_period"])
            print("Returned:", loan["returned"])
            found = found + 1

    if found == 0:
        print("No active loans.")
