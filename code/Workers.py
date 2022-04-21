#!/usr/bin/python
#-*- coding: utf-8 -*-

from Employee import Employee

class Workers(Employee):
    def __init__(self,WorkHrs,JobAssigned,Skills,*args):
        super().__init__(*args)
        self.WorkHrs = WorkHrs
        self.JobAssigned = JobAssigned
        self.Skills = Skills
        print(self.e_name)

    def getTotalWorkHrs(self, e_id):
        print("Hell")

