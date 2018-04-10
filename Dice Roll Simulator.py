# Dice Roller
from tkinter import *
from random import randint
window = Tk()
window.title("Dice Roller")
textwindow = Text(window, width=1, height=1,)
def roll1dice():
    textwindow.delete(0.0, END)
    textwindow.insert(END, str(randint(1,6)))
def roll2dice():
    textwindow.delete(0.0, END)
    textwindow.insert(END, str(randint(2,12)))
roll1button = Button(window, text="Roll 1 dice", command=roll1dice)
roll2button = Button(window, text="Roll 2 dice", command=roll2dice)
textwindow.pack()
roll1button.pack()
roll2button.pack()
# Copyright Jaiden Spencer 2015 © All rights Reserved.

