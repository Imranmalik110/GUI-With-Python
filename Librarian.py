from tkinter import *
from tkinter import messagebox
import pymysql
def Register_Data():
    if id.get()=="" or name.get()=="" or email.get()==""  or password.get()=="":
        messagebox.showerror("Warning","All filed reqired")
    else:
        try:
            con=pymysql.connect(host="localhost",user="root",password="",database="lms")
            cur=con.cursor()
            cur.execute("insert into librarian(id,name,email,pass) values(%s,%s,%s,%s)",(
            id.get(),
            name.get(),
            email.get(),
            password.get()
            ))
            con.commit()
            messagebox.showinfo("sucess","Data Added Successfully")
            con.close()
            root.destroy()
    #======Reset Function===================#
    
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}")
            root.destroy()
def add_data():
    global root,id,name,email,password
    root=Tk()
    root.geometry('600x500')
    root.config(bg='light blue')
    con=pymysql.connect(host="localhost",user="root",password="",database="lms")
    cur=con.cursor()
    #----------ID  Label Code--------#
    lbl_id=Label(root,text='ID',font=('times new roman',17),fg='green',bg='white').place(x=40,y=80)
    id=Entry(root,font=('times new roman',20))
    id.place(x=120,y=80)
    #----------Name Label Code---------#
    lbl_name=Label(root,text='Name',font=('times new roman',17),fg='green',bg='white').place(x=40,y=160)
    name=Entry(root,font=('times new roman',20))
    name.place(x=120,y=160)
    #--------Email Label Code-----------------#
    lbl_email=Label(root,text='Email',font=('times new roman',17),fg='green',bg='white').place(x=40,y=220)
    email=Entry(root,font=('times new roman',20))
    email.place(x=120,y=220)
    #---------------Password Label Code------------#
    lbl_pass=Label(root,text='Password',font=('times new roman',17),fg='green',bg='white').place(x=20,y=280)
    password=Entry(root,font=('times new roman',20))
    password.place(x=120,y=280)
   
    #---------Button code--------------------#
    btnadd=Button(root,text='Add Librarian',font=('times new roman',17),command=Register_Data,fg='green',bg='white')
    btnadd.place(x=60,y=350)
    root.mainloop() 

    