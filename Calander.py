from tkinter import *
from tkcalendar import *
from PIL import ImageTk,Image
from tkinter import messagebox
root=Tk()
root.title('Date Picker')
root.geometry("800x400")
root.config(bg='crimson')
bg_img=Image.open("Photo/calander.jpg")
bg_img=bg_img.resize((50,50),Image.ANTIALIAS)
bg_img=ImageTk.PhotoImage(bg_img)
lbl_bg=Label(root ,image=bg_img).place(x=310,y=40)
lbl_date=Label(root,text='Choose Date',font=('times new roman',24,'bold'),fg='#6495ED',bg='white').place(x=30,y=40)
e=DateEntry(root,font=('Guddy old style',20,'bold'),fg='green',bg='white',image=lbl_bg)
e.place(x=210,y=40)
root.mainloop()