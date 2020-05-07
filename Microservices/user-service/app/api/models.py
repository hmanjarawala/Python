# -*- coding: utf-8 -*-
"""
Created on Thu May  7 18:50:19 2020

@author: Himanshu.Manjarawala
"""

from pydantic import BaseModel

class UserIn(BaseModel):
    name: str
    email: str
    bdate: str
    
    
class User(UserIn):
    id: int