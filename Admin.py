from tkinter import *
from tkinter import messagebox
import pymysql
from LMS import *
    #------Code verify----#
def check():
    if email.get()==""  or password.get()=="":
        messagebox.showerror("Error","Email id and password must not be empty")
    else:
        try:
            con=pymysql.connect(host="localhost",user="root",password="",database="lms")
            cur=con.cursor()
            cur.execute("select * from adminlogin where email=%s",email.get())
            row=cur.fetchone()
            if row!=None:
                messagebox.showinfo("Success","Admin login successfully")
                window.destroy()
                Admin_menu()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}")
               
def Admin_Login():
    global window,email,password
    window=Tk()
    window.title("Admin Menu")
    window.geometry('600x400')
    window.config(bg='light blue')
    window.resizable(False,False)
     #--------Username Label Code-----------------#
    lbl_email=Label(window,text='Email',font=('times new roman',17),fg='green',bg='white').place(x=40,y=80)
    email=Entry(window,font=('times new roman',20))
    email.place(x=180,y=80)
    #---------------Password Label Code------------#
    lbl_pass=Label(window,text='Password',font=('times new roman',17),fg='green',bg='white').place(x=40,y=160)
    password=Entry(window,font=('times new roman',20))
    password.place(x=180,y=160)

    #------Buttton lable---------------------------#
    btn=Button(window,text='login',command=check,font=('Guddy old style',21,'italic'),fg='green',bg='white')
    btn.place(x=120,y=220)
    btn1=Button(window,text='Exit',font=('Guddy old style',21,'italic'),fg='green',bg='white',command=window.destroy).place(x=220,y=220)
    window.mainloop()
def clear_field():
    email.delete(0,END)
    password.delete(0,END)
Admin_Login()