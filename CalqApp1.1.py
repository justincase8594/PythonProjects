# getting rid of "X" for "*" to use less code (also I feel like it would come back to haunt me if I kept it.)
# got rid of "+/-", and the "%" for the sake of time and siplicity so I stop banging my head against the same
# problems and move forward.
# my partner thinks it should be green because she likes that color, so I'll make it green (challenge accepted?)


#importing ttk for color changes (maybe style chages)

import tkinter as tk
from tkinter import ttk





# Function for number button clicks
def button_click(number):
    
    current_text = screenLabel['text']
    screenLabel["text"] = current_text + str(number)

# Function to clear the screen
def clear_screen():
    screenLabel["text"] = ""

# Function to calculate the result
def calculate_result(event=None):
    expression = screenLabel["text"]
    try:
        result = eval(expression)
        screenLabel["text"] = str(result)
    except Exception as e:
        screenLabel["text"] = "Error"

f"""def calculate_result():
    expression = screenLabel["text"]
    try:
        result = eval_expression(expression)
        screenLabel["text"] = str(result)
    except Exception as e:
        screenLabel["text"] = "Error"""

# Function to evaluate the expression
def eval_expression(expression):
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    tokens = expression.split()
    stack = []

    for token in tokens:
        if token.isdigit():
            stack.append(float(token))
        elif token in operators:
            if len(stack) < 2:
                raise ValueError("Invalid expression")
            y = stack.pop()
            x = stack.pop()
            result = operators[token](x, y)
            stack.append(result)
        else:
            raise ValueError("Invalid expression")

    if len(stack) != 1:
        raise ValueError("Invalid expression")

    return stack[0]

# Create UI window
window = tk.Tk()
window.title("CalQlator")
window.configure(bg="green")

# Create screen label
screenLabel = tk.Label(window, text="", anchor="e", relief="ridge", width=30)
screenLabel.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# Define button positions in a dictionary
buttons = {
    "C": (1, 0), "": (1, 1), "*": (1, 2), "/": (1, 3),
    "7": (2, 0), "8": (2, 1), "9": (2, 2), "+": (2, 3),
    "4": (3, 0), "5": (3, 1), "6": (3, 2), "-": (3, 3),
    " ": (4, 0), "0": (4, 1), ".": (4, 2), "=": (4, 3)
}

# Create buttons and assign functions to them
for button_text, (row, column) in buttons.items():
    if button_text == "=":
        button_widget = tk.Button(window, text=button_text, width=5, command=calculate_result)
    elif button_text == "C":
        button_widget = tk.Button(window, text=button_text, width=5, command=clear_screen)
    elif button_text == "/":
        button_widget = tk.Button(window, text=button_text, width=5, command=lambda: perform_operation("/"))
    elif button_text == "*":
        button_widget = tk.Button(window, text=button_text, width=5, command=lambda: perform_operation("*"))
    else:
        button_widget = tk.Button(window, text=button_text, width=5, command=lambda text=button_text: button_click(text))
    button_widget.grid(row=row, column=column, padx=3, pady=5, sticky="nsew")

# Configure column and row weights for dynamic button resizing
for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for i in range(5):
    window.grid_rowconfigure(0, weight=1)

# Function to perform the operation
def perform_operation(operator):
    current_text = screenLabel["text"]
    if current_text and not current_text.endswith(operator):
        screenLabel["text"] = current_text + " " + operator
    elif operator:
        screenLabel["text"] = operator





# Start the GUI main loop
window.mainloop()
