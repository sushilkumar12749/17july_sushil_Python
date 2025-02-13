#  Write a Python program to create a class and access its properties using an object.

# Define a class named 'Person'
class Person:
    # Constructor to initialize name and age
    def __init__(self, name, age):
        self.name = name  # Property for name
        self.age = age    # Property for age

    # Method to display person's information
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Create an object of the 'Person' class
person1 = Person("Alice", 30)

# Accessing properties using the object
print("Accessing properties through object:")
print(f"Name: {person1.name}")
print(f"Age: {person1.age}")

# Calling the method to display information
print("\nCalling the method to display info:")
person1.display_info()
