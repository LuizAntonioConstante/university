print("Operate your name")
print("")

name = input("Type your name to operate: ")

#01
print("")
print("a) Name in upper")
print(name.upper())

#02
print("")
print("b) Name in lower")
print(name.lower())

#03
print("")
print("c) Name in capitalized")
print(name.capitalize())

#04
print("")
print("d) Count letter's")
namenospace = name.replace(" ", "")
print(len(namenospace))

#05
print("")
print("e) Count letter's on the first name")
firstname = name.split()[0]
print(len(firstname))
