print('Getting the first name and the last name')

fullname = input('Enter your name: ')

spacename = fullname.split()
namenum = len(spacename)

firstname = spacename[0]
lastname = spacename[namenum-1]

print(firstname)
print(lastname)
