from tkinter import *
from tkinter import messagebox
import smtplib
import random
root = Tk()
root.title('Gmail verifaction')
root.geometry('599x348+100+58')
root.config(bg='#FF5733')
lbl_email=Label(root,text='Enter your Email id:',font=('Guddy old style',15),fg='white',bg='crimson').place(x=20,y=40)
email=Entry(root,font=('Guddy old style',15))
email.place(x=220,y=40,width=270)

def send_mail():

    try:
        s = smtplib.SMTP("smtp.gmail.com" , 587)  # 587 is a port number 
        s.starttls()
        s.login("imranim4205102@gmail.com" , "kudvywzshnfobmbv")
        otp = random.randint(1000, 9999)
        otp = str(otp)
        subject="Sending Email verifaction using python"
        body="Your verifacation code is  "+otp
        msg="Subject:{}\n\n{}".format(subject,body)
        s.sendmail("imranim4205102@gmail.com" , email.get() ,msg)
        messagebox.showinfo("Send OTP via Email", f"OTP sent to {email.get()}")
        s.quit()
    except Exception as es:
        messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)
def Check_OTP():
    global otp
    if verify==(otp):
        messagebox.showerror("Error",f"Error due to: {str(Verify.get())}",parent=root)
    else:
        messagebox.showinfo("Success","Email Login Successfully",parent=root)
sbt=Button(root,text='Send Mail',command=send_mail,font=('times new roman',22),fg='white',bg='#6162ff',cursor='hand2').place(x=180,y=100)
lbl_verifyl=Label(root,text='Enter OTP',font=('times new roman',19),fg='white',bg='grey').place(x=50,y=180)
verify=Entry(root,font=('times new roman',19)).place(x=180,y=180)
sbt1=Button(root,text='Verify OTP',command=Check_OTP,font=('times new roman',22),fg='white',bg='#6162ff',cursor='hand2').place(x=180,y=250)
root.mainloop()