''' Write a Python program to count the number of characters (character 
frequency) in a string'''

string = input("Enter string :")
print("opreatrion to perforame 1. total length 2. count of chareater ")

choice = input()
if choice == '1':
    print(len(string))
elif choice == '2':
    char = input("Enter chareter :")
    if char in string:
        print(string.count (char))
    else:
        print("chareter not avaliable")
    
else:
    print("invalid choice....")


