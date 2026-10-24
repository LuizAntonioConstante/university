print("Palindrome check")

error = True
word = " "

while error:
    if word.count(" ") != 0:
        word = input("Enter the word: ").lower()
    else:
        error = False

wordreverse = word[::-1]

if word == wordreverse:
    print(f"The word {word} is an palindrome")

else:
    print(f"The word {word} is not an palindrome")

