# !/usr/bin/python
# -*- coding: utf-8 -*-

from cgitb import text
from functools import partial
from tkinter import *
from Database import Database

class Medicine:
    def __init__(self,m_name=None,m_id=None,mfg=None,t=None,rack_no=None,cost=None,exp_date=None,reorder_lvl=None):
        self.m_name = m_name
        self.m_id = m_id
        self.mfg = mfg
        self.type = t
        self.rack_no = rack_no
        self.cost = cost
        self.exp_date = exp_date
        self.reorder_lvl = reorder_lvl
        self.sq = Database()
        # self.gui()

    def getRackNo(self, m_id):
        q = f"select rack_no from medicine where m_id='{m_id}';"
        return self.sq.execute(q)

    def getType(self, m_id):
        q = f"select m_type from medicine where m_id='{m_id}';"
        return self.sq.execute(q)

    def expiryStatus(self, m_id):
        q = f"select expiry from medicine where m_id='{m_id}';"
        return self.sq.execute(q)

    def getCost(self, m_id):
        q = f"select m_cost from medicine where m_id='{m_id}';"
        return self.sq.execute(q)

    def getReorderLevel(self, m_id):
        q = f"select reorder_lvl from medicine where m_id='{m_id}';"
        return self.sq.execute(q)

    def getDetails(self,m_id):
        self.m_id = m_id.get()
        self.rack_no = self.getRackNo(self.m_id)
        self.type = self.getType(self.m_id)
        self.exp_date = self.expiryStatus(self.m_id)
        self.cost = self.getCost(self.m_id)
        self.reorder_lvl = self.getReorderLevel(self.m_id)

        

    def gui(self):
        root = Tk()
        root.geometry('600x450')  
        root.title('Medicine')

        topFrame = Frame(root)
        topFrame.pack()

        medIdLabel = Label(topFrame,text="Medicine Id:",pady=40)
        medIdLabel.grid(row=0,column=0)

        med_id = StringVar()
        medIdEntry = Entry(topFrame, textvariable=med_id)
        medIdEntry.grid(row=0, column=1)

        emptyLabel = Label(topFrame,text="")
        emptyLabel.grid(row=0,column=2)

        bottomFrame = Frame(root,pady=20)
        bottomFrame.pack()

        def show(id):
            self.getDetails(id)
            Label(bottomFrame,text="Id:").grid(row=0,column=0)
            Label(bottomFrame,text=self.m_id).grid(row=0,column=1)
            Label(bottomFrame,text="Rack:").grid(row=1,column=0)
            Label(bottomFrame,text=self.rack_no).grid(row=1,column=1)
            Label(bottomFrame,text="Type:").grid(row=2,column=0)
            Label(bottomFrame,text=self.type).grid(row=2,column=1)
            Label(bottomFrame,text="Expiry:").grid(row=3,column=0)
            Label(bottomFrame,text=self.exp_date).grid(row=3,column=1)
            Label(bottomFrame,text="Cost:").grid(row=4,column=0)
            Label(bottomFrame,text=self.cost).grid(row=4,column=1)
            Label(bottomFrame,text="Reorder level:").grid(row=5,column=0)
            Label(bottomFrame,text=self.reorder_lvl).grid(row=5,column=1)

        getDetails = partial(show, med_id)
        getRackButton = Button(topFrame,text="Medicine Details", command=getDetails)
        getRackButton.grid(row=1,column=1)
        

        return root

def forOwner():
    return obj.gui()
    
    
obj = Medicine()