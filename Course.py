from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql
class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg='white')
        self.root.focus_force()
        #----------All the Vairble----------------#
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charge=StringVar()
#----------Title-----------------------------------#
        title=Label(self.root,text="Manage Course Details",font=('Guddy old sytle',20,'bold'),bg='#033054',fg='white').place(x=0,y=0,relwidth=1,height=50)
#---------Widgts---------------------------#
        lbl_courseName=Label(self.root,text="Course Name",font=('Guddy old style',15,'bold'),bg='white').place(x=10,y=60)
        lbl_duration=Label(self.root,text="Duration",font=('Guddy old style',15,'bold'),bg='white').place(x=10,y=100)
        lbl_charges=Label(self.root,text="Charges",font=('Guddy old style',15,'bold'),bg='white').place(x=10,y=140)
        lbl_description=Label(self.root,text="Description",font=('Guddy old style',15,'bold'),bg='white').place(x=10,y=180)
        #-------Entry field--------------------------------------------#
        self.txt_courseName=Entry(self.root,textvariable=self.var_course,font=('Guddy old style',15,'bold'),bg='lightyellow')
        self.txt_courseName.place(x=150,y=60,width=200)
        self.txt_duration=Entry(self.root,textvariable=self.var_duration,font=('Guddy old style',15,'bold'),bg='lightyellow')
        self.txt_duration.place(x=150,y=100,width=200)
        self.txt_charges=Entry(self.root,textvariable=self.var_charge,font=('Guddy old style',15,'bold'),bg='lightyellow')
        self.txt_charges.place(x=150,y=140,width=200)
        self.txt_description=Text(self.root,font=('Guddy old style',15,'bold'),bg='lightyellow')
        self.txt_description.place(x=150,y=180,width=500,height=100)
    #-------------Button------------------#
        self.btn_add=Button(self.root,text="Save",font=('Guddy old style',15,'bold'),bg='#2196f3',fg='white',cursor='hand2',command=self.Add_course)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",font=('Guddy old style',15,'bold'),bg='#4caf50',fg='white',cursor='hand2',command=self.updte_data)
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=('Guddy old style',15,'bold'),bg='#f44336',fg='white',cursor='hand2',command=self.Delete_data)
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=('Guddy old style',15,'bold'),bg='grey',fg='white',cursor='hand2',command=self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40)
    #-----------Search Panel----------------------------------------#
        self.var_search=StringVar()
        lbl_search_courseName=Label(self.root,text="Course Name",font=('Guddy old style',15,'bold'),bg='white').place(x=720,y=60)
        txt_search_courseName=Entry(self.root,font=('Guddy old style',15,'bold'),textvariable=self.var_search,bg='lightyellow').place(x=860,y=60,width=180)
        btn_search=Button(self.root,text="Search",font=('Guddy old style',15,'bold'),bg='#2196f3',fg='white',cursor='hand2',command=self.search)
        btn_search.place(x=1050,y=60,width=110)
        #----------------Content----------------#
        self.c_frame=Frame(self.root,bd=2,relief=RIDGE)
        self.c_frame.place(x=720,y=100,width=470,height=340)
        scrolly=Scrollbar(self.c_frame,orient=VERTICAL)
        scrollx=Scrollbar(self.c_frame,orient=HORIZONTAL)
        self.courseTable=ttk.Treeview(self.c_frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.courseTable.xview)
        scrolly.config(command=self.courseTable.yview)
        self.courseTable.heading("cid",text="Course_ID")
        self.courseTable.heading("duration",text="Duration")
        self.courseTable.heading("name",text="Name")
        self.courseTable.heading("charges",text="Charges")
        self.courseTable.heading("description",text="Description")
        self.courseTable["show"]='headings'
        self.courseTable.column("cid",width=100)
        self.courseTable.column("name",width=100)
        self.courseTable.column("duration",width=100)
        self.courseTable.column("charges",width=100)
        self.courseTable.column("description",width=200)
        self.courseTable.pack(fill=BOTH,expand=1)
        self.courseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show_Details()
        #-----------function-------#
    def Delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="lms")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Wraning","course should be required",parent=self.root)
            else:
                cur.execute("select * from addcourse where name=%s",self.var_course.get())
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("warning","plese select course from list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete the record",parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM  addcourse where name=%s",self.var_course.get())
                        con.commit()
                        messagebox.showinfo("Success","Record Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    def clear(self):
        self.show_Details()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charge.set("")
        self.txt_description.delete('1.0',END)
        self.txt_courseName.config(state=NORMAL)
    def updte_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="lms")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Wraning","Course name Not not be Empty")
            else:
                cur.execute("select * from addcourse where name=%s",self.var_course.get())
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("warning","select course from list",parent=self.root)
                else:
                    cur.execute("update addcourse set duration=%s,charges=%s,description=%s where name=%s",(
                        self.var_duration.get(),
                        self.var_charge.get(),
                        self.txt_description.get("1.0",END),
                        self.var_course.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course update Successfully",parent=self.root)
                    self.Clear_field()
                    self.show_Details()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
        
    def get_data(self,ev):
        self.txt_courseName.config(state='readonly')
        self.txt_courseName
        r=self.courseTable.focus()
        content=self.courseTable.item(r)
        row=content["values"]
    #    print(row)
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charge.set(row[3])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])
    def Clear_field(self):
        self.txt_courseName.delete(0,END)
        self.txt_duration.delete(0,END)
        self.txt_charges.delete(0,END)
        self.txt_description.delete('1.0',END)
    def Add_course(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="lms")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Wraning","Course name Not not be Empty")
            else:
                cur.execute("select * from addcourse where name=%s",self.var_course.get())
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("warning","Course Name Already Exists",parent=self.root)
                else:
                    cur.execute("insert into addcourse(name,duration,charges,description) values(%s,%s,%s,%s)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charge.get(),
                        self.txt_description.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course Added Successfully",parent=self.root)
                    self.Clear_field()
                    self.show_Details()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    def show_Details(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="lms")
        cur=con.cursor()
        try:
            cur.execute("select * from addcourse")
            rows=cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert('',END,values=row)
        except Exception as es:
             messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    def search(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="lms")
        cur=con.cursor()
        try:
            cur.execute(f"select * from addcourse where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert('',END,values=row)
        except Exception as es:
             messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)   
if __name__=="__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()