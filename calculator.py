# imports the tkinter module for gui
from tkinter import *

# creates the root window
root = Tk()
# adds a title to the root window
root.title("Simple Calculator ")

# creates a entry box for user input
e = Entry(root, width=35, borderwidth=5)
# add the entry box to the window
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# this function gets user input and adds it the entry box
def button_click(number):
    # this variable stores the current entry
    current = e.get()
    # clears the current number from the entry box
    e.delete(0, END)
    # appends the new number on the the original entry
    e.insert(0,str(current) + str(number))

# this function clears the text box
def button_clear():
    e.delete(0, END)

# this function stores the contents of the entry box to a global variable
# and assigns a gobal variable to choose the math operation to preform later
def button_add():
    # gets the number from the entry box
    first_number = e.get()
    # define global variable to store the number
    global f_num
    # assigns the number as a float to the global variable
    f_num = float(first_number)
    # define global variable for math operations
    global operation
    # sets global variable for addition
    operation = "+"
    # clears the entry box
    e.delete(0, END)

# this function takes the first number from the f_num global variable,
# clears the entry box, gets the math logic from the global operation
# variable, preforms the math logic and displays it in the entry box
def button_equal():
        second_number = e.get()
        e.delete(0, END)
        if operation == "+":
            e.insert(0, f_num + int(second_number))
        elif operation == "-":
            e.insert(0, f_num - int(second_number))
        elif operation == "/":
            e.insert(0, f_num / int(second_number))
        else:
            e.insert(0, f_num * int(second_number))

# identical to he button_addition function but sets operation global
# variable for subtraction
def button_subtract():
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    global operation
    operation = "-"
    e.delete(0, END)

# identical to he button_addition function but sets operation global
# variable for multiplication
def button_multiply():
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    global operation
    operation = "*"
    e.delete(0, END)

# identical to he button_addition function but sets operation global
# variable for division
def button_divide():
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    global operation
    operation = "/"
    e.delete(0, END)

# creates all of the interface number buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
# creates all the buttons for choosing math logic and reciving a result
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=87, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=27, pady=20, command=button_clear)
button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide)

# puts all number buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

# puts all operation and result buttons on the screen
button_clear.grid(row=0, column=3)
button_add.grid(row=4, column=1)
button_equal.grid(row=4, column=2, columnspan=2)
button_divide.grid(row=1, column=3)
button_multiply.grid(row=2, column=3)
button_subtract.grid(row=3, column=3)

# main loop to keep the window open
root.mainloop()