#  Write a Python program to show single inheritance
# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Derived class
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Creating an instance of the derived class
dog = Dog("Buddy")
print(dog.speak())

