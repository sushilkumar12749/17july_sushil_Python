# Write a Python program to demonstrate handling multiple exceptions.

def handle_multiple_exceptions():
    try:
        # Take user input for a number and perform some operations
        num = input("Enter a number: ")

        # Try to convert the input to an integer
        num = int(num)
        result = 10 / num
        print(f"Result of division: {result}")

    except ValueError:
        print("Error: Invalid input! Please enter a valid integer.")
    
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function to demonstrate exception handling
handle_multiple_exceptions()
