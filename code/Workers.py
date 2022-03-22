#!/usr/bin/python
#-*- coding: utf-8 -*-

from Employee import Employee

class Workers(WorkHrs,JobAssigned,Skills):
    def __init__(self):
        self.WorkHrs = WorkHrs
        self.JobAssigned = JobAssigned
        self.Skills = Skills

    def getTotalWorkHrs(self, ):
        pass

