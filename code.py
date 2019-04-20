import cv2
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Frame
from PIL import ImageTk, Image
import tkinter.filedialog as tkfd
import os

white = "#ffffff"
lightBlue2 = "#adc5ed"
font = "Constantia"
fontButtons = (font, 12)
maxWidth = 830
maxHeight = 570

# Graphics window
mainWindow = tk.Tk()
mainWindow.configure(bg=lightBlue2)
mainWindow.title("Face Recognization")
mainWindow.geometry('%dx%d+%d+%d' % (maxWidth, maxHeight, 0, 0))
mainWindow.resizable(0, 0)
# mainWindow.overrideredirect(1)

mainFrame = Frame(mainWindow)
mainFrame.place(x=10, y=10)

# Capture video frames
lmain = tk.Label(mainFrame)
lmain.grid(row=0, column=0)

# cv2 and Video Path
cap = cv2.VideoCapture(0)


def show_frame():
    ret, frame = cap.read()

    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    img = Image.fromarray(cv2image).resize((800, 400))
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(20, show_frame)


# end of video function

def show_detail():
    # Image and Person Details
    canvas = Canvas(mainWindow, width=100, height=120)
    canvas.place(x=10, y=430)
    img = PhotoImage(file="2.png")
    canvas.create_image(20, 20, anchor=NW, image=img)
    # End of Image
    Lname = Label(mainWindow, text="Name:", font=fontButtons, )
    Lname.place(x=115, y=430)
    LPhone = Label(mainWindow, text="Phone:", font=fontButtons, )
    LPhone.place(x=115, y=455)
    # Function to show details
    match_detail()


def match_detail():
    # Getting Details from Database and show it in Fields
    LnameS = Label(mainWindow, text="Unknow Person ", font=fontButtons, )
    LnameS.place(x=175, y=430)
    LPhoneS = Label(mainWindow, text="0304000000", font=fontButtons, )
    LPhoneS.place(x=175, y=455)


def add_detail():
    # End of Image
    Lname = Label(mainWindow, text="Name:", font=fontButtons, )
    Lname.place(x=560, y=430)
    LPhone = Label(mainWindow, text="Phone:", font=fontButtons, )
    LPhone.place(x=560, y=455)
    Limage = Label(mainWindow, text="Image:", font=fontButtons, )
    Limage.place(x=560, y=480)
    # Function to add details
    insert_details()


def insert_details():
    # Get Details from Input Fields and insert it into database
    name = Entry(mainWindow)
    name.place(x=620, y=430)
    phone = Entry(mainWindow)
    phone.place(x=620, y=455)

    imageBtn = Button(mainWindow, text="Select File..", command=filedialog)
    imageBtn.place(x=620, y=480)

    InsertBtn = Button(mainWindow, text="ADD ", font=fontButtons, bg=white, width=10, height=1)
    # # InsertBtn.configure (command=lambda: mainWindow.destroy ())
    InsertBtn.place(x=620, y=520)


def filedialog():
    mainWindow.filename = tkfd.askopenfilename(initialdir="/", title="Select file ",
                                               filetypes=(("jpeg files", ".jpg"), ("all files", ".")))


# Close Button
def closeBtn():
    closeButton = Button(mainWindow, text="CLOSE", font=fontButtons, bg=white, width=10, height=1)
    closeButton.configure(command=lambda:mainWindow.destroy())
    closeButton.place(x=115, y=520)


show_frame()  # Display
show_detail()
add_detail()
closeBtn()
mainWindow.mainloop()  # Starts GUI
