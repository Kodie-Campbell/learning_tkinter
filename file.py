from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
root = Tk()
root.title("files")

def open():
    global my_label
    global my_image_label
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/gui/images", title="Select a file")
    my_label = Label(root,text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_btn = Button(root, text="Open File", command= open).pack()


root.mainloop()