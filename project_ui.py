#header files import gareko
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

#define path of image
test_path = 0

#define functions
def UploadClicked():
    global test_path
    test_path = filedialog.askopenfilename()
    ShowObject(window,test_path,105,105,295,295)

def ShowObject(window, Path,X , Y , Height , Width):
    img = Image.open((Path))
    img = img.resize((Height, Width), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(window, image=img)
    panel.image = img
    panel.pack()
    panel.place(x=X,y=Y)

def showConvertedImg():
    if test_path == 0:
        messagebox.showinfo("Error: Image not Selected", "Please Upload an Image.")
        return 0
    ShowObject(window,test_path, 605,105,295,295)
    
def makeButton(window,text,X,Y,command):
    panel = tk.Button(window,text=text, width=20,command=command)
    panel.pack()
    panel.place(x=X,y=Y)


#initailize window
window=Tk()
window.title("Makaara")
window.geometry('1024x700')
window["bg"] = "#8993a3"

#heading
tk.Label(window, 
		 text="SKETCH TO PHOTO GENERTOR USING CGAN",
		 fg = "#FFFFFF",
		 bg = "#212e42",
		 font = "Helvetica 30 bold ").pack()

#space to input image
canvas = Canvas(window, width=300, height=300)
canvas.pack()
canvas.create_rectangle(0, 0,300,300, fill='black')
canvas.create_rectangle(5, 5,295,295, fill='white')
canvas.place(x=100,y=100)

canvas = Canvas(window, width=300, height=300)
canvas.pack()
canvas.create_rectangle(0, 0,300,300, fill='black')
canvas.create_rectangle(5, 5,295,295, fill='white')
canvas.place(x=600,y=100)

#buttons
makeButton(window,"upload",420,200,UploadClicked)
makeButton(window,"convert",420,300,showConvertedImg)

window.mainloop()
