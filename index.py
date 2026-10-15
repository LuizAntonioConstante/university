print("#" * 50)
print("WELCOME TO THE CENTER OF MY UNIVERSITY PROGRAM'S")
print("#" * 50)

error = True

while error:
    option = int(input("""
***** Select the option if you need: ***** 

    1- Activities
    2- Little Projects - PYTHON

    9- EXIT


    Select: """))
    match option:
        case 1:
            error = False
            print("=" * 50)
            print("These are the activities I use to understand the concepts.")
            print("=" * 50)
        
        case 2:
            error = False
            print("=" * 50)
            print("These are small projects I develop to improve my skills.")
            print("=" * 50)
        
        case 9:
            error = False
            print("=" * 50)
            print("Exiting the program...")
            print("=" * 50)

        case _:
            print("=" * 50)
            print(" Select a valid option!!! ".center(45," "))
            print("=" * 50)
