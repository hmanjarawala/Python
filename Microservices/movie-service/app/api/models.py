# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:16:10 2020

@author: Himanshu.Manjarawala
"""

from typing import List
from pydantic import BaseModel

class Movie(BaseModel):
    title: str
    rating: float
    director: str
    id: str