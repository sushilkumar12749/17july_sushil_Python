# Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel, etc.).

# Base class
class Animal:
    def speak(self):
        return "Animal speaks"

# Derived class
class Dog(Animal):
    def bark(self):
        return "Dog barks"

# Create an instance of Dog
dog = Dog()
print(dog.speak())  # Output: Animal speaks
print(dog.bark())   # Output: Dog barks

# Base class 1
class Animal:
    def speak(self):
        return "Animal speaks"

# Base class 2
class Pet:
    def play(self):
        return "Pet plays"

# Derived class
class Dog(Animal, Pet):
    def bark(self):
        return "Dog barks"

# Create an instance of Dog
dog = Dog()
print(dog.speak())  # Output: Animal speaks
print(dog.play())   # Output: Pet plays
print(dog.bark())   # Output: Dog barks

Multilevel Inheritance

In multilevel inheritance, a class is derived from another derived class.

# Base class
class Animal:
    def speak(self):
        return "Animal speaks"

# Intermediate derived class
class Mammal(Animal):
    def walk(self):
        return "Mammal walks"

# Derived class
class Dog(Mammal):
    def bark(self):
        return "Dog barks"

# Create an instance of Dog
dog = Dog()
print(dog.speak())  
print(dog.walk()) 
print(dog.bark())   


