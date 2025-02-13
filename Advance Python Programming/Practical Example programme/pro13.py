# Write a Python program to show hierarchical inheritance.

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Derived class 1
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Derived class 2
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Derived class 3
class Cow(Animal):
    def speak(self):
        return f"{self.name} says Moo!"

# Creating objects of each derived class
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")

# Calling the speak method for each object
print(dog.speak())  
print(cat.speak())  
print(cow.speak())  
