import time
from tkinter import *
from tkinter import ttk
from threading import *

frameWidth = 120  # ширина страницы
frameHeigth = 340  # высота страницы
ovalRadius = 50  # радиус кругов
c = 10  # растояние кругов от стенки
diff = 5  # растояние между шарами

redTime = 5
yellowTime = 2
greenTime = 5

frame = Tk()
canvas = Canvas(frame, width=frameWidth, height=frameHeigth)

red = canvas.create_oval(c, c, c + 2 * ovalRadius, c + 2 * ovalRadius, fill="white", outline="black", width=2)
yellow = canvas.create_oval(c, diff + c + 2 * ovalRadius, c + 2 * ovalRadius, diff + c + 4 * ovalRadius, fill="white",
                            outline="black", width=2)
green = canvas.create_oval(c, 2 * diff + c + 4 * ovalRadius, c + 2 * ovalRadius, 2 * diff + c + 6 * ovalRadius,
                           fill="white", outline="black", width=2)
greenTimer = Label(background="white", font="Arial 25 normal roman")
redTimer = Label(background="white", font="Arial 25 normal roman")

def setRed():
    canvas.itemconfig(red, fill="red")
    canvas.itemconfig(yellow, fill="white")
    canvas.itemconfig(green, fill="white")
    greenTimer.config(background="white")
    greenTimer.config(text="")
    redTimer.config(background="red")

def setYellow():
    canvas.itemconfig(yellow, fill="yellow")
    canvas.itemconfig(green, fill="white")

def setGreen():
    canvas.itemconfig(red, fill="white")
    canvas.itemconfig(yellow, fill="white")
    canvas.itemconfig(green, fill="green")
    greenTimer.config(background="green")
    redTimer.config(background="white")
    redTimer.config(text="")

cnt = 5
def color():
    while True:
        setRed()
        for i in range(redTime-yellowTime):
            redTimer.config(text=str(redTime-i))
            time.sleep(1)

        setYellow()
        for i in range(yellowTime):
            redTimer.config(text=str(yellowTime-i))
            time.sleep(1)

        setGreen()
        for i in range(greenTime):
            greenTimer["text"] = str(greenTime - i)
            greenTimer.update()
            time.sleep(1)

thr = Thread(target=color, args=())
thr.start()

redTimer.place(x=48, y=40)
greenTimer.place(x=48, y=250)
canvas.pack()
frame.mainloop()
