from tkinter import *

root = Tk()
root.title("dropboxes")
root.geometry("400x400")

def show():
    mylabel = Label(root, text=clicked.get())
    mylabel.pack()


options = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday"
]
clicked = StringVar()

clicked.set(options[0])
drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="show selection", command=show)
myButton.pack()







root.mainloop()
