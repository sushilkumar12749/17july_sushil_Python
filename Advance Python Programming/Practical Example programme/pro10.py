# Write a Python program to demonstrate the use of local and global variables in a clas

# Global variable
global_var = "I am a global variable"

class VariableDemo:
    def __init__(self):
        # Instance variable (local to the class instance)
        self.instance_var = "I am an instance variable"

    def demonstrate_variables(self):
        # Local variable (local to this method)
        local_var = "I am a local variable"
        
        print(global_var)  # Accessing the global variable
        print(self.instance_var)  # Accessing the instance variable
        print(local_var)  # Accessing the local variable

# Create an instance of the class
demo = VariableDemo()

# Call the method to demonstrate variable usage
demo.demonstrate_variables()