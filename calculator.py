# This Python script creates a simple command-line calculator.
# It allows users to perform basic arithmetic operations: addition, subtraction, multiplication, and division.

def add(x, y):
    """
    Adds two numbers and returns the sum.
    Args:
        x (float): The first number.
        y (float): The second number.
    Returns:
        float: The sum of x and y.
    """
    return x + y

def subtract(x, y):
    """
    Subtracts the second number from the first and returns the difference.
    Args:
        x (float): The first number.
        y (float): The second number.
    Returns:
        float: The difference between x and y.
    """
    return x - y

def multiply(x, y):
    """
    Multiplies two numbers and returns the product.
    Args:
        x (float): The first number.
        y (float): The second number.
    Returns:
        float: The product of x and y.
    """
    return x * y

def divide(x, y):
    """
    Divides the first number by the second and returns the quotient.
    Handles division by zero error.
    Args:
        x (float): The numerator.
        y (float): The denominator.
    Returns:
        float: The quotient of x divided by y, or an error message if division by zero occurs.
    """
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

def calculator():
    """
    Main function to run the calculator.
    It prompts the user for two numbers and an operation, then displays the result.
    The calculator continues until the user chooses to exit.
    """
    print("Welcome to Simple Python Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        choice = input("Enter choice(1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
        elif choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a valid choice (1/2/3/4/5).")

# Call the calculator function to start the application
if __name__ == "__main__":
    calculator()
