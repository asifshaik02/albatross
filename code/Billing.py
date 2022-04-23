from datetime import date as dt
from tkinter import *
from functools import partial
from tkinter import ttk
import tkinter as tk
from Database import Database

class Billing:
    def __init__(self):
        self.sum=0
        self.res=[]
        self.ans=0

    def getBillTransactions(self,m_name,quantity,f2):
        
        sq=Database()
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

        r=sq.execute(f"select m_cost,m_name from medicine where m_name='{n}'")

        for i in r:
            self.res.append([i[1],i[0],c])
    
        style=ttk.Style()
        style.theme_use("default")
        style.map("viewtree")
        viewtree.grid(row=0,column=0,sticky='nsew')

        scrollbar=ttk.Scrollbar(f2,orient=tk.VERTICAL,command=viewtree.yview)
        viewtree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0,column=1,sticky='ns')
    
    def totalcost(self,m_name,quantity,f3):
        sq=Database()
        n = m_name.get()
        c = int(quantity.get())
        res = sq.execute(f"select m_cost from medicine where m_name='{n}'")
        columns=('m_name','m_cost','c')
        viewtree=ttk.Treeview(f3,columns=columns,show='headings')
        viewtree.heading('m_name',text="Medicine Name")
        viewtree.heading('m_cost',text='Medicine Cost')
        viewtree.heading('c',text='Medicine Quantity')
        viewtree.column('m_name',width=200,anchor=CENTER)
        viewtree.column('m_cost',width=200,anchor=CENTER)
        viewtree.column('c',width=180,anchor=CENTER)
        viewtree.grid(row=0,column=0,sticky='nsew')

        for i in self.res:
            viewtree.insert('','end',values=i)
        scrollbar=ttk.Scrollbar(f3,orient=tk.VERTICAL,command=viewtree.yview)
        viewtree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0,column=1,sticky='ns')

        r = sq.execute(f"select m_cost,m_id from medicine where m_name='{n}'")

        self.ans=r[0][0]
        id=r[0][1]
        b = sq.execute("select b_id from billing")
        if len(b) == 0:
            b = 0
        else:
            b = b[-1][0] + 1
        a=sq.insert(f"insert into billing (b_id,b_date,quantity,m_name,m_cost,b_total,m_id) values ({b},'{str(dt.today())}',{c},'{n}',{self.ans},{self.sum},'{id}') ")

            

    def window(self,m_name,quantity,f3):
        sq=Database()
        n = m_name.get()
        c = int(quantity.get())
        res = sq.execute(f"select m_cost from medicine where m_name='{n}'")
        
        self.sum += res[0][0] * c

        res=Label(f3,text=self.sum,font=('times new romman',15,'bold','italic'))
        res.grid(row=1,column=0,sticky=SE,pady=18)
        tcost=Label(f3,text="Total Cost:",font=('times new romman',20,'bold','italic'),fg='black')
        tcost.grid(row=1,column=0,sticky=S,pady=20)
    
    def gui(self):
        root=Tk()
        root.title("Medical Store Billing")
        root.geometry("600x480")

        title=Label(root,text='Medicines Billing System',bg='#2D9290',fg='White',font=('times new romman',40,'bold','italic'),relief=GROOVE,bd=10)
        title.pack(fill=X)
        f1=LabelFrame(root,text="Medicine Details",font=('times new romman',20,'bold','italic'),fg='gold')
        f1.place(x=5,y=90,height=500,width=600)

        med=Label(f1,text="Medicine Name",font=('times new romman',15,'bold','italic','underline'),fg='black')
        med.grid(row=0,column=0,padx=20,pady=15)

        quan=Label(f1,text="Medicine Quantity",font=('times new romman',15,'bold','italic','underline'),fg='black')
        quan.grid(row=4,column=0,padx=20,pady=15)
        
        m_name = StringVar()
        m_quan=IntVar()
        mnameEntry = Entry(f1, textvariable=m_name,relief=SUNKEN,bd=7)
        mnameEntry.grid(row=0, column=3)
        mquanEntry = Entry(f1, textvariable=m_quan,relief=SUNKEN,bd=7)
        mquanEntry.grid(row=4, column=3)
        f2=LabelFrame(root,text="Bill",font=('times new romman',20,'bold','italic'),fg='gold')
        f2.place(x=700,y=90,height=500,width=600)

        f3=Frame(root,relief=GROOVE,bd=10,bg='white')
        f3.place(x=5,y=590,width=600,height=120)


        bill=partial(self.getBillTransactions,mnameEntry,mquanEntry,f2)
        cost=partial(self.totalcost,mnameEntry,mquanEntry,f2)
        win=partial(self.window,mnameEntry,mquanEntry,f2)
        enter=Button(f1,text="Enter",command=bill,font=('times new romman',15,'bold'))
        enter.grid(row=8,column=3)
        button_2=Button(f3,text="Generate Bill",command=cost,font=('times new romman',15,'bold'),bg='gold')
        button_2.grid(row=0,column=4)
        button_3=Button(f3,text="Total Cost",command=win,font=('times new romman',15,'bold'),bg='gold')
        button_3.grid(row=0,column=20,padx=30,pady=10)

        root.mainloop()


        
        

        












