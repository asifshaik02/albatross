from datetime import date
# from distutils.command.config import config
from tkinter import *
from tkinter import messagebox
from functools import partial
from turtle import bgcolor
import psycopg2
from tkinter import ttk
import tkinter as tk
import datetime as dt

from setuptools import Command

from Medicine import Medicine
# from tkinter.messagebox import shorootfo
hostname='localhost'
database='postgres'
username='postgres'
pwd='pgadmin'
port_id=5432
conn=None
curr=None
try:
    conn=psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password='1234',
            port=port_id)
    
    curr=conn.cursor()
    


except Exception as error:
    print(error)




root=Tk()
date=dt.datetime.now()
format_date=f"{date:%a, %b %d %Y}"
root.title("Owner --- "+format_date)
root.geometry("700x350")



class Owner:
    def __init__(self,name="",id="",phone_no="",role="",password="",o_id=""):
        self.e_name = name
        self.e_id = id
        self.e_phone = phone_no
        self.e_role = role
        self.e_password = password
        self.o_id = o_id
    def login(self, e_name, password):
        # don't know
        pass

    def getEmployeeDetails(self, e_id):
        r=curr.execute(f"select * from medicine where e_id='{e_id}'")
        pass

    def getMedicineDetails(self):
        obj = Medicine()
        pass

    def getBillTransactions(self, biil_id):
        pass

cur=Owner()

my_notebook = ttk.Notebook(root)
my_notebook.pack()

frame1=LabelFrame(my_notebook,text="Enter details",width=500,height=500,bg="blue",padx=75,pady=30)
frame2=Frame(my_notebook,width=500,height=500,bg="red")
frame3=Frame(my_notebook,width=500,height=500,bg="green")
frame4=Frame(my_notebook,width=500,height=500,bg="pink")
frame2button = Button(my_notebook,text="getMidicine Details",command= cur.getMedicineDetails)
childframe1 = Frame(frame1,width=500,height=100,bg="green")
childframe1.pack(fill="both",expand=1)
frame1.pack(fill="both",expand=1)

frame3.pack(fill="both",expand=1)
frame4.pack(fill="both",expand=1)

my_notebook.add(frame1,text="getEmployeeDetails")
my_notebook.add(frame2button,text="getMidicine Details")
my_notebook.add(frame3,text="getBillTransactions")
my_notebook.add(frame4,text="Calculator")


# buttons for frame1

e_id_store=StringVar()

def popup():
    # showinfo showwarning showerror askquestion askokcancel askyesno
    messagebox.showinfo("this is msg")

def frame1submit():
    e_id=e_id_store.get()
    q = f"select * from employee where m_id='{e_id}';"
    if (q):
        popup()
        return
    
    pass
e_label = Label(childframe1,text="Enter Employee ID",font=('times new romman',15,'bold','italic','underline'),fg='green')
e_entry = Entry(childframe1,textvariable=e_id_store,relief=SUNKEN,bd=7)

submitFram1 = Button(childframe1,text='Submit',command=frame1submit)
e_label.grid(row=0,column=0)
e_entry.grid(row=0,column=1,padx=10)
submitFram1.grid(row=1,column=0,padx=20,pady=30)



#
root.mainloop()
curr.close()
conn.close()
