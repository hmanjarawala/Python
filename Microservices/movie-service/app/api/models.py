# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:16:10 2020

@author: Himanshu.Manjarawala
"""

from pydantic import BaseModel

class MovieIn(BaseModel):
    title: str
    rating: float
    director: str
    
class Movie(MovieIn):    
    id: int