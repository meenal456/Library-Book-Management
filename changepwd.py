from tkinter import *
import pymysql
import pymysql.cursors
from tkinter import messagebox

def change():
    user=username.get()
    ol=password.get()
    np=nwp.get()
    cn=cnp.get()
    try:
        if(np==cn):
            conn=pymysql.connect(host='localhost',user='root',password='',db="lib")
            a=conn.cursor()
            a.execute("update reg set password='"+np+"' where username='"+user+"' and password='"+ol+"'")
            conn.commit()
            messagebox.showinfo("message", "change")
        else:
                      messagebox.showinfo("message","not match password")

    except:
                      conn.rollback()
                      messagebox.showinfo("message"," not changed")
                      conn.close()
                      
            

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
lb=Label(Mframe,text="Change Password",font=('italic',40,'bold'),width=41,fg='black')
lb.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

lb2=Label(Mframe,text="Username",width=15)
lb2.grid(row=1,column=0,padx=10,pady=10)
username=StringVar()
tb2=Entry(Mframe,textvariable=username)
tb2.grid(row=1,column=1)

lb3=Label(Mframe,text="Old_Password",width=15)
lb3.grid(row=2,column=0,padx=10,pady=10)
password=StringVar()
tb3=Entry(Mframe,textvariable=password)
tb3.grid(row=2,column=1)


lb4=Label(Mframe,text="New_Password",width=15)
lb4.grid(row=3,column=0,padx=10,pady=10)
nwp=StringVar()
tb4=Entry(Mframe,textvariable=nwp)
tb4.grid(row=3,column=1)

lb4=Label(Mframe,text="Confirm_Password",width=15)
lb4.grid(row=4,column=0,padx=10,pady=10)
cnp=StringVar()
tb4=Entry(Mframe,textvariable=cnp)
tb4.grid(row=4,column=1)

btn1=Button(Mframe,text="Change Password",font=('italic',15,'bold'),bd=5,width=15,fg='black',relief='raise',activebackground="orange",command=change)
btn1.grid(row=5,column=0,columnspan=2,padx=10,pady=10)
win.mainloop()
