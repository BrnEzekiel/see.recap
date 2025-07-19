Simple Python Calculator
This Python script creates a simple command-line calculator that allows users to perform basic arithmetic operations: addition, subtraction, multiplication, and division.

Features
Basic Arithmetic Operations: Perform addition, subtraction, multiplication, and division.

User-Friendly Interface: Simple command-line interface for easy interaction.

Error Handling: Includes basic error handling for invalid input (non-numeric input) and division by zero.

Continuous Calculation: Allows multiple calculations until the user chooses to exit.

How to Use
Prerequisites
Python 3.x installed on your system.

Running the Calculator
Save the code: Save the provided Python code into a file named calculator.py (or any other .py extension).

Open a terminal or command prompt: Navigate to the directory where you saved the calculator.py file.

Run the script: Execute the script using the Python interpreter:

python calculator.py

Interacting with the Calculator
Once the script is running, you will see a welcome message and a menu of operations:

Welcome to Simple Python Calculator!
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit

Choose an operation: Enter the number corresponding to the operation you want to perform (e.g., 1 for Add, 2 for Subtract, etc.).

Enter numbers: If you choose an arithmetic operation (1-4), you will be prompted to enter two numbers.

View result: The calculator will display the result of the operation.

Continue or Exit: After each calculation, you can choose another operation or enter 5 to exit the calculator.

Example Usage
Enter choice(1/2/3/4/5): 1
Enter first number: 10
Enter second number: 5
10.0 + 5.0 = 15.0
Enter choice(1/2/3/4/5): 4
Enter first number: 20
Enter second number: 0
20.0 / 0.0 = Error! Division by zero is not allowed.
Enter choice(1/2/3/4/5): 5
Exiting calculator. Goodbye!

Project Structure
The project consists of a single Python file:

calculator.py: Contains all the functions for arithmetic operations and the main calculator logic.

Functions
add(x, y): Adds two numbers.

subtract(x, y): Subtracts the second number from the first.

multiply(x, y): Multiplies two numbers.

divide(x, y): Divides the first number by the second, handles division by zero.

calculator(): The main function that runs the calculator loop, handles user input, and displays results.
