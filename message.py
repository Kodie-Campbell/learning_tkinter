from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message Box")

def popup():
    response = messagebox.askyesno("This is my popup", "Hello World")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked yes").pack()
    else:
        Label(root, text ="You clicked no").pack()
Button(root, text="popup", command=popup).pack()






root.mainloop()