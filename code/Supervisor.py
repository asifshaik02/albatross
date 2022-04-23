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
from Database import Database

# from tkinter.messagebox import shorootfo
hostname='localhost'
database='postgres'
username='postgres'
pwd='1234'
port_id="5432"
conn=None
curr=None
try:
    conn=psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)
    
    curr=conn.cursor()
    


except Exception as error:
    print(error)



# from Employee import Employee

class Supervisor:

    def __init__(self):
        pass
    def requestMedicines(self,ownerid,medicineid,quantity):
        
        pass

    def assignwork(self,eid,worktype ):

        pass

    def assignWorkHrs(self, e_id,no_of_hrs):
        print(e_id,no_of_hrs)
        curr.execute(f"UPDATE employee SET workinghours = '{no_of_hrs}' WHERE e_id = '{e_id}';")
        pass
    def gui(self):
        root=Tk()
        date=dt.datetime.now()
        format_date=f"{date:%a, %b %d %Y}"
        root.title("Supervisor --- "+format_date)
        root.geometry("900x650")
        frame1=LabelFrame(root,text="Enter details",width=900,height=650,bg="blue",pady=0,padx=0)
        childframe1 = Frame(frame1,width=400,height=100,bg="green")
        childframe2 = Frame(frame1,width=400,height=400)
        childframe3 =  Frame(frame1,width=400,height=400)
        childframe4 =  Frame(frame1,width=400,height=400)
        childframe1.place(x=10,y=2,height=100,width=400)
        childframe2.place(x=10,y=150,height=400,width=400)
        childframe3.place(x=10,y=150,height=400,width=400)
        childframe4.place(x=10,y=150,height=400,width=400)
        frame1.pack(fill="both",expand=1)
        def clos():
            childframe2.place(width=0,height=0)
            childframe3.place(width=0,height=0)
            childframe4.place(width=0,height=0)
        clos()
        e_id_store=StringVar()
        e_working=StringVar()
        owner_id = StringVar()
        medicineid=StringVar()
        medicinequantity=StringVar()
        e_workhrs=IntVar()
        def opendchldfrm2():
            clos()
            childframe2.place(x=10,y=150,height=400,width=400)
        def AssignWorkCheck():
            clos()
            x=e_id_store.get()
            y=e_working.get()
            q = curr.execute(f"select * from employee where e_id='{x}'")
            q=curr.fetchall()
            z=[]
            for i in q:
                print(i)
                z=i
            if 1:
                popup()
                return
            self.assignwork(x,y)
            opendchldfrm2()
        def openchldfrm3():
            clos()
            childframe3.place(x=10,y=150,height=400,width=400)
        def openchldfrm4():
            clos()
            childframe4.place(x=10,y=150,height=400,width=400)
        def RequestMedicineCheck():
            clos()
            x=owner_id.get()
            y=medicineid.get()
            z=medicinequantity.get()
            q = curr.execute(f"select * from employee where e_id='{x}'")
            q=curr.fetchall()
            z=[]
            for i in q:
                print(i)
                z=i
            if 1:
                popup()
                return
            self.requestMedicines(x,y,z)
            openchldfrm3()
        def Assignworkhrscheck():
            clos()
            x=e_id_store.get()
            y=e_workhrs.get()
            print(x)
            q = curr.execute(f"select * from employee where e_id='{x}'")
            q=curr.fetchall()
            
            for i in q:
                print(i)
                z=i
            if z==[]:
                popup()
                return
            self.assignWorkHrs(x,y)
            openchldfrm4()
            pass
        submitchildfram1 = Button(childframe1,text='Assign Work',command=opendchldfrm2)
        submitchildfram1.grid(row=0,column=0)
        submitchildfram2 = Button(childframe1,text='Request Medicine',command=openchldfrm3)
        submitchildfram2.grid(row=1,column=1)
        submitchildfram3 = Button(childframe1,text='Assign Work Hours',command=openchldfrm4)
        submitchildfram3.grid(row=2,column=2)
        
        e_label = Label(childframe2,text="Enter Employee ID",font=('times new romman',15,'bold','italic','underline'),fg='green')
        e_entry = Entry(childframe2,textvariable=e_id_store,relief=SUNKEN,bd=7)
        e_labelworkhrs=Label(childframe2,text="Enter type of work ",font=('times new romman',15,'bold','italic','underline'),fg='green')
        e_entryworkhrs = Entry(childframe2,textvariable=e_working,relief=SUNKEN,bd=7)
        submitchildfram2 = Button(childframe2,text='Submit',command=AssignWorkCheck)
        e_label.grid(row=0,column=0)
        e_entry.grid(row=0,column=1)
        e_labelworkhrs.grid(row=1,column=0)
        e_entryworkhrs.grid(row=1,column=1)
        submitchildfram2.grid(row=2,column=1)

        o_label = Label(childframe3,text="Enter Owner ID",font=('times new romman',15,'bold','italic','underline'),fg='green')
        o_entry = Entry(childframe3,textvariable=owner_id,relief=SUNKEN,bd=7)
        m_id=Label(childframe3,text="Enter Medicine ID ",font=('times new romman',15,'bold','italic','underline'),fg='green')
        m_entry = Entry(childframe3,textvariable=medicineid,relief=SUNKEN,bd=7)
        m_q=Label(childframe3,text="Enter Medicine Quantity ",font=('times new romman',15,'bold','italic','underline'),fg='green')
        mq_entry = Entry(childframe3,textvariable=medicinequantity,relief=SUNKEN,bd=7)
        submitchildfram3 = Button(childframe3,text='Submit',command=RequestMedicineCheck)
        o_label.grid(row=0,column=0)
        o_entry.grid(row=0,column=1)
        m_id.grid(row=1,column=0)
        m_entry.grid(row=1,column=1)
        m_q.grid(row=2,column=0)
        mq_entry.grid(row=2,column=1)
        submitchildfram3.grid(row=3,column=1)

        eid_label = Label(childframe4,text="Enter Owner ID",font=('times new romman',15,'bold','italic','underline'),fg='green')
        eid_entry = Entry(childframe4,textvariable=e_id_store,relief=SUNKEN,bd=7)
        ew_id=Label(childframe4,text="Enter Working hours ",font=('times new romman',15,'bold','italic','underline'),fg='green')
        ew_entry = Entry(childframe4,textvariable=e_workhrs,relief=SUNKEN,bd=7)
        submitchildfram4 = Button(childframe4,text='Submit',command=Assignworkhrscheck)
        eid_label.grid(row=0,column=0)
        eid_entry.grid(row=0,column=1)
        ew_id.grid(row=1,column=0)
        ew_entry.grid(row=1,column=1)
        submitchildfram4.grid(row=2,column=1)
        def popup():
            # showinfo showwarning showerror askquestion askokcancel askyesno (different messagebox here not completed)
            messagebox.showwarning("Enter valid Employee ID")
        
        # submitFram1 = Button(childframe1,text='Submit',command=frame1submit)
        root.mainloop()
        curr.close()
        conn.close()
Supervisor().gui()
