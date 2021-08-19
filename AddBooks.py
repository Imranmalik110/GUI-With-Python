from tkinter import *
from tkinter import messagebox
import pymysql
def addBooks():
    global window,id,title,author,status
    window =Tk()
    window.geometry('800x500')
    window.title("Add Books Menu")
    window.config(bg='#FF5733')
    #-----Title -------------#
    lbl=Label(window,text='Add Book Menu',font=('Guddy old style',24,'bold'),fg='#6495ED',bg='#DFFF00').place(x=0,y=0,relwidth=1,height=50)
    frame=Frame(window,bg='black')
    frame.place(x=100,y=100,width=600,height=350)
    #--------------Id Label Code-----------------#
    lbl_Id=Label(frame,text='ID',font=('Times of Roman',18),fg='#6162ff',bg='white').place(x=40,y=120)
    window.mainloop()
addBooks()