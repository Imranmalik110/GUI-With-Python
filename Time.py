import time
from tkinter import *
root = Tk()
root.title("Digital Clock")
root.config(bg='green')
root.geometry("1200x600")
def Clock():
   h=str(time.strftime("%H"))
   m=str(time.strftime("%M"))
   s=str(time.strftime("%S"))
   if int(h)>12 and int(m)>0:
      lbl_am.config(text='PM')
   if int(h)>12:
      h=str(int(h)-12)
   lbl_hr.config(text=h)
   lbl_min.config(text=m)
   lbl_sec.config(text=s)
   lbl_hr.after(200,Clock)
   
#----------Hours Lable----------#
lbl_hr=Label(root,text=12,font=('times new roman',50,'bold'),bg='#087587',fg='white')
lbl_hr.place(x=250,y=200,width=150,height=150)
lbl_hr2=Label(root,text='HOURS',font=('times new roman',20,'bold'),bg='#087587',fg='white')
lbl_hr2.place(x=250,y=360,width=150,height=50)
#----------Minute Lable----------#
lbl_min=Label(root,text=60,font=('times new roman',50,'bold'),bg='#6495ED',fg='white')
lbl_min.place(x=450,y=200,width=150,height=150)
lbl_min2=Label(root,text='MINUTE',font=('times new roman',20,'bold'),bg='#6495ED',fg='white')
lbl_min2.place(x=450,y=360,width=150,height=50)
#-----------Second Lable-----------#
lbl_sec=Label(root,text=34,font=('times new roman',50,'bold'),bg='#DFFF00',fg='white')
lbl_sec.place(x=650,y=200,width=150,height=150)
lbl_sec2=Label(root,text='SECOND',font=('times new roman',20,'bold'),bg='#DFFF00',fg='white')
lbl_sec2.place(x=650,y=360,width=150,height=50)
#---------PM/AM Lable -------------#
lbl_am=Label(root,text='AM',font=('times new roman',50,'bold'),bg='crimson',fg='white')
lbl_am.place(x=850,y=200,width=150,height=150)
lbl_am2=Label(root,text='NOON',font=('times new roman',20,'bold'),bg='crimson',fg='white')
lbl_am2.place(x=850,y=360,width=150,height=50)
Clock()
root.mainloop()