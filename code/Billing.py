from tkinter import *
from functools import partial
#from PIL import ImageTk,Image


root=Tk()
root.title("Medical Store Billing")
root.geometry("600x480")

title=Label(root,text='Medicines Billing System',bg='#2D9290',fg='White',font=('times new romman',40,'bold','italic'),relief=GROOVE,bd=10)
title.pack(fill=X)

# --------Medicines details----#
f1=LabelFrame(root,text="Medicine Details",font=('times new romman',20,'bold','italic'),fg='gold')
f1.place(x=5,y=90,height=500,width=800)

med=Label(f1,text="Medicine Id",font=('times new romman',15,'bold','italic','underline'),fg='black')
med.grid(row=0,column=0,padx=20,pady=15)

quan=Label(f1,text="Medicine Quantity",font=('times new romman',15,'bold','italic','underline'),fg='black')
quan.grid(row=0,column=3,padx=20,pady=15)

#------Details----#
mid = StringVar()
midEntry = Entry(f1, textvariable=mid,relief=SUNKEN,bd=7).grid(row=1, column=0)

mquan = StringVar()
mquanEntry = Entry(f1, textvariable=mquan,relief=SUNKEN,bd=7).grid(row=1, column=3)


#-----Bill -----#
f2=Frame(root,relief=GROOVE,bd=10)
f2.place(x=820,y=90,width=500,height=500)
reciept=Label(f2,text="Bill",relief=GROOVE,font=('times new romman',15,'bold'),bd=7,fg='black').pack(fill=X)

#-------Buttons----#
f3=Frame(root,relief=GROOVE,bd=10)
f3.place(x=5,y=590,width=900,height=120)

button_1=Button(f3,text="Total Cost",font=('times new romman',15,'bold'),bg='gold')
button_1.grid(row=0,column=0,padx=20,pady=10)

button_2=Button(f3,text="Generate Bill",font=('times new romman',15,'bold'),bg='gold')
button_2.grid(row=0,column=4)




root.mainloop()
class Billing:
    def __init__(self,bid,b_date,cost,quantity,m_name):
        self.b_id = bid
        self.billDate = b_date
        self.b_cost = cost
        self.quantity = quantity
        self.medicineName = m_name

    def getBillTransactions(self,bid ):
        pass

