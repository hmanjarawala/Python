# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 19:30:20 2020

@author: Himanshu.Manjarawala
"""

from IntroductionClass import Employee

if __name__ == '__main__':
    emp1 = Employee("Neelam", 2000)
    emp2 = Employee("Himanshu", 5000)
    print ("Employee.__doc__:", Employee.__doc__)
    print ("Employee.__name__:", Employee.__name__)
    print ("Employee.__module__:", Employee.__module__)
    print ("Employee.__bases__:", Employee.__bases__)
    print ("Employee.__dict__:", Employee.__dict__ )
    
    # Accessing attributes
    print(hasattr(emp1, 'salary'))
    print(getattr(emp1, 'salary'))
    setattr(emp1, 'salary', 2500)
    print(getattr(emp1, 'salary'))
    delattr(emp1, 'salary')
    print(hasattr(emp1, 'salary'))