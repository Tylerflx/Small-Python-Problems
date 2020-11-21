# this program is simple and fast to practice tkinter
# we will have a box and let user to input the email to check if email is validate
# we will use validate_email package

from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmsg
from validate_email import validate_email

# build GUI for the program
root = Tk()

# title for the app
root.title("Validate Email App")

# box dimension
root.geometry("600x600")

# heading
label = Label(root, text="Email Verification using Python Tkinter!").pack()

var = StringVar()

def display():
    email = var.get()
    if(validate_email(email)):
        # if it valid
        tmsg.showinfo("Result", f"{email} you entered is valid!")
    else:
        tmsg.showinfo("Result", f"{email} you entered is invalid!")

# use textvariable to set the value
ttk.Entry(root, width="50", textvariable=var).pack()
Button(root, text="Check", command=display).pack()


root.mainloop()