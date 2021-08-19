from tkinter import *
from PIL import ImageTk
from  tkinter import messagebox
from tkinter import ttk
import pymysql
from StudentRegister import Register
import os
class login:
    def __init__(self,root):
        self.root=root
        self.root.title("login form")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='sky blue')
        # Background Image--------------------
        self.bg=ImageTk.PhotoImage(file="Photo/my.jpg")
        bg_image=Label(self.root, image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
    #------title of the Frame Window--------------------#
        title=Label(self.root,text="Login Form",font=('Guddy old sytle',25,'bold'),bg='yellow',fg='red').place(x=0,y=0,relwidth=1,height=50)
    #-----------Frame Lable------------------------------#
        lframe=LabelFrame(self.root,text='Login Here',font=('Guddy old style',14,'bold'),bg='lightyellow',fg='#033054')
        lframe.place(x=450,y=200,width=600,height=400)
    #------Row 1-------------------#
        lframe.left=ImageTk.PhotoImage(file="Photo/username.png")
        left=Label(lframe, image=lframe.left).place(x=35,y=85)
        
        email=Label(lframe,text="Username",font=('Guddy old style',20),bg='#033054',fg='white').place(x=120,y=100)
        self.txt_email=Entry(lframe,font=('Guddy old style',20),bg='lightgrey')
        self.txt_email.place(x=270,y=100,width=320)
        #------row2------------------#
        lframe.front=ImageTk.PhotoImage(file="Photo/password.png")
        left=Label(lframe, image=lframe.front).place(x=35,y=160)
        password=Label(lframe,text="Password",font=('Guddy old style',20),bg='#033054',fg='white').place(x=120,y=170)
        self.txt_pass=Entry(lframe,font=('Guddy old style',20),bg='lightgrey')
        self.txt_pass.place(x=270,y=170,width=320)
    #-----button----------#
        lframe.btn_login=ImageTk.PhotoImage(file="Photo/login.jpg")
        btn1=Button(lframe,image=lframe.btn_login,bd=0,cursor='hand2',command=self.login).place(x=40,y=240)   

        lframe.btn_forget=ImageTk.PhotoImage(file="Photo/forget.jpg")
        btn=Button(lframe,image=lframe.btn_forget,bd=0,cursor='hand2',command=self.forget_password_window).place(x=340,y=250)
    #--------Register button------------------------#
        btn_register=Button(lframe,text="Register as new user",bd=0,font=('times new roman',18,'bold'),activebackground='green',bg='green',fg='white',cursor='hand2',command=self.Register_window).place(x=340,y=10)
    #----------Function---------------------------------------#
    def clear(self):
        self.cmb_question.current(0)
        self.txt_newpass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_email.delete(0,END)
    def forget_password(self):
        if self.cmb_question.get()=="select" or self.txt_answer.get()=="" or self.txt_newpass.get()=="":
            messagebox.showerror("Error","All fileds are requried",parent=self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="lms")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and question=%s and answer=%s",(self.txt_email.get(),self.cmb_question.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Warning","Please select valid sequrity Q & Ans",parent=self.root2)
                else:
                    cur.execute("update employee set password=%s where email=%s",(self.txt_newpass.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Password reseted login with new password",parent=self.root2)
                    self.clear()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to : {str(es)}",parent=self.root)
    def login(self):
        if self.txt_email.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error","All fileds are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="lms")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and password=%s",(self.txt_email.get(),self.txt_pass.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Warning","Register first then login",parent=self.root)
                    self.Register_window()
                else:
                    messagebox.showinfo("Success",f"Welcome :{self.txt_email.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python Dashbord.py")
            except Exception as es:
                messagebox.showerror("Warning",f"Error due: {str(es)}",parent=self.root)
    def Register_window(self):
        self.root.destroy()
        os.system("python StudentRegister.py") 
    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","username field not be empty",parent=self.root)
        else:
        
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="lms")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s",self.txt_email.get())
                row=cur.fetchone()
            #    print(row)
                if row==None:
                    messagebox.showerror("Warning","Enter the valid email id",parent=self.root)
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("forget password")
                    self.root2.geometry("400x480+655+150")
                    self.root2.config(bg='white')
                    self.root2.focus_force()
                    self.root2.focus_get()
                    t=Label(self.root2,text="Forget Password",font=('Guddy old style',23,'bold'),fg='white',bg='#033054').place(x=0,y=0,relwidth=1,height=50)
                    #----Label Enrtry root 2-------------------#
                    Question= Label(self.root2, text="Security Question", font=('Guddy old style', 21, 'bold'), fg='grey', bg='white').place(x=60, y=80)
                    self.cmb_question=ttk.Combobox(self.root2,font=('times new roman',15),state='readonly',justify=CENTER)
                    self.cmb_question['value']=("select","Select Your pet name","your Birth place","your best firend name")
                    self.cmb_question.current(0) 
                    self.cmb_question.place(x=60,y=140,width=250)
                    
                    answer = Label(self.root2, text="answer", font=('Guddy old style', 23, 'bold'), fg='grey', bg='white').place(x=60, y=170)
                    self.txt_answer=Entry(self.root2,font=('times new roman',19),bg='lightgrey')
                    self.txt_answer.place(x=60,y=230,width=250)
                    
                    newpassword = Label(self.root2, text="New Password", font=('Guddy old style', 23, 'bold'), fg='grey', bg='white').place(x=60, y=270)
                    self.txt_newpass=Entry(self.root2,font=('times new roman',21),bg='lightgrey')
                    self.txt_newpass.place(x=60,y=320,width=250)
                #----------Change passsword button-----------------------------------------#
                    btn_change=Button(self.root2,text="Change Password",font=('Guddy old style',20,'bold'),fg='white',bg='green',cursor='hand2',command=self.forget_password).place(x=60,y=390,width=250)
            except Exception as es:
                messagebox.showerror("Warning",f"Error due: {str(es)}",parent=self.root)
            
            
       
if __name__=="__main__":
    root=Tk()
    obj=login(root)
    root.mainloop()