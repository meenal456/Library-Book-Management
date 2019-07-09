from tkinter import *
import pymysql
import pymysql.cursors
from tkinter import messagebox
import os

def meenal():
    os.system('changepwd.py')
def meenal2():
    os.system('forgetpd.py')

def insert():
    #uid=tb.get()
    un=username.get()
    pd=password.get()
    em=Email_id.get()
    cn=contact_no.get()
    try:
        conn= pymysql.connect(host='localhost',user='root',password='',db='lib')
        a=conn.cursor()
        a.execute("insert into reg values('"+un+"','"+pd+"','"+em+"', '"+cn+"')")
        conn.commit()
        messagebox.showinfo('submitted')
    except:
        conn.rollback()
        messagebox.showinfo('Not submit')
    conn.close()


win=Tk()
win.geometry("1350x750")
win.title("Library Management")
win.configure(bg="orange")

#---top_frame---
topframe=Frame(win,bg="yellow",width=1500,height=200,relief='raise',bd=10)
topframe.pack(side=TOP)
lb=Label(topframe,text="Book Library Management",font=('italic',40,'bold'),width=41,fg='black')
lb.grid(row=0,column=1)

#---middle_frame---

Mframe=Frame(win,bg="yellow",width=1000,height=800,relief='raise',bd=10)
Mframe.pack(padx=50,pady=20)
lb=Label(Mframe,text="Registration",font=('italic',40,'bold'),width=41,fg='black')
lb.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

lb2=Label(Mframe,text="Student_Name",width=15)
lb2.grid(row=1,column=0,padx=10,pady=10)
username=StringVar()
tb2=Entry(Mframe,textvariable=username)
tb2.grid(row=1,column=1)

lb3=Label(Mframe,text="Password",width=15)
lb3.grid(row=2,column=0,padx=10,pady=10)
password=StringVar()
tb3=Entry(Mframe,textvariable=password)
tb3.grid(row=2,column=1)


lb4=Label(Mframe,text="Email_id",width=15)
lb4.grid(row=3,column=0,padx=10,pady=10)
Email_id=StringVar()
tb4=Entry(Mframe,textvariable=Email_id)
tb4.grid(row=3,column=1)

lb4=Label(Mframe,text="Contact_no",width=15)
lb4.grid(row=4,column=0,padx=10,pady=10)
contact_no=StringVar()
tb4=Entry(Mframe,textvariable=contact_no)
tb4.grid(row=4,column=1)

btn1=Button(Mframe,text="Submit",font=('italic',15,'bold'),bd=5,width=15,fg='black',relief='raise',activebackground="orange",command=insert)
btn1.grid(row=5,column=0,columnspan=2,padx=10,pady=10)

btn2=Button(Mframe,text="Change Password",font=('italic',15,'bold'),bd=5,width=15,fg='black',relief='raise',activebackground="orange",command=meenal)
btn2.grid(row=6,column=0,columnspan=2,padx=10,pady=10)

btn3=Button(Mframe,text="Forget Password",font=('italic',15,'bold'),bd=5,width=15,fg='black',relief='raise',activebackground="orange",command=meenal2)
btn3.grid(row=7,column=0,columnspan=2,padx=10,pady=10)


win.mainloop()
