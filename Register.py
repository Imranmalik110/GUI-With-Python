from tkinter import *
from PIL import ImageTk
from  tkinter import messagebox
import pymysql
class Register_Data:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1199x688+100+58")
        # Background Image
        self.bg=ImageTk.PhotoImage(file="Photo/nature.jpg")
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        frame=Frame(self.root,bg='white')
        frame.place(x=330,y=150,width=600,height=450)
        title = Label(frame, text="Registration Here", font=('impact', 35, 'bold'), fg='#6162ff', bg='white').place(x=90, y=30)
        #------------Here User ID Code----#
        lbl_Id=Label(frame,text='ID',font=('Times of Roman',18),fg='#6162ff',bg='white').place(x=40,y=120)
        self.id=Entry(frame,font=('Guddy old style',20),bg='#E7E6E6')
        self.id.place(x=130,y=120)
        #-------------UserName Label------#
        lbl_Username=Label(frame,text='Name',font=('Guddy old style',18),fg='#6162ff',bg='white').place(x=40,y=180)
        self.name=Entry(frame,font=('Guddy old style',20),bg='#E7E6E6')
        self.name.place(x=130,y=180)
        #-------------Course Label -------------#
        lbl_course=Label(frame,text='Course',font=('Guddy old styel',18),fg='#6162ff',bg='white').place(x=40,y=240)
        self.course=Entry(frame,font=('Guddy old style',20),bg='#E7E6E6')
        self.course.place(x=130,y=240)
        #----------Password Label Code---------------#
        lbl_pass=Label(frame,text='Password',font=('Guddy old style',18),fg='#6162ff',bg='white').place(x=40,y=300)
        self.password=Entry(frame,font=('Guddy old style',20),bg='#E7E6E6')
        self.password.place(x=160,y=300)
        #-----------Register Button---------#
        register = Button(frame, text='Register',command=self.Empty, font=('Guddy old style', 20), fg='Green', bg='black',bd=1).place(x=90, y=360)
        Clear=Button(frame, text='Exit form',command=self.Reset,font=('Guddy old style', 20), fg='red', bg='yellow',bd=1).place(x=280, y=360)
        #------------Sql Connection------------#
    def Empty(self):
        if self.id.get()=="" or self.name.get=="" or self.course.get()=="" or self.password.get()=="":
            messagebox.showerror("Errror","All Fileds Are Requied",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="python")
                cur=con.cursor()
                cur.execute("select * from student where id=%s ",self.id.get())
                row=cur.fetchone()
                print(row)
                if row !=None:
                    messagebox.showerror("Error","Student Are Already Exist plese enter new ID",parent=self.root)
                    self.clear()
                else:
                    cur.execute("insert into student(id,stud_name,course,password) values(%s,%s,%s,%s)",
                    (
                        self.id.get(),self.name.get(),self.course.get(),self.password.get()
                    ))
                    con.commit()
                    messagebox.showinfo("success", "Register Successfully", parent=self.root)
                    con.close()
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    def clear(self):
        self.id.delete(0,END)
        self.name.delete(0,END)
        self.course.delete(0,END)
        self.password.delete(0,END)
    def Reset(self):
        exit(0)
root = Tk()
obj = Register_Data(root)
root.mainloop()
