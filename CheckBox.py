from tkinter import *
top = Tk()
top.title("Hello Python")
top.config(bg="black")
top.geometry("300x200")
c1 = IntVar()
c2 = IntVar()
c3 = IntVar()
cbt1 = Checkbutton(top,text="Cricket",variable=c1,onvalue=1,offvalue=0,height=1,width=10,font=25)
cbt1.place(x=50,y=70)
cbt2 = Checkbutton(top,text="Hockey",variable=c2,onvalue=1,offvalue=0,height=1,width=10,font=25)
cbt2.place(x=130,y=130)
top.mainloop()