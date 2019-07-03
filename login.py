from tkinter import *
import pymysql
import pymysql.cursors
from tkinter import messagebox
import os

'''def abc():
    win.destroy()
    os.system'''
def login():
    us=username.get()
    pa=Password.get()

    conn=pymysql.connect(host='localhost',user='root',password='',db='lib')
    a=conn.cursor()

    a.execute("select * from reg where username='"+us+"'and password='"+pa+"'")
    results=a.fetchall()
    count=a.rowcount
    print(results)
    print(count)
    if(count>0):
      
       #os.system('border.py')
       os.system('library2.py')
       '''wel=Tk()
       wel.configure(bg="cyan")
       wel.geometry("400x400")
       lb1=Label(wel,text="Welcome",font=("gigi",20,"bold"),width=20,bd=10,relief="raised")
       lb1.grid(row=0,padx=40,pady=40)
       messagebox.showinfo("message","login")'''
    else:
        messagebox.showinfo("Message","not login")


win=Tk()
win.geometry("1350x750")
win.title("Library Management")
win.configure(bg="orange")
#win.overrideredirect(True)
#win.overrideredirect(True)
topframe=Frame(win,bg="yellow",width=1500,height=200,relief='raise',bd=10)
topframe.pack(side=TOP)
lb=Label(topframe,text="Book Library Management",font=('italic',40,'bold'),width=41,fg='black')
lb.grid(row=0,column=1)

Mframe=Frame(win,bg="yellow",width=1000,height=800,relief='raise',bd=10)
Mframe.pack(padx=50,pady=20)
lb=Label(Mframe,text="Login Form",font=('italic',40,'bold'),width=41,fg='black')
lb.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

lb2=Label(Mframe,text="Username",width=15)
lb2.grid(row=1,column=0,padx=10,pady=10)
username=StringVar()
tb2=Entry(Mframe,textvariable=username)
tb2.grid(row=1,column=1)

lb3=Label(Mframe,text="Password",width=15)
lb3.grid(row=2,column=0,padx=10,pady=10)
Password=StringVar()
tb3=Entry(Mframe,textvariable=Password)
tb3.grid(row=2,column=1)


btn1=Button(Mframe,text="Login",font=('italic',15,'bold'),bd=5,width=12,fg='black',relief='raise',activebackground="orange",command=login)
btn1.grid(row=3,column=0,columnspan=2,padx=10,pady=10)
