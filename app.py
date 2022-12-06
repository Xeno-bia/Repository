from tkinter import *
from tkinter import ttk

root = Tk()
root.attributes("-zoomed", "1")

a1 = Label(root, text="title", font="Arial, 50", bg="red")
a1.place(x=50, y=100)

b1 = Label(root, text="1", font="Arial, 50")
b1.place(x=50, y=300)

c1 = Label(root, text="2", font="Arial, 50")
c1.place(x=50, y=500)

d1 = Label(root, text="3", font="Arial, 50")
d1.place(x=50, y=700)

root.mainloop()