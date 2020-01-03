from tkinter import *

root = Tk()
root.title("Checkboxes")
root.geometry("400x400")

def show():
    myLable = Label(root, text=var.get())
    myLable.pack()

var = IntVar()


c = Checkbutton(root, text="check this box", variable=var)
c.pack()


myButton = Button(root, text="show selection", command=show)
myButton.pack()


root.mainloop()