from tkinter import *
from tkinter import ttk

frameWidth = 300  # ширина страницы
frameHeigth = 300  # высота страницы
ovalRadius = 30  # радиус кругов
c = 10  # растояние кругов от стенки
diff = 5  # растояние между шарами

frame = Tk()
canvas = Canvas(frame, width=frameWidth, height=frameHeigth)

red = canvas.create_oval(c, c, c + 2 * ovalRadius, c + 2 * ovalRadius, fill="white", outline="black", width=2)
yellow = canvas.create_oval(c, diff + c + 2 * ovalRadius, c + 2 * ovalRadius, diff + c + 4 * ovalRadius, fill="white",
                            outline="black", width=2)
green = canvas.create_oval(c, 2 * diff + c + 4 * ovalRadius, c + 2 * ovalRadius, 2 * diff + c + 6 * ovalRadius,
                           fill="white", outline="black", width=2)


def setRed():
    canvas.itemconfig(red, fill="red")
    canvas.itemconfig(yellow, fill="white")
    canvas.itemconfig(green, fill="white")

def setYellow():
    canvas.itemconfig(red, fill="white")
    canvas.itemconfig(yellow, fill="yellow")
    canvas.itemconfig(green, fill="white")

def setGreen():
    canvas.itemconfig(red, fill="white")
    canvas.itemconfig(yellow, fill="white")
    canvas.itemconfig(green, fill="green")


redButton = Button(text="Set red.", command=setRed)
yellowButton = Button(text="Set yellow.", command=setYellow)
greenButton = Button(text="Set green.", command=setGreen)

canvas.pack()

redButton.pack()
yellowButton.pack()
greenButton.pack()

frame.mainloop()
