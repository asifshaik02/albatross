#!/usr/bin/python
#-*- coding: utf-8 -*-

from Employee import Employee

class Workers(Employee):
    def __init__(self,WorkHrs,JobAssigned,Skills):
        self.WorkHrs = WorkHrs
        self.JobAssigned = JobAssigned
        self.Skills = Skills

    def getTotalWorkHrs(self, e_id):
        pass

