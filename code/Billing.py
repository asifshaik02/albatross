from datetime import date
from distutils.command.config import config
from tkinter import *
from tkinter import messagebox
from functools import partial
import psycopg2
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
#from click import command

hostname='localhost'
database='firstdatabase'
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
            password=pwd,
            port=port_id)
    
    curr=conn.cursor()
    


except Exception as error:
    print(error)




root=Tk()
root.title("Medical Store Billing")
root.geometry("600x480")

title=Label(root,text='Medicines Billing System',bg='#2D9290',fg='White',font=('times new romman',40,'bold','italic'),relief=GROOVE,bd=10)
title.pack(fill=X)

# mid = StringVar()
# mquan = IntVar()
# total_cost=StringVar()
# bdate=StringVar()
# icost=IntVar()
# mname=StringVar()
# b_id=StringVar()


class Billing:
    def __init__(self):
        # self.b_id = bid
        # self.billDate = b_date
        # self.b_cost = cost
        # self.quantity = quantity
        # self.medicineName = m_name
        self.sum=0

    def getBillTransactions(self,m_name,quantity,f2):
        n=m_name.get()
        c=int(quantity.get())
        columns=('m_name','m_cost','c')
        viewtree=ttk.Treeview(f2,columns=columns,show='headings',height=10)
        viewtree.heading('m_name',text="Medicine Name")
        viewtree.heading('m_cost',text='Medicine Cost')
        viewtree.heading('c',text='Medicine Quantity')


        viewtree.column('m_name',width=200,anchor=CENTER)
        viewtree.column('m_cost',width=200,anchor=CENTER)
        viewtree.column('c',width=180,anchor=CENTER)

        
        r=curr.execute(f"select m_name,m_cost from medicine where m_name='{n}'")
        r=curr.fetchall()
        for i in r:
            viewtree.insert(parent='',index='end',text='',values=(n,i[1],c))
        style=ttk.Style()
        style.theme_use("default")
        style.map("viewtree")
        viewtree.grid(row=0,column=0,sticky='nsew')

        scrollbar=ttk.Scrollbar(f2,orient=tk.VERTICAL,command=viewtree.yview)
        viewtree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0,column=1,sticky='ns')
    
        
        
        
        
    def totalcost(self,m_name,quantity,f3):
        n = m_name.get()
        c = int(quantity.get())
        curr.execute(f"select m_cost from medicine where m_name='{n}'")
        # for i in curr:
        #     print(i)
        self.sum+=(list(curr)[0][0])*c
        print(self.sum)
        res=Label(f2,text=self.sum,font=('times new romman',20),fg='black')
        res.grid(row=10,column=0,padx=20,pady=15)
    
        
        
        

        

obj=Billing()
# --------Medicines details----#
f1=LabelFrame(root,text="Medicine Details",font=('times new romman',20,'bold','italic'),fg='gold')
f1.place(x=5,y=90,height=500,width=600)

med=Label(f1,text="Medicine Name",font=('times new romman',15,'bold','italic','underline'),fg='black')
med.grid(row=0,column=0,padx=20,pady=15)

quan=Label(f1,text="Medicine Quantity",font=('times new romman',15,'bold','italic'),fg='black')
quan.grid(row=4,column=0,padx=20,pady=15)

#------Details----#
m_name = StringVar()
m_quan=IntVar()
mnameEntry = Entry(f1, textvariable=m_name,relief=SUNKEN,bd=7).grid(row=0, column=3)
mquanEntry = Entry(f1, textvariable=m_quan,relief=SUNKEN,bd=7).grid(row=4, column=3)



#-----Bill -----#
f2=LabelFrame(root,text="Bill",font=('times new romman',20,'bold','italic'),fg='gold')
f2.place(x=700,y=90,height=500,width=600)

# item1=Label(f2,text='Medicine Name',font=('times new romman',15,'bold','italic','underline'),fg='black')
# item1.grid(row=0,column=0,padx=20,pady=15)

# item2=Label(f2,text='Medicine Cost',font=('times new romman',15,'bold','italic','underline'),fg='black')
# item2.grid(row=0,column=1,padx=20,pady=15)

# item3=Label(f2,text='Medicine Quantity',font=('times new romman',15,'bold','italic','underline'),fg='black')
# item3.grid(row=0,column=2,padx=20,pady=15)


#-------Buttons----#
f3=Frame(root,relief=GROOVE,bd=10,bg='white')
f3.place(x=5,y=590,width=600,height=120)


bill=partial(obj.getBillTransactions,m_name,m_quan,f2)
cost=partial(obj.totalcost,m_name,m_quan,f2)
enter=Button(f1,text="Enter",command=bill,font=('times new romman',15,'bold'))
enter.grid(row=8,column=3)
button_2=Button(f3,text="Generate Bill",command=cost,font=('times new romman',15,'bold'),bg='gold')
button_2.grid(row=0,column=4)


root.mainloop()
curr.close()
conn.close()












