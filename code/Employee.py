#!/usr/bin/python
#-*- coding: utf-8 -*-

class Employee:
    def __init__(self,e_name,e_id,passw,e_phone,role):
        self.e_name = e_name
        self.e_id = e_id
        self.password = passw
        self.e_phone = e_phone
        self.role = role

    def login(self, id, passw):
        pass

    def billgeneration(self, mIdArr):
        pass

