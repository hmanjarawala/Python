# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 19:07:53 2020

@author: Himanshu.Manjarawala
"""

class Employee:
    'Common base class for all employees'
    employeeCount = 0  # class (static) variable
    
    def __init__(self, name, salary): # constructor
        self.name = name #member variable
        self.salary = salary #member variable
        Employee.employeeCount += 1
    
    def displayCount(self):
        print("Total Employee %d" % Employee.employeeCount)
    
    def displayEmployee(self):
        print("name: ", self.name, ", Salary:", self.salary)
    
    def __del__(self): #destructor for class
        Employee.employeeCount -= 1
        print(self.__class__.__name__, "distroyed")


if __name__ == '__main__':
    e1 = Employee("Himanshu", 50000)
    e2 = Employee("Neelam", 20000)
    
    e1.displayEmployee()
    e2.displayEmployee()
    
    print("Total Employee: %d" % Employee.employeeCount)
    
    del e1
    
    print("Total Employee: %d" % Employee.employeeCount)