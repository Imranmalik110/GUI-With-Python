from tkinter import *
from PIL import ImageTk
from  tkinter import messagebox
from tkinter import ttk
import pymysql
import os
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registeration form")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='crimson')
        # Background Image--------------------
        self.bg=ImageTk.PhotoImage(file="Photo/back.jpg")
        bg_image=Label(self.root, image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        # front Image-----------------------
        self.left=ImageTk.PhotoImage(file="Photo/summer.jpg")
        left=Label(self.root, image=self.left).place(x=80,y=100,width=400,height=500)
        # Register Frame----------------------------------------
        frame1=Frame(self.root,bg='white')
        frame1.place(x=480,y=100,width=700,height=500)
#-----------Title frame-------------------------#      
        title = Label(frame1, text="Registration Here", font=('impact', 20, 'bold'), fg='#6162ff', bg='white').place(x=50, y=30)
#-------Row-1--------------------------#
        Lbl_f_name = Label(frame1, text="First Name", font=('Guddy old style', 15, 'bold'), fg='grey', bg='white').place(x=50, y=100)
        self.txt_f_name=Entry(frame1,font=('times new roman',15),bg='lightgrey')
        self.txt_f_name.place(x=50,y=130,width=250)
        
        Lbl_l_name = Label(frame1, text="Last Name", font=('Guddy old style', 15, 'bold'), fg='grey', bg='white').place(x=370, y=100)
        self.txt_l_name=Entry(frame1,font=('times new roman',15),bg='lightgrey')
        self.txt_l_name.place(x=370,y=130,width=250)
#----------Row-2------------------------#        
        contact= Label(frame1, text="Contact No.", font=('Guddy old style', 15, 'bold'), fg='grey', bg='white').place(x=50, y=170)
        self.txt_contact=Entry(frame1,font=('times new roman',15),bg='lightgrey')
        self.txt_contact.place(x=50,y=200,width=250)
        
        email = Label(frame1, text="Email", font=('Guddy old style', 15, 'bold'), fg='grey', bg='white').place(x=370, y=170)
        self.txt_email=Entry(frame1,font=('times new roman',15),bg='lightgrey')
        self.txt_email.place(x=370,y=200,width=250)
#---------Row -3---------------------------#
        Question= Label(frame1, text="Security Question", font=('Guddy old style', 15, 'bold'), fg='grey', bg='white').place(x=50, y=240)
        self.cmb_question=ttk.Combobox(frame1,font=('times new roman',13),state='readonly',justify=CENTER)
        self.cmb_question['value']=("select","Select Your pet name","your Birth place","your best firend name")
        self.cmb_question.current(0) 
        self.cmb_question.place(x=50,y=270,width=250)
       
        answer = Label(frame1, text="answer", font=('Guddy old style', 15, 'bold'), fg='grey', bg='white').place(x=370, y=240)
        self.txt_answer=Entry(frame1,font=('times new roman',15),bg='lightgrey')
        self.txt_answer.place(x=370,y=270,width=250)
#----------Row----pass-----------------------------------------#
        password= Label(frame1, text="Password", font=('Guddy old style', 15, 'bold'), fg='grey', bg='white').place(x=50, y=310)
        self.txt_password=Entry(frame1,font=('times new roman',15),bg='lightgrey')
        self.txt_password.place(x=50,y=340,width=250)
        
        cpassword = Label(frame1, text="confirm password", font=('Guddy old style', 15, 'bold'), fg='grey', bg='white').place(x=370, y=310)
        self.txt_cpassword=Entry(frame1,font=('times new roman',15),bg='lightgrey')
        self.txt_cpassword.place(x=370,y=340,width=250)
#-------Checkbox---------------------------------------------------------#
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I agree the terms & conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg='white',font=('times new roman',14)).place(x=50,y=380)
        
        self.btn_image=ImageTk.PhotoImage(file="Photo/registerButton.jpg")
        btn_register=Button(frame1,image=self.btn_image,bd=0,cursor='hand2',command=self.register_data).place(x=50,y=410)
        
        self.btn_login=ImageTk.PhotoImage(file="Photo/login.jpg")
        btn1=Button(self.root,image=self.btn_login,bd=0,cursor='hand2',command=self.login).place(x=140,y=370)
#------------Function--------------------------------------------------------------------#
    def login(self):
        self.root.destroy()
        os.system("python StudentLogin.py")
    def clear(self):
        self.txt_f_name.delete(0,END)
        self.txt_l_name.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END) 
        self.txt_answer.delete(0,END)
        self.cmb_question.current(0) 
    def register_data(self):
        if self.txt_f_name.get()=="" or self.txt_l_name.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_question.get()=="select" or self.txt_password.get()=="" or self.txt_cpassword.get()=="" or self.txt_answer.get()=="":
                messagebox.showerror("Warning","All filed required",parent=self.root) 
        elif self.txt_password.get()!=self.txt_cpassword.get():
                messagebox.showerror("Error","Password & confirm password does not match",parent=self.root)
        elif self.var_chk.get()==0:
                messagebox.showerror("Error","Please Check I agree the terms & condtions",parent=self.root)
        else:
                try:
                        con=pymysql.connect(host="localhost",user="root",password="",database="lms")
                        cur=con.cursor()
                        cur.execute("select * from employee where email=%s",self.txt_email.get())
                        row=cur.fetchone()
                        if row!=None:
                                messagebox.showinfo("Error","user Already Exits",parent=self.root)
                        else:
                                cur.execute("insert into employee(f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",(
                                        self.txt_f_name.get(),
                                        self.txt_l_name.get(),
                                        self.txt_contact.get(),
                                        self.txt_email.get(),
                                        self.cmb_question.get(),
                                        self.txt_answer.get(),
                                        self.txt_password.get()
                                ))
                                con.commit()
                                con.close()
                                messagebox.showinfo("Success","Register Successfully",parent=self.root)
                                self.clear()
                                self.login()
                except Exception as es:
                        messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()