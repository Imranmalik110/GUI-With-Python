from tkinter import *
window =Tk()
window.title("Hello Python")
window.config(bg="black")
window.geometry("300x200")
name=Label(window,text='Name',font=25,bg='pink',fg='grey').place(x=30,y=50)
email=Label(window,text='Email',font=25,bg='pink',fg='green').place(x=30,y=90)
pwd=Label(window,text="Password",font=25).place(x=30,y=130)
sbt1=Button(window,text='Submit',font=25).place(x=30,y=170)
e1=Entry(window).place(x=80,y=50)
e2=Entry(window).place(x=80,y=90)
e3=Entry(window).place(x=95,y=135)
window.mainloop()

