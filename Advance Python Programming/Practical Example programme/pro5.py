# Write a Python program to read a file and print the data on the console.

# Open the file in read mode
with open("example.txt", "r") as file:
    # Read the contents of the file
    content = file.read()

# Print the file contents to the console
print(content)
