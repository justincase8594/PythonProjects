#parts copied from original prototype calculator file to use good peices
# and replace better, less error prone code

# Addition function
def add(x, y):
    return x + y

# Subtraction function
def subtract(x, y):
    return x - y

# Multiplication function
def multiply(x, y):
    return x * y

# Division function
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero!"

# making a dictionary to Map choice to operations
operations = {
    "1": (add, "+"),
    "2": (subtract, "-"),
    "3": (multiply, "*"),
    "4": (divide, "/"),
    "5": () #place holder, otherwise you will get a ""Invalid choice. Please try again."" error
}

# Main calculator loop
while True:
    print("---CalQlator---")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit") 

    choice = input("Enter your choice (1-5): ")

    if choice not in operations:
        print("Invalid choice. Please try again.")
        continue

    if choice == "5":
        break

    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    # Check if the inputs are valid numbers
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Numbers only. Please try again.")
        continue

    operation_func, operation_symbol = operations[choice]
    result = operation_func(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {result}")





