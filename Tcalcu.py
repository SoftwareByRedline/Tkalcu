from tkinter import *
import tkinter.font as tkfont
from math import sqrt


mainWindow = Tk()
mainWindow.title("Tkalcu")
mainWindow.config(bg = "black")

operation = StringVar()
character = ""
operationDisplay = Label(text = operation.get(), fg = "white", bg = "black", height = 1 , width = 25)

def addCharacter(character):
    global operation
    operation.set(operation.get() + character)
    operationDisplay.update()
    operationDisplay.config(text = operation.get())

def b1press(arg=0):
    addCharacter("1")
def b2press(arg=0):
    addCharacter("2")
def b3press(arg=0):
    addCharacter("3")

def b4press(arg=0):
    addCharacter("4")
def b5press(arg=0):
    addCharacter("5")
def b6press(arg=0):
    addCharacter("6")
def b7press(arg=0):
    addCharacter("7")
def b8press(arg=0):
    addCharacter("8")
def b9press(arg=0):
    addCharacter("9")
def b0press(arg=0):
    addCharacter("0")

def pluspress(arg = 0):
    addCharacter("+")
def minuspress(arg = 0):
    addCharacter("-")
def multipress(arg = 0):
    addCharacter("*")
def dividepress(arg = 0):
    addCharacter("/")
def powerpress(arg = 0):
    addCharacter("**")
def paropenpress(arg = 0):
    addCharacter("(")
def parclosepress(arg = 0):
    addCharacter(")")
def sqrtpress(arg = 0):
    addCharacter("sqrt(")


buttonWidth = 5



def delchar():
    operation.set(operation.get()[:-1])
    operationDisplay.config(text = operation.get())
    
def clear():
    operation.set("")
    operationDisplay.config(text = operation.get())



def evaluate(arg = 0):
    try:
        resultDisplay.config(text = eval(operation.get()))
    except:
        resultDisplay.config(text = "Error")


buttonBg = "#262626"
opButtonBg = "#4a4a4a"

resultDisplay = Label(text = "", fg = "white", bg = "black", font = 30)


bttn1 = Button(text = "1", fg = "white", bg = buttonBg, width = buttonWidth, command = b1press)
bttn2 = Button(text = "2", fg = "white", bg = buttonBg,width = buttonWidth,command = b2press)
bttn3 = Button(text = "3", fg = "white", bg = buttonBg, width = buttonWidth,command = b3press)
bttn4 = Button(text = "4", fg = "white", bg = buttonBg, width = buttonWidth,command = b4press)
bttn5 = Button(text = "5",fg = "white", bg = buttonBg,  width = buttonWidth,command = b5press)
bttn6 = Button(text = "6", fg = "white", bg = buttonBg, width = buttonWidth,command = b6press)
bttn7 = Button(text = "7", fg = "white", bg = buttonBg, width = buttonWidth,command = b7press)
bttn8 = Button(text = "8", fg = "white", bg = buttonBg, width = buttonWidth,command = b8press)
bttn9 = Button(text = "9",fg = "white", bg = buttonBg,  width = buttonWidth,command = b9press)
bttn0 = Button(text = "0", fg = "white", bg = buttonBg, width = buttonWidth,command = b0press)

delbttn = Button(text = "<-", fg = "white", bg = "red", width = buttonWidth, command = delchar)
clearbttn = Button(text = "C", fg = "white", bg = "red",  width = buttonWidth,command = clear)

equalbttn = Button(text = "=", fg = "white", bg = "lightblue", width = buttonWidth, command = evaluate)

plusbttn = Button(text = "+", fg = "white", bg = opButtonBg,  width = buttonWidth,command = pluspress)
minusbttn = Button(text = "-", fg = "white", bg = opButtonBg,  width = buttonWidth,command = minuspress)
multibttn = Button(text = "*", fg = "white", bg = opButtonBg,  width = buttonWidth,command = multipress)
dividebttn = Button(text = "/", fg = "white", bg = opButtonBg, width = buttonWidth, command = dividepress)

powerbttn = Button(text = "^", fg = "white", bg = opButtonBg,  width = buttonWidth,command = powerpress)
sqrtbttn = Button(text = "Sqrt", fg = "white", bg = opButtonBg, width = buttonWidth, command = sqrtpress)


paropenbttn = Button(text = "(", fg = "white", bg = opButtonBg, width = buttonWidth, command = paropenpress)
parclosebttn = Button(text = ")", fg = "white", bg = opButtonBg,  width = buttonWidth,command = parclosepress)



operationDisplay.grid(row = 0, column = 0, columnspan = 3)
resultDisplay.grid(row = 1, column = 0, columnspan = 3)
bttn1.grid(row = 2, column = 0)
bttn2.grid(row = 2, column = 1)
bttn3.grid(row = 2, column = 2)
bttn4.grid(row = 3, column = 0)
bttn5.grid(row = 3, column = 1)
bttn6.grid(row = 3, column = 2)
bttn7.grid(row = 4, column = 0)
bttn8.grid(row = 4, column = 1)
bttn9.grid(row = 4, column = 2)
bttn0.grid(row = 5, column = 1)
equalbttn.grid(row = 5, column = 2)
delbttn.grid(row = 5, column = 0)
plusbttn.grid(row = 5, column = 3)
minusbttn.grid(row = 4, column = 3)
multibttn.grid(row = 3, column = 3)
dividebttn.grid(row = 2, column = 3)
powerbttn.grid(row = 2, column = 4)
sqrtbttn.grid(row = 3, column = 4)
clearbttn.grid(row = 6, column = 0)

paropenbttn.grid(row = 6, column = 1)
parclosebttn.grid(row = 6, column = 2)

mainWindow.bind("1", b1press)
mainWindow.bind("2", b2press)
mainWindow.bind("3", b3press)
mainWindow.bind("4", b4press)
mainWindow.bind("5", b5press)
mainWindow.bind("6", b6press)
mainWindow.bind("7", b7press)
mainWindow.bind("8", b8press)
mainWindow.bind("9", b9press)
mainWindow.bind("0", b0press)
mainWindow.bind("=", evaluate)
mainWindow.bind("+", pluspress)
mainWindow.bind("-", minuspress)
mainWindow.bind("*", multipress)
mainWindow.bind("/", dividepress)
mainWindow.bind("^", powerpress)
mainWindow.bind("(", paropenpress)
mainWindow.bind(")", parclosepress)


mainloop()
