# !/usr/bin/python
# -*- coding: utf-8 -*-

from Employee import Employee

class Supervisor(Employee):

    def __init__(self,*args):
        super().__init__(*args)
        print(self.e_name)
        
    def requestMedicines(self,mid ):
        
        pass

    def assignwork(self,eid ):

        pass

    def assignWorkHrs(self, e_id,no_of_hrs):
        e_id.WorkHrs=no_of_hrs
        pass

