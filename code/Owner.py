#!/usr/bin/python
#-*- coding: utf-8 -*-

class Owner:
    def __init__(self,name,id,phone_no,password):
        self.o_name = name
        self.o_id = id
        self.o_phone = phone_no
        self.password = password

    def login(self, id, password):
        pass

    def getEmployeeDetails(self, id):

        pass

    def getMedicineDetails(self, medicine_id):
        pass

    def getBillTransactions(self, biil_id):
        pass

    def gui(self):
        root = Tk()
        root.geometry('600x450')  
        root.title('Owner')

        topFrame = Frame(root)
        topFrame.pack()

       
        Owner_o_name = Label(topFrame,text="Owner Id:",pady=20)
        o_IdLabel.grid(row=0,column=0)

        med_id = StringVar()
        o_IdEntry = Entry(topFrame, textvariable=med_id)
        o_IdEntry.grid(row=0, column=1)

        emptyLabel = Label(topFrame,text="")
        emptyLabel.grid(row=0,column=2)

        bottomFrame = Frame(root)
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
        getRackButton = Button(topFrame,text="Medicine Details", command=getDetails,pady=20)
        getRackButton.grid(row=1,column=1)
        

        root.mainloop()
obj = Owner()