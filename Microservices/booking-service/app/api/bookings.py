# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:40:50 2020

@author: Himanshu.Manjarawala
"""

import os
import json
from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import Booking

root_dir = os.path.dirname(os.path.realpath(__file__ + '/..'))

with open("{}\\db\\bookings.json".format(root_dir), "r") as f:
    fake_movie_db = json.load(f)

bookings = APIRouter()

@bookings.get('/', response_model=List[Booking])
async def index():
    return fake_movie_db

@bookings.post('/', status_code=201)
async def add_booking(payload: Booking):
    movie = payload.dict()
    fake_movie_db.append(movie)
    return {'id': len(fake_movie_db) - 1}

@bookings.put('/{id}')
async def update_booking(id: int, payload: Booking):
    movie = payload.dict()
    movies_length = len(fake_movie_db)
    if 0 <= id <= movies_length:
        raise HTTPException(status_code=404, detail="Movie with given id not found")
    fake_movie_db[id] = movie
    return None

@bookings.delete('/{id}')
async def delete_booking(id: int):
    movies_length = len(fake_movie_db)
    if 0 <= id <= movies_length:
        raise HTTPException(status_code=404, detail="Movie with given id not found")
    del fake_movie_db[id]
    return None