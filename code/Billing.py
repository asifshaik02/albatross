#!/usr/bin/python
#-*- coding: utf-8 -*-

class Billing:
    def __init__(self,bid,b_date,cost,quantity,m_name):
        self.b_id = bid
        self.billDate = b_date
        self.b_cost = cost
        self.quantity = quantity
        self.medicineName = m_name

    def getBillTransactions(self,bid ):
        pass

