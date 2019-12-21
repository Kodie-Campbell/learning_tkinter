from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("radio buttons")

#r = IntVar()
#r.set(2)

modes = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in modes:
    Radiobutton(root, text=text, variable=pizza, value=mode, command= lambda: clicked(pizza.get())).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


#Radiobutton(root, text="option 1", variable=r, value=1, command= lambda: clicked(r.get())).pack()
#Radiobutton(root, text="option 2", variable=r, value=2, command= lambda: clicked(r.get())).pack()




myLabel = Label(root, text=pizza.get())
myLabel.pack()

root.mainloop()