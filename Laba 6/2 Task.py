from tkinter import *
from random import *

frameWidth = 500
frameHeight = 600
cnt = 0
def motion():
    global cnt
    if cnt%100==0:
        canvas.itemconfig(rect, fill="red")
    elif cnt%50==0:
        canvas.itemconfig(rect, fill="blue")
    cnt += 1
    if canvas.coords(rect)[0] > 0:
        canvas.move(rect, -randint(0,frameWidth//100), 0)
    if canvas.coords(rect)[1]>0:
        canvas.move(rect, 0, -randint(0,frameHeight//100))
    if canvas.coords(rect)[2] < frameWidth:
        canvas.move(rect, randint(0,frameWidth//100), 0)
    if canvas.coords(rect)[3]<frameHeight:
        canvas.move(rect, 0, randint(0,frameHeight//100))

    frame.after(10, motion)


frame = Tk()
canvas = Canvas(frame, bg="white", width=frameWidth, height=frameHeight)
rect = canvas.create_rectangle(0,0,50,50, fill="red")

motion()
canvas.pack()
frame.mainloop()
