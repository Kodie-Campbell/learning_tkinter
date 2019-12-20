# import tkinter module for gui
from tkinter import *

# define  the root window
root = Tk()

# this function displays text when it is called by a button
def myClick():
    # creates a label with text
    myLabel = Label(root, text="Look! i clicked a button!")
    # adds the label to the root window
    myLabel.pack()

# creates a button that calls the myClick function
myButton = Button(root, text="Click me!", command=myClick)
# add the button to the root window
myButton.pack()

# main look to keep the window open
root.mainloop()