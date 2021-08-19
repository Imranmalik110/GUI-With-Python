from tkinter import *
class GUI:
    def __init__(self, win):
        self.lbl1=Label(win, text='First number',fg='Green',width=10,height=1,font=20)
        self.lbl2=Label(win, text='Second number',fg='Blue',height=1,width=12,font=20)
        self.lbl3=Label(win, text='Result',width=10,height=1,font=25,fg='DarkBlue')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.btn1 = Button(win, text='Add')
        self.btn2=Button(win, text='Subtract')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=220, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=220, y=100)
        self.b1=Button(win, text='Add', command=self.add)
        self.b2=Button(win, text='Subtract',command=self.sub)
        self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)
    def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))
    def sub(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))

window=Tk()
mywin=GUI(window)
window.title('Hello Python')
window.config(bg='Black')
window.geometry("400x300+10+10")
window.mainloop()