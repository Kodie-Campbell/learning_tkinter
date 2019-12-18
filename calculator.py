from tkinter import *

root = Tk()
root.title("Simple Calculator ")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    global operation
    operation = "+"
    e.delete(0, END)

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

def button_subtract():
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    global operation
    operation = "-"
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    global operation
    operation = "*"
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    global operation
    operation = "/"
    e.delete(0, END)

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
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=87, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=27, pady=20, command=button_clear)
button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide)

# put buttons on screen
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
button_clear.grid(row=0, column=3)
button_add.grid(row=4, column=1)
button_equal.grid(row=4, column=2, columnspan=2)

button_divide.grid(row=1, column=3)
button_multiply.grid(row=2, column=3)
button_subtract.grid(row=3, column=3)


root.mainloop()