

# make a calculator app that does all basic functions
# this will not do anything besides basic arithmatic
# that would take forever
#1> make GUI and buttons (buttons not functional)
#2> make each button functional
#3> make functionality between butons useful to creating
#an actual calculator result
#4> make it look sleek

import tkinter as tk

# Function for buttons

def button_click(number):
    current_text = screenLabel['text']
    screenLabel["text"] = current_text + str(number)

# when C button, clear string
def clear_screen():
    screenLabel["text"] = ""

#beware! 80% sure how this function works
def calculate_result():
    expression = screenLabel["text"]
    try:
        result = eval(expression)
        screenLabel["text"] = str(result)
    except Exception as e:
        screenLabel["text"] = "Error"

#create ui window
window = tk.Tk()
window.title("CalQlator")
screenLabel = tk.Label(window, text="", anchor="e", relief="ridge", width=30)
screenLabel.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
#less repetative code for simple buttons, dictionary will make it easier to format
buttons = {
    "C": (1, 0), "+/-": (1, 1), "%": (1, 2), "/": (1,3),
    "7": (2, 0), "8": (2, 1), "9": (2, 2), "X": (2, 3),
    "4": (3, 0), "5": (3, 1), "6": (3, 2), "-": (3, 3),
    " ": (4, 0), "0": (4, 1), ".": (4, 2), "=": (4, 3)
}
# using the dictionary with row and columns to set up button on grid
#**don't forget to add the screen later
for button_text, (row, column) in buttons.items():
    if button_text == "=":
        button_widget = tk.Button(window, text=button_text, width=5, command=calculate_result)
    elif button_text == "C":
        button_widget = tk.Button(window, text=button_text, width=5, command=clear_screen)
    else:
        button_widget = tk.Button(window, text=button_text, width=5, command=lambda text=button_text: button_click(text))
    button_widget.grid(row = row, column = column, padx=3, pady=5, sticky="nsew")
#buttons don't move when i expand calq app, look up command and lambda to fix?
#need to integrate some type of auto adjust for buttons
#this move the buttons and scree but does not change the size
for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for i in range(5):
    window.grid_rowconfigure(0, weight=1)



window.mainloop()