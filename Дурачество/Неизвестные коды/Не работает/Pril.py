from tkinter import *

tk = Tk()
tk.title('My Gui')
tk.geometry('250x300')
tk.resizable(False,False)
tk.columnconfigure(bg='gray22')

counter = 0
def btn_cmd():

    counter+=1
    btn['text']=counter

btn = Button(root)
btn.configure(bg = 'blue', fg = 'yellow', text = counter, command = btn_cmd())
btn.place(x = 50, y = 100, width = 150, height = 100 )

tk.mainloop()













