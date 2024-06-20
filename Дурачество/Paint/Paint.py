from tkinter import *



canvas_width = 700

canvas_height = 500

brush_size = 3

color = "black"



"""Функция для рисования"""





def paint(event):

    global brush_size

    global color

    x1 = event.x - brush_size

    x2 = event.x + brush_size

    y1 = event.y - brush_size

    y2 = event.y + brush_size

    w.create_oval(x1, y1, x2, y2,

                  fill=color,

                  outline=color)





"""

Функция для изменения размера кисти

"""





def brush_size_change(new_size):

    global brush_size

    brush_size = new_size





"""Функция для изменения цвета кисти"""





def color_change(new_color):

    global color

    color = new_color  # Изменение цвета

    col = Label(root, text=color)

    col.grid(row=0, column=6)



"""

Создание окна и его название

"""

root = Tk()

root.title("Paint")



"""

Создание фона окна

"""

w = Canvas(root, width=canvas_width,

           height=canvas_height, bg="white")



"""

Назначение кнопки для рисования

"""

w.bind("<B1-Motion>", paint)



col = Label(root, text="Цвет кисти")

col.grid(row=0, column=0)




size = Label(root, text="Размер кисти")

size.grid(row=8, column=0)



"""

Кнопки изменяющие размер кисти.

"""

ten_btn = Button(text="Размер 10", width=8, command=lambda: brush_size_change(10))

five_btn = Button(text="Размер 5", width=8, command=lambda: brush_size_change(5))

two_btn = Button(text="Размер 3", width=8, command=lambda: brush_size_change(3))

fiveten_btn = Button(text="Размер 15", width=8, command=lambda: brush_size_change(15))



"""

Кнопки изменяющие цвет кисти

"""

black_btn = Button(text="Черный", width=10, command=lambda: color_change("black"))

red_btn = Button(text="Красный", width=10, command=lambda: color_change("red"))  # Кнопка

green_btn = Button(text="Зеленый", width=10, command=lambda: color_change("green"))

white_btn = Button(text="Ластик", width=10, command=lambda: color_change("white"))

clear_btn = Button(text="Удалить всё", width=10, command=lambda: w.delete("all"))



w.grid(row=2, column=0,

       columnspan=7, padx=5,

       pady=5, sticky=E + W + S + N)

w.columnconfigure(6, weight=1)

w.rowconfigure(2, weight=1)



"""
Расположение кнопок
"""
two_btn.grid(row=8, column=1)

five_btn.grid(row=8, column=2)

ten_btn.grid(row=8, column=3)

fiveten_btn.grid(row=8, column=4)



clear_btn.grid(row=0, column=5)

white_btn.grid(row=0, column=4)

green_btn.grid(row=0, column=3)

black_btn.grid(row=0, column=2)

red_btn.grid(row=0, column=1)



root.mainloop()