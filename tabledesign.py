from tkinter import *
import tkinter as tk
from tkinter import ttk
import pymysql
def Show():
    r=tk.Tk()
    r.title('Student details')
    r.geometry('500x350')
    r.config(bg='crimson')
    con=pymysql.connect(host='localhost',user='root',password='',database='lms')
    cur=con.cursor()
    cur.execute('select * from librarian')
    tree=ttk.Treeview(r)
    tree['show']='headings'
    style=ttk.Style(r)
    style.theme_use('classic')
    style.configure(".",font=('Guddy old style',18))
    style.configure("Treeview.Heading",fg="red",font=('Guddy old style',18))    
    tree['columns']=("id",'name','email','pass')
    #--------Tree Width-------#
    tree.column('id',width=150,minwidth=50,anchor=tk.CENTER)
    tree.column('name',width=150,minwidth=50,anchor=tk.CENTER)
    tree.column('email',width=150,minwidth=50,anchor=tk.CENTER)
    tree.column('pass',width=150,minwidth=50,anchor=tk.CENTER)
    #------Assign heading------------#
    tree.heading('id',text='ID',anchor=tk.CENTER)
    tree.heading('name',text='NAME',anchor=tk.CENTER)
    tree.heading('email',text='EMAIL',anchor=tk.CENTER)
    tree.heading('pass',text='PASSWORD',anchor=tk.CENTER)
    
    i=0
    for ro in cur:
        tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3]))
        i = i+ 1
    hsb=ttk.Scrollbar(r,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(r,orient=VERTICAL)
    hsb.configure(command=tree.xview)
    scroll_y.configure(command=tree.yview)
    tree.configure(xscrollcommand=hsb.set)
    tree.configure(yscrollcommand=scroll_y.set)
    scroll_y.pack(side=RIGHT,fill=Y)
    hsb.pack(side=BOTTOM,fill=X)
    tree.pack()
    r.mainloop()
Show()
    