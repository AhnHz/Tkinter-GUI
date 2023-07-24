from tkinter import *

window = Tk()

Label(window,
      text = "Times Font 폰트와 빨강색 사용",
      fg = "red",
      font = "Times 32 bold italic").pack()

Label(window,
      text = "Helvetica 폰트와 녹색 사용",
      fg = "blue",
      bg = "yellow",
      font = "Helvetica 32 bold italic").pack()

window.mainloop() 