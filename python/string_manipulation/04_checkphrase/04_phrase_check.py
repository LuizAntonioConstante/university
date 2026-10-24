print('Is this the phrase check the letter "A"')

phrase = input('Insert the phrase to see intersting information: ')

countletter = 0

countletter += phrase.count('a')
countletter += phrase.count('A')

phrase_lower = phrase.lower()

if countletter > 0:
    print(f'The letter "A" apper {countletter} times')
    phraseletterfirst = phrase_lower.find("a")
    print(f"First occurrence of the letter {phraseletterfirst}")

    phraseletterlast = phrase_lower.rfind("a")
    print(f"Last occurrence of the letter {phraseletterlast}")

else:
    print("Don't apper letter A in the phrase")


