from ast import Global
from cProfile import label
from datetime import date
from doctest import master
from pkgutil import extend_path
from threading import local
# from distutils.command.config import config
from tkinter import *
from tkinter import messagebox
from functools import partial
from turtle import bgcolor
import psycopg2
from tkinter import ttk
import tkinter as tk
import datetime as dt
from PIL import ImageTk, Image
from setuptools import Command
from Medicine import forOwner


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
        q = curr.execute(f"select * from employee where e_id='{e_id}'")
        q=curr.fetchall()
        x=[]
        for i in q:
            x=i
        return x
        

        pass

    def getMedicineDetails(self):
        pass
        

    def getBillTransactions(self, biil_id):
        pass
    def gui(self):
        root=Tk()
        date=dt.datetime.now()
        format_date=f"{date:%a, %b %d %Y}"
        root.title("Owner --- "+format_date)
        root.geometry("900x650")
        # cur=Owner()

        my_notebook = ttk.Notebook(root)
        my_notebook.pack()

        frame1=LabelFrame(my_notebook,text="Enter details",width=900,height=650,bg="blue",pady=0,padx=0)
        frame2=LabelFrame(my_notebook,text="Enter details",width=900,height=650,bg="blue",pady=0,padx=0)
        frame3=LabelFrame(my_notebook,text="Medicine Details",width=900,height=650,bg="blue",pady=0,padx=0)
        # frame3=Frame(my_notebook,width=500,height=500,bg="green")
        # frame2button = Button(my_notebook,text="getMidicine Details",command= forOwner)
        childframe1 = Frame(frame1,width=400,height=100,bg="green")
        childframe2 = Frame(frame1,width=400,height=400)
        childframe1.place(x=10,y=2,height=100,width=400)
        childframe2.place(x=10,y=150,height=0,width=0)
        # frame.pack(fill="both",expand=1)
        frame1.pack(fill="both",expand=1)
        frame2.pack(fill="both",expand=1)
        # frame3.pack(fill="both",expand=1)

        my_notebook.add(frame1,text="getEmployeeDetails")
        my_notebook.add(frame2,text="Medicine Details/Billtranscation")
        buttonasif = Button(frame2,text="getMidicine Details",command= forOwner)
        buttonanil = Button(frame2,text="getBillTransaction",command= forOwner)
        buttonasif.grid(row=0,column=0,padx=5,pady=10)
        buttonanil.grid(row=0,column=1)
        # my_notebook.add(frame2button,text="getMidicine Details")
        # my_notebook.add(frame3,text="getBillTransactions")


        # buttons for frame1

        childframe2cur=0

        e_id_store=StringVar()

        def Employedetails(e_id):
            x=self.getEmployeeDetails(e_id)
            labele_nameq.config(text = x[0])
            labele_phoneq.config(text = x[2])
            labele_roleq.config(text = x[3])
            labelo_idq.config(text = x[5])

        def popup():
            messagebox.showwarning("Enter valid Employee ID")

        def frame1submit():
            forchildhide()
            e_id=e_id_store.get()
            q = curr.execute(f"select * from employee where e_id='{e_id}'")
            q=curr.fetchall()
            val=1
            for i in q:val=0
            y =Label(childframe2,text=q)
            y.place()
            if (val):
                popup()
                return
            forchildvisible()
            Employedetails(e_id)
        def forchildhide():
            #childframe1.destroy()
            childframe2.place(height=0,width=0)
            pass
        def forchildvisible():
            childframe2.place(height=300,width=400)
        e_label = Label(childframe1,text="Enter Employee ID",font=('times new romman',15,'bold','italic','underline'),fg='green')
        e_entry = Entry(childframe1,textvariable=e_id_store,relief=SUNKEN,bd=7)

        submitFram1 = Button(childframe1,text='Submit',command=frame1submit)
        e_label.grid(row=0,column=0)
        e_entry.grid(row=0,column=1,padx=10)
        submitFram1.grid(row=1,column=0,padx=20,pady=30)
        x=Button(childframe2,text=" Hide Information ",command=forchildhide)
        x.grid(row=0,column=0)

        labele_name=Label(childframe2,text="Name of the employee is          :  ")
        labele_nameq=Label(childframe2)
        labele_phone=Label(childframe2,text="Phone number of the employee is : ")
        labele_phoneq=Label(childframe2)
        labele_role=Label(childframe2,text="Role of the employee is          : ")
        labele_roleq=Label(childframe2)
        labelo_id=Label(childframe2,text="Owner ID of the employee is        : ")
        labelo_idq=Label(childframe2)

        # <<<<<<< HEAD
        labele_name.grid(row=1,column=0)
        labele_nameq.grid(row=1,column=1)
        labele_phone.grid(row=2,column=0)
        labele_phoneq.grid(row=2,column=1)
        labele_role.grid(row=3,column=0)
        labele_roleq.grid(row=3,column=1)
        labelo_id.grid(row=4,column=0)
        labelo_idq.grid(row=4,column=1)
#
# obj=Owner()
# obj.gui()
root.mainloop()
curr.close()
conn.close()
# =======
       #  root.mainloop()
# obj = Owner()
# >>>>>>> b7b2b9e1ca58c3505fab41d9d8a1c8000e19ec3f
