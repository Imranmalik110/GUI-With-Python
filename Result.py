from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql
class ResultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg='white')
        self.root.focus_force()
        #----------All the Vairble----------------#
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_fullmarks=StringVar()
        self.roll_list=[]
        self.fetch_roll()
#----------Title-----------------------------------#
        title=Label(self.root,text="Add Student Result",font=('Guddy old sytle',20,'bold'),bg='orange',fg='#262626').place(x=0,y=0,relwidth=1,height=50)
#------------Label-------------------------------------#
        lbl_select=Label(self.root,text='Select Student',font=('Guddy old style',20,'bold'),bg='white').place(x=50,y=100)
        lbl_name=Label(self.root,text='Name',font=('Guddy old style',20,'bold'),bg='white').place(x=50,y=160)
        lbl_course=Label(self.root,text='Course',font=('Guddy old style',20,'bold'),bg='white').place(x=50,y=220)
        lbl_marks_obatined=Label(self.root,text='Marks Obtained',font=('Guddy old style',20,'bold'),bg='white').place(x=50,y=280)
        lbl_fullmarks=Label(self.root,text='Full Marks',font=('Guddy old style',20,'bold'),bg='white').place(x=50,y=340)
#---------------ComboBox Entry filed for select course--------------------#
        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=(self.roll_list),font=('Guddy old style',20,'bold'),state='readonly',justify=CENTER)
        self.txt_student.place(x=280,y=100,width=200,height=40)
        self.txt_student.set("Empty")     
#-------------------Search Button----------------------------------------#
        btn_search=Button(self.root,text="Search",font=('Guddy old style',15,'bold'),bg='#2196f3',fg='white',cursor='hand2',command=self.search)
        btn_search.place(x=480,y=100,width=120,height=40)
#---------Entry Field-------------------------------------------#
        txt_name=Entry(self.root,font=('Guddy old style',20,'bold'),textvariable=self.var_name,bg='lightyellow',state='readonly').place(x=280,y=160,width=320)
        txt_course=Entry(self.root,font=('Guddy old style',20,'bold'),textvariable=self.var_course,bg='lightyellow',state='readonly').place(x=280,y=220,width=320)
        txt_marks=Entry(self.root,font=('Guddy old style',20,'bold'),textvariable=self.var_marks,bg='lightyellow').place(x=280,y=280,width=320)
        txt_full_marks=Entry(self.root,font=('Guddy old style',20,'bold'),textvariable=self.var_fullmarks,bg='lightyellow').place(x=280,y=340,width=320)
#----------Button ---------------------------------------------------#
        btn_add=Button(self.root,text='Submit',font=('times new roman',15,'bold'),bg='lightgreen',activebackground='lightgreen',cursor='hand2',command=self.Add).place(x=300,y=420,width=120,height=35)
        btn_clear=Button(self.root,text='Clear',font=('times new roman',15,'bold'),bg='lightgrey',activebackground='lightgrey',cursor='hand2',command=self.clear).place(x=430,y=420,width=120,height=35)
#-------Imagae Tk----------------------------------------------------#
        self.bg_img=Image.open("Photo/rs.jpg")
        self.bg_img=self.bg_img.resize((500,300),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root ,image=self.bg_img).place(x=630,y=100)
#------------Functions---------------------------#
    def fetch_roll(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="lms")
        cur=con.cursor()
        try:
            cur.execute("select roll from student")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as es:
             messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    def search(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="lms")
        cur=con.cursor()
        try:
            cur.execute("select name,course from student where roll=%s",(self.var_roll.get()))
            rows=cur.fetchone()
            if rows!=None:
               self.var_name.set(rows[0])
               self.var_course.set(rows[1])
            else:
                messagebox.showerror("Error","No Record found",parent=self.root)
        except Exception as es:
             messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    def Add(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="lms")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Wraning","please first search student record",parent=self.root)
            else:
                cur.execute("select * from result where roll=%s and course=%s",(self.var_roll.get(),
                        self.var_course.get()
                ))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("warning","Result Already Exists",parent=self.root)
                else:
                    per=(int(self.var_marks.get())*100)/int(self.var_fullmarks.get())
                    cur.execute("insert into result(roll,name,course,marks_ob,full_marks,per) values(%s,%s,%s,%s,%s,%s)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_fullmarks.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Result Added Successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    def clear(self):
                self.var_roll.set("select")
                self.var_name.set("")
                self.var_course.set("")
                self.var_marks.set("")
                self.var_fullmarks.set("")
if __name__=="__main__":
    root=Tk()
    obj=ResultClass(root)
    root.mainloop()