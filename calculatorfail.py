# this ultamitaly didn't work because it was thrown together in a protoype
# it worked but has a lot of bugs
# was too much work to try and keep adding code, so I started fresh and used a dictionary
# to map my choices to get rid of the biggest error issue
# was good to get the though down on a file and then reference the good parts 
# and put into the better file

#start writing the easiest thing first which is the functions
#figure out how to fit that into the rest later

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

# Main calculator loop
while True:
    print("---CalQlator---")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("4. Divide")
    print("3. Multiply")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == "1":
        result = add(num1, num2)
        operation = "+"
    elif choice == "2":
        result = subtract(num1, num2)
        operation = "-"
    elif choice == "3":
        result = divide(num1, num2)
        operation = "/"
    elif choice == "4":
        result = multiply(num1, num2)
        operation = "*"
    else:
        print("Invalid choice. Please try again.")
        continue

    print(f"{num1} {operation} {num2} = {result}")