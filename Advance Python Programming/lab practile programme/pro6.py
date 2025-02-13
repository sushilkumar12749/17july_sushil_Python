# Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).

def simple_calculator():
    try:
        # Take input for two numbers and the operation
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        # Perform the selected operation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation. Please choose +, -, *, or /.")

        # Print the result
        print(f"The result is: {result}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Call the function to run the calculator
simple_calculator()

