from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
from tkcalendar import *
import pymysql
class StudentClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Manage Student System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg='white')
        self.root.focus_force()
        #----------All the Vairble----------------#
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()
        
#----------Title-----------------------------------#
        title=Label(self.root,text="Manage Student  Details",font=('Guddy old sytle',20,'bold'),bg='#033054',fg='white').place(x=0,y=0,relwidth=1,height=50)
#---------Widgts-1--------------------------#
        lbl_roll=Label(self.root,text="Roll_No",font=('Guddy old style',15,'bold'),bg='white').place(x=10,y=60)
        lbl_name=Label(self.root,text="Name",font=('Guddy old style',15,'bold'),bg='white').place(x=10,y=100)
        lbl_email=Label(self.root,text="Email",font=('Guddy old style',15,'bold'),bg='white').place(x=10,y=140)
        lbl_gender=Label(self.root,text="Gender",font=('Guddy old style',15,'bold'),bg='white').place(x=10,y=180)
        lbl_state=Label(self.root,text="State",font=('Guddy old style',15,'bold'),bg='white').place(x=10,y=220)
        self.txt_state=Entry(self.root,textvariable=self.var_state,font=('Guddy old style',15,'bold'),bg='lightyellow')
        self.txt_state.place(x=150,y=220,width=200)
        lbl_Address=Label(self.root,text="Address",font=('Guddy old style',15,'bold'),bg='white').place(x=10,y=260)
        lbl_city=Label(self.root,text="City",font=('Guddy old style',15,'bold'),bg='white').place(x=320,y=220)
        self.txt_city=Entry(self.root,textvariable=self.var_city,font=('Guddy old style',15,'bold'),bg='lightyellow')
        self.txt_city.place(x=380,y=220,width=150)
        lbl_pim=Label(self.root,text="Pin",font=('Guddy old style',15,'bold'),bg='white').place(x=510,y=220)
        self.txt_pin=Entry(self.root,textvariable=self.var_pin,font=('Guddy old style',15,'bold'),bg='lightyellow')
        self.txt_pin.place(x=550,y=220,width=135)
        
        #-------Entry field- 1-------------------------------------------#
        self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=('Guddy old style',15,'bold'),bg='lightyellow')
        self.txt_roll.place(x=150,y=60,width=200)
        self.txt_name=Entry(self.root,textvariable=self.var_name,font=('Guddy old style',15,'bold'),bg='lightyellow')
        self.txt_name.place(x=150,y=100,width=200)
        self.txt_email=Entry(self.root,textvariable=self.var_email,font=('Guddy old style',15,'bold'),bg='lightyellow')
        self.txt_email.place(x=150,y=140,width=200)
        self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","MALE","FEMALE"),font=('Guddy old style',15,'bold'),state='readonly',justify=CENTER)
        self.txt_gender.place(x=150,y=180,width=200)
        self.txt_gender.current(0)
        #----------TExt Adddress Widget-------------------------#
        self.txt_address=Text(self.root,font=('Guddy old style',15,'bold'),bg='lightyellow')
        self.txt_address.place(x=150,y=260,width=500,height=100)
        #------------------Coulumn-2--------------#
        lbl_dob=Label(self.root,text="D.O.B",font=('Guddy old style',15,'bold'),bg='white').place(x=360,y=60)
        lbl_contact=Label(self.root,text="Contact",font=('Guddy old style',15,'bold'),bg='white').place(x=360,y=100)
        lbl_admission=Label(self.root,text="Admission",font=('Guddy old style',15,'bold'),bg='white').place(x=360,y=140)
        lbl_course=Label(self.root,text="Course",font=('Guddy old style',15,'bold'),bg='white').place(x=360,y=180)
        #----Widghet txt-2-----------------#
        self.cours_list=[]
        #----function call update list-----------------#
        self.fetch_course()        
        self.txt_dob=DateEntry(self.root,textvariable=self.var_dob,font=('Guddy old style',15,'bold'),bg='lightyellow')
        self.txt_dob.place(x=480,y=60,width=200)
        self.txt_contact=Entry(self.root,textvariable=self.var_contact,font=('Guddy old style',15,'bold'),bg='lightyellow')
        self.txt_contact.place(x=480,y=100,width=200)
        self.txt_admission=DateEntry(self.root,textvariable=self.var_a_date,font=('Guddy old style',15,'bold'),bg='lightyellow')
        self.txt_admission.place(x=480,y=140,width=200)
        self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=(self.cours_list),font=('Guddy old style',15,'bold'),state='readonly',justify=CENTER)
        self.txt_course.place(x=480,y=180,width=200)
        self.txt_course.set("Empty")
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
        lbl_search_roll=Label(self.root,text="Roll No",font=('Guddy old style',15,'bold'),bg='white').place(x=720,y=60)
        txt_search_roll=Entry(self.root,font=('Guddy old style',15,'bold'),textvariable=self.var_search,bg='lightyellow').place(x=860,y=60,width=180)
        btn_search=Button(self.root,text="Search",font=('Guddy old style',15,'bold'),bg='#2196f3',fg='white',cursor='hand2',command=self.search)
        btn_search.place(x=1050,y=60,width=110)
        #----------------Content----------------#
        self.c_frame=Frame(self.root,bd=2,relief=RIDGE)
        self.c_frame.place(x=720,y=100,width=470,height=340)
        scrolly=Scrollbar(self.c_frame,orient=VERTICAL)
        scrollx=Scrollbar(self.c_frame,orient=HORIZONTAL)
        self.courseTable=ttk.Treeview(self.c_frame,columns=("roll","name","email","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.courseTable.xview)
        scrolly.config(command=self.courseTable.yview)
        self.courseTable.heading("roll",text="Roll No")
        self.courseTable.heading("name",text="Name")
        self.courseTable.heading("email",text="EMAIL")
        self.courseTable.heading("gender",text="Gender")
        self.courseTable.heading("dob",text="D.O.B")
        self.courseTable.heading("contact",text="Contact")
        self.courseTable.heading("admission",text="Admission")
        self.courseTable.heading("course",text="Course")
        self.courseTable.heading("state",text="STATE")
        self.courseTable.heading("city",text="City")
        self.courseTable.heading("pin",text="PIN")
        self.courseTable.heading("address",text="Address")
        self.courseTable["show"]='headings'
    #---column heding-----------------------
        self.courseTable.column("roll",width=50)
        self.courseTable.column("name",width=100)
        self.courseTable.column("email",width=200)
        self.courseTable.column("gender",width=100)
        self.courseTable.column("dob",width=200)
        self.courseTable.column("contact",width=120)
        self.courseTable.column("admission",width=100)
        self.courseTable.column("course",width=100)
        self.courseTable.column("state",width=100)
        self.courseTable.column("city",width=100)
        self.courseTable.column("pin",width=100)
        self.courseTable.column("address",width=300)
        self.courseTable.pack(fill=BOTH,expand=1)
        self.courseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show_Details()
        #-----------function-------#
    def Delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="lms")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Wraning","Roll  should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=%s",self.var_roll.get())
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("warning","plese select student from list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete the record",parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM  student where roll=%s",self.var_roll.get())
                        con.commit()
                        messagebox.showinfo("Success","Record Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    def clear(self):
        self.show_Details()
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_contact.set(""),
        self.var_a_date.set(""),
        self.var_course.set(""),
        self.var_state.set(""),
        self.var_city.set(""),
        self.var_pin.set(""),
        self.txt_address.delete("1.0",END),
        self.var_roll.set(""),
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")
        
    def updte_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="lms")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Wraning","Roll Number should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=%s",self.var_roll.get())
                row=cur.fetchone()
            #    print(row)
                if row==None:
                    messagebox.showerror("warning","select student  from list",parent=self.root)
                else:
                    cur.execute("update student set name=%s,email=%s,gender=%s,dob=%s,contact=%s,admission=%s,course=%s,state=%s,city=%s,pin=%s,address=%s  where roll=%s",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END),
                        self.var_roll.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student updated Successfully",parent=self.root)
                    self.Clear_field()
                    self.show_Details()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
        
    def get_data(self,ev):
        self.txt_roll.config(state='readonly')
        self.txt_roll
        r=self.courseTable.focus()
        content=self.courseTable.item(r)
        row=content["values"]
    #    print(row)
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_a_date.set(row[6]),
        self.var_course.set(row[7]),
        self.var_state.set(row[8]),
        self.var_city.set(row[9]),
        self.var_pin.set(row[10]),
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[11])
        
    def Clear_field(self):
        self.txt_roll.delete(0,END)
        self.txt_name.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_address.delete('1.0',END)
    def Add_course(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="lms")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Wraning","Roll Number should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=%s",self.var_roll.get())
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("warning","Roll Number Already Exists",parent=self.root)
                else:
                    cur.execute("insert into student(roll,name,email,gender,dob,contact,admission,course,state,city,pin,address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Added Successfully",parent=self.root)
                    self.Clear_field()
                    self.show_Details()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    def show_Details(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="lms")
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            rows=cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert('',END,values=row)
        except Exception as es:
             messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    def fetch_course(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="lms")
        cur=con.cursor()
        try:
            cur.execute("select name from addcourse")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.cours_list.append(row[0])
        except Exception as es:
             messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)         
    def search(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="lms")
        cur=con.cursor()
        try:
            cur.execute("select * from student where roll=%s",(self.var_search.get()))
            rows=cur.fetchone()
            if rows!=None:
                self.courseTable.delete(*self.courseTable.get_children())
                self.courseTable.insert('',END,values=rows)
            else:
                messagebox.showerror("Error","No Record found",parent=self.root)
        except Exception as es:
             messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)   
if __name__=="__main__":
    root=Tk()
    obj=StudentClass(root)
    root.mainloop()