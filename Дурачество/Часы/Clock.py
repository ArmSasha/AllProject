from tkinter import *
import math
import datetime
def x_coordinate(length, angle):
    return width / 2 + length * math.cos(angle * math.pi / 180)
def y_coordinate(length, angle):
    return height / 2 - length * math.sin(angle * math.pi / 180)
width=600
height=600
radius= 250
root = Tk()
root.title("Часы")
canvas = Canvas(root, width=width, height=height)
canvas.pack()

seconds = canvas.create_line(0, 0, 0, 0, fill = "darkred")
minutes = canvas.create_line(0, 0, 0, 0, fill = "yellow")
hours = canvas.create_line(0, 0, 0, 0, fill = "blue")
def change_hand(length, time, clock_hand, degree):
    alpha = 90 - time * degree
    x1 = x_coordinate(0, alpha)
    y1 = y_coordinate(0, alpha)
    x2 = x_coordinate(length, alpha)
    y2 = y_coordinate(length, alpha)
    canvas.coords(clock_hand, x1, y1, x2, y2)
def update():
    time = str(datetime.datetime.now())
    sec = int(time [17:19])
    minu = int(time [14:16])
    h = int(time[11:13])
    change_hand(radius - 20, sec, seconds, 6)
    change_hand(radius - 30, minu, minutes, 6)
    change_hand(radius - 60, h, hours, 6)
    root.after(1000, update)
alpha = 60
for i in range(1, 13):
    canvas.create_text(x_coordinate(radius + 20, alpha), y_coordinate(radius + 20, alpha), text=i, fill="blue", font="Times 20 italic bold")
    alpha=alpha - 30
for i in range(60):
    x1 = x_coordinate(radius, alpha)
    y1 = y_coordinate(radius, alpha)
    if alpha%30 ==0:
        x2 = x_coordinate(radius -20, alpha)
        y2 = y_coordinate(radius - 20, alpha)
    else:
        x2 = x_coordinate(radius -10, alpha)
        y2 = y_coordinate(radius - 10, alpha)
    alpha=alpha+6
update()
root.mainloop()