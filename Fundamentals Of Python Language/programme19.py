'''Write a Python program to get a string made of the first 2 and the last
2 chars from a given a string. If the string length is less than 2, return
instead of the empty string. '''

string = input("Enter the string :")
count=0
for i in string:
    count=count+1
    new = string [0:2]+ string [count-2: count]
    print("new formed string is : ", new)
