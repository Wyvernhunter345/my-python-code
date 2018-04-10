from tkinter import *
from time import sleep
window = Tk()
window.title("Diamond Clicker")
back = Canvas(window, height=30, width=30)
back.pack()
diamonds = 0
def morediamonds():
    global diamonds
    diamonds += 1
    print ("You have " + str(diamonds) + " diamonds!")
def cursorworking():
    global diamonds
    for x in range(20):
        if diamonds < 15:
            print ("Not enough diamonds!")
            break
        diamonds -= 15
        diamonds += 1
        print ("You now have " + str(diamonds) + " diamonds!")
        sleep(1)
def minerworking():
    global diamonds
    diamonds -=15
Cursor = Button(window, text="Cursor: Clicks every second (Cost: 15). Lasts 20 seconds.", command=cursorworking) 
PlusOneDiamonds = Button(window, text="+1 Diamond", command=morediamonds)
PlusOneDiamonds.pack()
Cursor.pack()
