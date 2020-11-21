#this program purposely for learning tkinter
# tkinter is GUI package, it's also a cross flatform use on mac, wins, linux
# it looks outdated, old style of website
# light weight, easy to use
# fast and functional

"""This program is a simple GUI to order flight ticket"""
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("600x600")

#label
Label(root,text="Which country you want to travel in?",font="lucidia 19 bold").pack()

#tuple
country = ["Vietnam", "Japan", "China", "Thailand"]

# nonewhere string set by default
var = StringVar()
new_var = var.set("nonewhere")

def travel():
    tmsg.showinfo("Let's travel", f"So, we are booking your flight to {var.get()} \n We wish you a happy trip")

# loop for displaying list of countries
for x in range(4):
    #radio button added to each country
    Radiobutton(root, text=country[x], variable = var, value=country[x]).pack()

#Submit button
Button(root, text="Let's go", command=travel).pack()
root.mainloop()