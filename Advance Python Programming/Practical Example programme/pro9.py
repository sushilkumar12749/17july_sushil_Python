# Write a Python program to create a class and access the properties of the class using an object.

# Define a class named 'Person'
class Person:
    # Initialize the class with a constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display the person's details
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Create an object of the class 'Person'
person1 = Person("Alice", 30)

# Access the properties of the class using the object
print(f"Person's Name: {person1.name}")
print(f"Person's Age: {person1.age}")

# Call the method to display details
person1.display_details()

