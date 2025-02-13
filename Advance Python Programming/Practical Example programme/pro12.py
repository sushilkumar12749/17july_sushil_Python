# ) Write a Python program to show multilevel inheritance

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Derived class (inherits from Animal)
class Mammal(Animal):
    def __init__(self, name, has_fur):
        super().__init__(name)
        self.has_fur = has_fur

    def describe(self):
        fur_status = "has fur" if self.has_fur else "does not have fur"
        return f"{self.name} is a mammal and {fur_status}."

# Further derived class (inherits from Mammal)
class Dog(Mammal):
    def __init__(self, name, has_fur, breed):
        super().__init__(name, has_fur)
        self.breed = breed

    def bark(self):
        return f"{self.name}, the {self.breed}, barks loudly!"

# Creating an instance of Dog
my_dog = Dog("Buddy", True, "Golden Retriever")

# Demonstrating multilevel inheritance
print(my_dog.speak())       # From Animal class
print(my_dog.describe())    # From Mammal class
print(my_dog.bark())        # From Dog class


