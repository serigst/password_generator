import random
import string
from tkinter import PhotoImage
from tkinter import Label
from tkinter import Tk
from tkinter import E
# from tkinter import W
from tkinter import N
from tkinter import S
from tkinter import Entry
from tkinter import Button

entered_text = ""


def click():
    entered_text = textentry.get()  # collects content from text box




"""
Definition of variables:
"""

count1 = 0
length = 0
leil = 0
amount = 0
filName = 0

"""
count1 = 0
length = int(input("How many characters do you want? : "))
leil = 100
amount = int(input("How many passwords would you like? : "))
filName = str(input("What do you want to name the file?"))
"""

"""
# Defining function for generating passwords
"""


def pwd(pword, count, count1):

    while count != length:
        upper = [random.choice(string.ascii_uppercase)]
        lower = [random.choice(string.ascii_lowercase)]
        num = [random.choice(string.digits)]
        everything = lower + num + upper

        pword += random.choice(everything)
        count += 1
        continue

    if count == length:
        with open(filName+'.txt', 'a') as the_file:
            the_file.write(pword + '\n')
        count1 += 1


# Graphical interface code:

window = Tk()

window.title("Z3RGST's awesome password generator!")

window.configure(background="grey")

photo1 = PhotoImage(file="snake.png")

Label(
    window,
    image=photo1,
    bg="grey"
    ).grid(
        row=0,
        column=0,
        sticky=E)

# Create Label

Label(
    window,
    text="How many passwords do you want? :",
    bg="grey",
    fg="black",
    font="courier 12"
    ).grid(
        row=0,
        column=1,
        sticky=N)


Label(
    window,
    text=entered_text,
    bg="grey",
    fg="red",
    font="courier 16"
    ).grid(
        row=0,
        column=1,
        sticky=N)

textentry = Entry(
    window,
    width=10,
    bg="white",
    font="courier 12"
)

textentry.grid(
    row=0,
    column=2,
    sticky=N
)

Button(
    window,
    text="GO!",
    width=6,
    command="click"
).grid(
    row=1,
    column=2,
    sticky=S
)

"""
Run the main loop
"""
window.mainloop()
