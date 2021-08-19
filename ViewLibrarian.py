from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
def view_Data():
    global window,table
    window=Tk()
    window.title("view Librarian")
    window.geometry("800x500")
    window.config(bg="crimson")
    btn=Button(window,text='BACK',font=('Guddy old style',23,'bold'),fg='yellow',bg='black',command=window.destroy,cursor='hand2').place(x=300,y=400)
    table=ttk.Treeview(window,columns=("id","student_name","email","pass"))
    table.heading("id",text="ID")
    table.heading("student_name", text="Librain Name")
    table.heading("email", text="Email")
    table.heading("pass",text="Password")
    table['show']="headings"
    table.pack()
    # --------------- Database Connection Establishment-------------#
    con=pymysql.connect(host="localhost",user="root",password="",database="lms")
    cur=con.cursor()
    cur.execute("select * from librarian")
    rows=cur.fetchall()
    if len(rows) !=0:
        table.delete(*table.get_children())
        for row in rows:
            table.insert('',END,values=row)  
    con.commit()
    #    messagebox.showinfo("data fetch successfully")
    con.close()
    window.mainloop()

