# Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).

def handle_multiple_exceptions():
    try:
        # Try reading a file (file not found error)
        filename = input("Enter the file name to open: ")
        with open(filename, "r") as file:
            content = file.read()
            print(content)

        # Try performing a division operation (division by zero)
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print(f"The result of division is: {result}")

    except FileNotFoundError:
        print("Error: The file was not found. Please check the file name and try again.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except ValueError:
        print("Error: Invalid input! Please enter valid numbers.")

    except Exception as c:
        print(f"An unexpected error occurred: {c}")

handle_multiple_exceptions()
