# !/usr/bin/python
# -*- coding: utf-8 -*-

from Employee import Employee

class Supervisor(Employee):
<<<<<<< HEAD
    def __init__(self,e_name,e_id,e_phone,e_password,e_role):
        self.e_name = e_name
        self.e_id = e_id
        self.e_phone = e_phone
        self.e_password = e_password
        self.e_role = e_role
        pass
=======
    def __init__(self,*args):
        super().__init__(*args)
        print(self.e_name)
>>>>>>> b7b2b9e1ca58c3505fab41d9d8a1c8000e19ec3f
    def requestMedicines(self,mid ):
        
        pass

    def assignwork(self,eid ):

        pass

    def assignWorkHrs(self, e_id,no_of_hrs):
        e_id.WorkHrs=no_of_hrs
        pass

