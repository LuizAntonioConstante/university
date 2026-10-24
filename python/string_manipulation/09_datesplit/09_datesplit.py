print("Working with date and semester")

error = True


while error:
    date = input("Select the date to discover what semester it has: ")
    datesplited = date.split("/")

    if (
        date.count("/") == 2
        and len(datesplited) == 3
        and all(value.isdigit() for value in datesplited)
        and len(datesplited[0]) == 2
        and len(datesplited[1]) == 2
    ):

        day = int(datesplited[0])
        mouth = int(datesplited[1])
        year = int(datesplited[2])
        
        if (day <= 31 and mouth <= 12):
            error = False

        else:
            print("The entered date is invalid")
    else:
        print("Its not on the date format")

print(f"The selected day is {day}")
print(f"The selected mouth is {mouth}")
print(f"The selected year is {year}")

if mouth < 7:
    print("Your date is on first semester")
else:
    print("Your date is on second semester")



