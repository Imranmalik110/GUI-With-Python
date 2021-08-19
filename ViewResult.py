from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
from tkcalendar import *
import pymysql
class ReportClass:
    def __init__(self,root):
        self.root=root
        self.root.title("View Student result")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg='white')
        self.root.focus_force()
    #----------Title-----------------------------------#
        title=Label(self.root,text="View Student Result",font=('Guddy old sytle',20,'bold'),bg='#033054',fg='white').place(x=0,y=0,relwidth=1,height=50)
    #-------------Search label and button--------------------#
        self.var_search=StringVar()
        self.var_id=""
        lbl_search=Label(self.root,text="Search By Roll No.",font=('Guddy old style',20,'bold'),bg='white',).place(x=260,y=100)   
        lbl_search=Entry(self.root,textvariable=self.var_search,font=('Guddy old style',20,'bold'),bg='lightyellow',).place(x=520,y=100,width=150)   
        btn_search=Button(self.root,text="Search",font=('Guddy old style',15,'bold'),activebackground='#2196f3',bg='#2196f3',fg='white',cursor='hand2',command=self.search).place(x=680,y=100,width=110,height=38)
        btn_clear=Button(self.root,text="clear",font=('Guddy old style',15,'bold'),activebackground='grey',bg='grey',fg='white',cursor='hand2',command=self.clear).place(x=800,y=100,width=110,height=38)
    #---------Result Label---------------------------------------#
        lbl_roll=Label(self.root,text="Roll No",font=('Guddy old style',15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50)        
        lbl_name=Label(self.root,text="Name",font=('Guddy old style',15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=300,y=230,width=150,height=50)        
        lbl_course=Label(self.root,text="Course",font=('Guddy old style',15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)        
        lbl_marks=Label(self.root,text="Marks Obtained",font=('Guddy old style',15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=600,y=230,width=150,height=50)        
        lbl_full=Label(self.root,text="Total Marks",font=('Guddy old style',15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=750,y=230,width=150,height=50)  
        lbl_per=Label(self.root,text="Percantage",font=('Guddy old style',15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=900,y=230,width=150,height=50)              
        #------Entry Label------------------------------------#
        self.roll=Label(self.root,font=('Guddy old style',15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.roll.place(x=150,y=280,width=150,height=50)        
        self.name=Label(self.root,font=('Guddy old style',15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.name.place(x=300,y=280,width=150,height=50)        
        self.course=Label(self.root,font=('Guddy old style',15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.course.place(x=450,y=280,width=150,height=50)        
        self.marks=Label(self.root,font=('Guddy old style',15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.marks.place(x=600,y=280,width=150,height=50)        
        self.full=Label(self.root,font=('Guddy old style',15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.full.place(x=750,y=280,width=150,height=50)  
        self.per=Label(self.root,font=('Guddy old style',15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.per.place(x=900,y=280,width=150,height=50)              
    #---------Button Delete------------------------------------#
        btn_delete=Button(self.root,text="Delete",font=('Guddy old style',15,'bold'),activebackground='red',bg='red',fg='white',cursor='hand2',command=self.Delete).place(x=500,y=350,width=150,height=38)
    #----------Funtion---------------------------#
    def search(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="lms")
        cur=con.cursor()
        try:
            cur.execute("select * from result where roll=%s",(self.var_search.get()))
            rows=cur.fetchone()
            if self.var_search.get()=="":
                messagebox.showerror("Warning","search filed should be required",parent=self.root)
            else:
                if rows!=None:
                    self.var_id=rows[0]
                    self.roll.config(text=rows[1])
                    self.name.config(text=rows[2])
                    self.course.config(text=rows[3])
                    self.marks.config(text=rows[4])
                    self.full.config(text=rows[5])
                    self.per.config(text=rows[6])
                else:
                    messagebox.showerror("Error","No Record found",parent=self.root)
        except Exception as es:
             messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    def clear(self):
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.per.config(text="")
        self.var_search.set("")
        self.var_id=""
    def Delete(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="lms")
        cur=con.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Wraning","Search student result first",parent=self.root)
            else:
                cur.execute("select * from result where rid=%s",self.var_id)
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("warning","Invalid Student Result",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete the record",parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM  result where rid=%s",self.var_id)
                        con.commit()
                        messagebox.showinfo("Success","Result deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
        
if __name__=="__main__":
    root=Tk()
    obj=ReportClass(root)
    root.mainloop()