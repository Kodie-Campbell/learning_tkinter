# imports tkinter for gui
from tkinter import *
# imports Pillow to handle images
from PIL import ImageTk,Image

# creates the root window
root = Tk()
# adds a title to the root window
root.title("Adding images")

# imports images from the images folder with Pillow
my_img1 = ImageTk.PhotoImage(Image.open("images/image1.jpeg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/image2.jpeg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/image3.jpeg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/image4.png"))

# adds the images to a list
image_list = [my_img1, my_img2, my_img3, my_img4]

# creates a label with an image
my_lable = Label(image= my_img1)
# adds the label to the screen
my_lable.grid(row=0, column=0, columnspan=3)

# this function changes my_lable to the next image, enables the back button,
# and disables the forward button if it is the last image in the list
def forward(image_number):
    # makes the image lable and navigation buttons global
    global my_lable
    global button_forward
    global button_back

    # removes the current image from the screen
    my_lable.grid_forget()
    # changes my_lable to the next image
    my_lable = Label(image= image_list[image_number-1])

    # changes the arg passed to this function to continue incrementing
    # images
    button_forward = Button(root, text=">>", command= lambda: forward(image_number + 1))
    # enables the back button to call the back function
    button_back = Button(root, text="<<", command= lambda: back(image_number - 1))

    # checks if on last image and disables the forward button
    if image_number == 4:
        button_forward = Button(root, text=">>", state=DISABLED)
    # adds image and navigation button the window
    my_lable.grid(row=0,column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

# this function allows for de-incrementing though the images
def back(image_number):
    global my_lable
    global button_forward
    global button_back

    my_lable.grid_forget()
    my_lable = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root,text="<<", state=DISABLED)

    my_lable.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

# create the initial navigation buttons
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_quit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command= lambda : forward(2))

# adds the initial navigation buttons to the screen
button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

# main loop to keep window open
root.mainloop()