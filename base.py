from tkinter import *

root= Tk()
root.title("first window")



def open():
    global lbl
    top = Toplevel()
    top.title("second window")
    lbl = Label(top, text="hello world").pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()
btn =Button(root, text="open second window", command= open).pack()



root.mainloop()