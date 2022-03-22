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

