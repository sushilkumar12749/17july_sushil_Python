#Write a Python program to get a single string from two given strings,
#separated by a space and swap the first two characters of each string.

x = input("Enter a string :")
y = input("Enter a second string :")

print(x, ',', y)
x_new=y[0:2]+x[2:]
y_new=x[0:2]+y[2:]
print(x_new, ',', y_new)
 