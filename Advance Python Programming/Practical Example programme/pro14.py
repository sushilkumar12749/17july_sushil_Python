# Write a Python program to demonstrate the use of super() in inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        # Call the constructor of the base class
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_info(self):
        # Call the display_info method of the base class
        super().display_info()
        print(f"Employee ID: {self.employee_id}")

# Create an instance of Employee
employee = Employee("John Doe", 30, "E12345")

