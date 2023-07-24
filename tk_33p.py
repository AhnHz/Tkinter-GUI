from tkinter import *

window = Tk()

w = Canvas(window, width=400, height=300)
w.pack()

w.create_rectangle(50,25,400,200, fill="gray")
w.create_line(0,0,300,200)
w.create_line(0,0,300,100,fill="red")

mainloop() 