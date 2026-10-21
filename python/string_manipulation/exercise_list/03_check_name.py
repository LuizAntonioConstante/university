print("Check cointains name")

name = input("Insert the name to check: ")

nameslice = name.lower().split()
souza = "souza" in nameslice

if souza:
    print(f"The changed name: '{name}' contains 'Souza'")
else:
    print(f"The changed name: '{name}' don't contains 'Souza'")


