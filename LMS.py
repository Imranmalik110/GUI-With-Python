from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
from Librarian import *
from ViewLibrarian import *
# Calander import *
def Admin_menu():
    global window
    window=Tk()
    window.title("Admin Menu")
    window.geometry('1200x600')
    window.config(bg='light blue')
    window.resizable(False,False)
    bg=ImageTk.PhotoImage(file="Photo/summer.jpg")
    bg_image=Label(window, image=bg).place(x=0,y=0,relwidth=1,relheight=1)
#---------------Button code-----------------------#
    lbl=Label(window,text='Admin Menu',cursor='hand2',font=('Guddy old style',23)).place(x=150,y=10)
    btn1=Button(window,text='Add Librarian',cursor='hand2',font=('times new roman',18),bg='white',fg='black',command=add_data).place(x=100,y=80)
    btn2=Button(window,text='view Libarian',cursor='hand2',font=('times new roman',18),bg='white',fg='black',command=view_Data).place(x=350,y=80)
    btn3=Button(window,text='Logout',command=window.destroy,cursor='hand2',font=('times new roman',18),bg='white',fg='black').place(x=550,y=80)
   #s btn4=Button(window,text='Chose date',cursor='hand2',font=('times new roman',18),bg='white',fg='black',command=get_Date).place(x=750,y=80)
    window.mainloop()
Admin_menu()