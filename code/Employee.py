#!/usr/bin/python
#-*- coding: utf-8 -*-

from tkinter import CENTER, GROOVE, X, Button, Frame, Label, Tk
from Billing import Billing



class Employee:
    def __init__(self,e_name,e_id,passw,e_phone,role):
        self.e_name = e_name
        self.e_id = e_id
        self.password = passw
        self.e_phone = e_phone
        self.role = role

    def login(self, id, passw):
        pass

    def billgeneration(self):
        obj = Billing().gui()

    def gui(self):
        root = Tk()
        root.geometry('600x450')  
        root.title('Employee')

        title=Label(root,text='Employee',bg='#2D9290',fg='White',font=('times new romman',30,'bold','italic'),relief=GROOVE,bd=5)
        title.pack(fill=X)

        frame = Frame(root)
        # frame.pack(fill=X)
        btn = Button(root,text="Billing",command=self.billgeneration)
        btn.pack(anchor=CENTER)
        root.mainloop()

Employee("","","<","","").gui()