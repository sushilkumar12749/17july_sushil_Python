# Write a Python program to read last n lines of a file.

fl=open('Data.txt','a')
fl=open('Data.txt','r')

n=int(input("How many line are you read?: "))

read=fl.readlines()[-n:]
for i in read:
    print(i)