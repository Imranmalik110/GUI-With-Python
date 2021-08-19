from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from Course import CourseClass
from Student import StudentClass
from Result import ResultClass
from ViewResult import ReportClass
import os
import pymysql  # pip install pymysql
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x688+0+0")
        self.root.config(bg='white')
        self.logo=ImageTk.PhotoImage(file="Photo/logo.jpg")
        #-------------------------title---Label----------------#
        title=Label(self.root,text="Student Result management System",compound=LEFT,padx=10,font=('Guddy old sytle',23,'bold'),image=self.logo,bg='#033054',fg='white').place(x=0,y=0,relwidth=1,height=50)
        #------Menues Frame-------------------------------#
        M_frame=LabelFrame(self.root,text='Menus',font=('times new roman',15),bg='white')
        M_frame.place(x=10,y=70,width=1340,height=80)
        btn_course=Button(M_frame,text='Course',command=self.Add_course,cursor='hand2',font=('Guddy old style',15,'bold'),bg='#0b5377',fg='white').place(x=20,y=5,width=200,height=40)
        btn_student=Button(M_frame,text='Student',command=self.Add_student,cursor='hand2',font=('Guddy old style',15,'bold'),bg='#0b5377',fg='white').place(x=240,y=5,width=200,height=40)
        btn_result=Button(M_frame,text='Result',command=self.Add_result,cursor='hand2',font=('Guddy old style',15,'bold'),bg='#0b5377',fg='white').place(x=460,y=5,width=200,height=40)
        btn_viewResult=Button(M_frame,text='View Student Result',command=self.view_result,cursor='hand2',font=('Guddy old style',15,'bold'),bg='#0b5377',fg='white').place(x=680,y=5,width=200,height=40)
        btn_logout=Button(M_frame,text='Logout',command=self.Logout,cursor='hand2',font=('Guddy old style',15,'bold'),bg='#0b5377',fg='white').place(x=900,y=5,width=200,height=40)
        btn_exit=Button(M_frame,text='Exit',command=self.Exit_form,cursor='hand2',font=('Guddy old style',15,'bold'),bg='#0b5377',fg='white').place(x=1120,y=5,width=200,height=40)
        #----------------Imge------------#
        self.bg_img=Image.open("Photo/result.jpg")
        self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root ,image=self.bg_img).place(x=400,y=180,width=920,height=350)
        #---------Update Details----------------------#
        self.lbl_student=Label(self.root,text="Total Student\n[0]",font=('Guddy old style',20),bd=10,relief=RIDGE,bg='#e34b06',fg='white')
        self.lbl_student.place(x=400,y=530,width=300,height=100)
        self.lbl_course=Label(self.root,text="Total Course\n[0]",font=('Guddy old style',20),bd=10,relief=RIDGE,bg='#0b5377',fg='white')
        self.lbl_course.place(x=710,y=530,width=300,height=100)
        self.lbl_result=Label(self.root,text="Total Result\n[0]",font=('Guddy old style',20),bd=10,relief=RIDGE,bg='#6495ED',fg='white')
        self.lbl_result.place(x=1020,y=530,width=300,height=100)
        
        #------Footer----------------------------------#
        footer=Label(self.root,text="SRS-Student Result management System\contact us for technical support : 8851247258",font=('Guddy old sytle',23),bg='#262626',fg='white').pack(side=BOTTOM,fill=X)
        self.Update_details()
        self.update_student()
        self.update_result()
    #==============================functions===============================#
    def Update_details(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="lms")
        cur=con.cursor()
        try:
            cur.execute("select * from addcourse")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Course\n[{str(len(cr))}]")
            self.lbl_course.after(200,self.Update_details)
        except Exception as es:
             messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    def update_student(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="lms")
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Student\n[{str(len(cr))}]")
            self.lbl_student.after(200,self.update_student)
        except Exception as es:
             messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    def update_result(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="lms")
        cur=con.cursor()
        try:
            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Result\n[{str(len(cr))}]")
            self.lbl_result.after(200,self.update_result)
        except Exception as es:
             messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    
    def Add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
    def Add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)
    def Add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ResultClass(self.new_win)
    def view_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ReportClass(self.new_win)
    def Logout(self):
        op=messagebox.askokcancel("Confirm","Do you realy want to logout",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python StudentLogin.py")
    def Exit_form(self):
        exit(0)
if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()