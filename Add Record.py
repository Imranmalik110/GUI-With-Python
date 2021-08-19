from tkinter import *
from  tkinter import messagebox
import mysql.connector
def Reset():
    exit(0)
def Ok():
    studname=e1.get()
    coursename=e2.get()
    feee=e3.get()
    con=mysql.connector.connect(host="localhost",user="root",password="",database="python")
    cur=con.cursor()

    try:

            sql="insert into record(id,stname,course,fee) values(%s,%s,%s,%s)"
            val=("",studname,coursename,feee)
            cur.execute(sql,val)
            con.commit()
            messagebox.showinfo("Success","Record Insert Successfully")
            studname.delete(0,END)
            coursename.delete(0,END)
            feee.delete(0,END)
    except Exception as e:
        print(e)
        con.rollback()
        con.close()


root=Tk()
root.title("Student Registration")
root.geometry("500x400")
global e1
global e2
global e3

Label(root,text='Student Name').place(x=18,y=10)
Label(root,text='Course').place(x=10,y=40)
Label(root,text='Fee').place(x=10,y=80)
e1 = Entry(root)
e1.place(x=140,y=10)
e2 = Entry(root)
e2.place(x=140,y=40)
e3 = Entry(root)
e3.place(x=140,y=80)
Button(root,text='Add',command=Ok,height=2,width=13).place(x=10,y=120)
Button(root,text='Exit',command=Reset,height=2,width=14).place(x=200,y=120)
root.config(bg='lightgreen')
root.mainloop()