# imports the tkinter module for gui
from tkinter import *

# creates the main window
root = Tk()

# creates a variable for a text entry box
e = Entry(root, width=50)
# adds the text entry box to the window
e.pack()
# adds default text into the entry box
e.insert(0, "Enter your name: ")

# this function gets the input from the text box and uses it
# to print a message
def myClick():
    # add text to the users entry and stores it in a variable
    hello = "Hello " + e.get()
    # creates a label with the variables text
    myLabel = Label(root, text= hello)
    # adds the label to the window
    myLabel.pack()

# creates a button to call the myClick function
myButton = Button(root, text="submit", command=myClick)
# adds the button to the widow
myButton.pack()

# main loop to keep the window open
root.mainloop()