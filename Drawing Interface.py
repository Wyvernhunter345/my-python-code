# The DRAWING MACHNE (Sorta)
from tkinter import *
import turtle
window = Tk()
def drawup():
    turtle.forward(25)
def turnleft():
    turtle.left(90)
def turnright():
    turtle.right(90)
def turnleft45():
    turtle.left(45)
def turnright45():
    turtle.right(45)
def pendown():
    turtle.pendown()
def penup():
    turtle.penup()
window.title ("Drawing Controls")
textwindow = Label(window, text="Click the buttons to start drawing stuff")
drawupbutton = Button(window, text="Draw Forward", command=drawup)
turnleftbutton = Button(window, text="Turn Left 90 Degrees", command=turnleft)
turnrightbutton = Button(window, text="Turn Right 90 Degrees", command=turnright)
turnleft45button = Button(window, text="Turn Left 45 Degrees", command=turnleft45)
turnright45button = Button(window, text="Turn Right 45 Degrees", command=turnright45)
pendownbutton = Button(window, text="Put Pen Down", command=pendown)
penupbutton = Button(window, text="Put Pen Up", command=penup)
textwindow2 = Label(window, text="Note: Close the Turtle Window and press a button to restart")
textwindow.pack()
drawupbutton.pack()
turnleftbutton.pack()
turnrightbutton.pack()
turnleft45button.pack()
turnright45button.pack()
pendownbutton.pack()
penupbutton.pack()
textwindow2.pack()
