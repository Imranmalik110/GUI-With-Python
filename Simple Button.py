#       Here We Display some Button Different Color
from tkinter import *
from tkinter import  messagebox
top = Tk()
top.geometry("300x300")
def fun():
    messagebox.showinfo("Hello", "Red Button clicked")
b1 = Button(top,text = "Red",command =fun,activeforeground = "Red",activebackground = "pink",pady = 10)
c1 = Button(top,text = "Green",activeforeground = "Green",activebackground = "pink",pady = 10)
d1 = Button(top,text = "Yellow",activeforeground = "Yellow",activebackground = "pink",pady = 10)
e1 = Button(top,text = "Black",activeforeground = "Black",activebackground = "pink",pady = 10)
b1.pack(side = TOP)
c1.pack(side = LEFT)
d1.pack(side = RIGHT)
e1.pack(side = BOTTOM)
top.mainloop()
