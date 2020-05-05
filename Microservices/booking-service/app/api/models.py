# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:05:26 2020

@author: Himanshu.Manjarawala
"""
from Type import List
from pydantic import BaseModel

class Booking(BaseModel):
    user: str
    date: str
    movies: List[int]