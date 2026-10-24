def read_integer(message, minimum):
    while True:
        try:
            number = int(input(message))
            if number >= minimum:
                return number
            print("Invalid! The value is below the minimum.")
        except ValueError:
            print("Invalid! Enter a whole number.")


def is_valid_isbn(isbn):
    digits = isbn.replace("-", "")

    if len(digits) != 13:
        return False

    for character in digits:
        if character < "0" or character > "9":
            return False

    return True
