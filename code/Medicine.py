#!/usr/bin/python
#-*- coding: utf-8 -*-

class Medicine:
    def __init__(self,m_name,m_id,mfg,t,rack_no,cost,exp_date,reorder_lvl):
        self.m_name = m_name
        self.m_id = m_id
        self.mfg = mfg
        self.type = t
        self.rack_no = rack_no
        self.cost = cost
        self.exp_date = exp_date
        self.reorder_lvl = reorder_lvl

    def getRackNo(self, m_id):
        pass

    def getType(self, m_id):
        pass

    def expiryStatus(self, m_id):
        pass

    def getCost(self, m_id):
        pass

    def getReorderLevel(self, m_id):
        pass

