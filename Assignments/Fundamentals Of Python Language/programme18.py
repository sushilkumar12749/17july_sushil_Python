'''Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead if the string length of the given string is less than 3, leave it
unchanged.'''

text = input("Enetr a string :")

if len(text)<3:
    print(text)
elif text[-3:] == "ing":
    print(text + "ly")
else:
    print(text + "ing")