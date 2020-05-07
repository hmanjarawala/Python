# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:05:26 2020

@author: Himanshu.Manjarawala
"""
from typing import List
from pydantic import BaseModel

class BookingIn(BaseModel):
    user: int
    date: str
    movies: List[int]

class Booking(BookingIn):
    id: int