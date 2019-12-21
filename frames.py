from tkinter import *
from PIL import ImageTk,Image

root = Tk()

frame = LabelFrame(root, text="This is my frame..", padx=5, pady=5)
frame.pack(padx=10, pady=10)
b = Button(frame, text="dont click here")
b.grid(row=0, column=0)
b = Button(frame, text="dont click here2")
b.grid(row=1, column=1)




root.mainloop()