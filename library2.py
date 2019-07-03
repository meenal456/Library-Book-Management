from tkinter import *
import pymysql
import pymysql.cursors
from tkinter import messagebox

win=Tk()
win.geometry("1350x750")
win.title("Library Management")
win.configure(bg="orange")
topframe=Frame(win,bg="yellow",width=1500,height=200,relief='raise',bd=10)
topframe.pack(side=TOP)
lb=Label(topframe,text="Book Library Management",font=('italic',40,'bold'),width=41,fg='black')
lb.grid(row=0,column=1)

Mframe=Frame(win,bg="yellow",width=1000,height=800,relief='raise',bd=10)
Mframe.pack(padx=50,pady=20)
lb=Label(Mframe,text="Registration",font=('italic',40,'bold'),width=41,fg='black')
lb.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

lb2=Label(Mframe,text="Student_Name",width=15)
lb2.grid(row=1,column=0,padx=10,pady=10)
sname=StringVar()
tb2=Entry(Mframe,textvariable=sname)
tb2.grid(row=1,column=1)

lb3=Label(Mframe,text="Password",width=15)
lb3.grid(row=2,column=0,padx=10,pady=10)
Password=StringVar()
tb3=Entry(Mframe,textvariable=Password)
tb3.grid(row=2,column=1)


lb4=Label(Mframe,text="Email_id",width=15)
lb4.grid(row=3,column=0,padx=10,pady=10)
email_id=StringVar()
tb4=Entry(Mframe,textvariable=email_id)
tb4.grid(row=3,column=1)

lb4=Label(Mframe,text="Contact_no",width=15)
lb4.grid(row=4,column=0,padx=10,pady=10)
contact=StringVar()
tb4=Entry(Mframe,textvariable=contact)
tb4.grid(row=4,column=1)

btn1=Button(Mframe,text="Submit",font=('italic',15,'bold'),bd=5,width=15,fg='black',relief='raise',activebackground="orange")
btn1.grid(row=5,column=0,columnspan=2,padx=10,pady=10)
win.mainloop()
