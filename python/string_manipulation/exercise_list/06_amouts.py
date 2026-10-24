print('Select the texto to calcule amout of things')

text = input('Enter your text: ')

charamout = text.replace(" ","")
charamout = len(charamout)

wordamout = text.split()
wordamout = len(wordamout)

print(f'Haves {charamout} characters in your text')
print(f'Haves {wordamout} words in your text')

