# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:40:50 2020

@author: Himanshu.Manjarawala
"""

import os
import json
from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import Booking, BookingIn
from app.api.movieservices import is_movie_present

root_dir = os.path.dirname(os.path.realpath(__file__ + '/..'))

with open("{}\\db\\bookings.json".format(root_dir), "r") as f:
    fake_booking_db = json.load(f)

bookings = APIRouter()

@bookings.get('/', response_model=List[Booking])
async def index():
    return fake_booking_db

@bookings.get('/{id}', response_model=Booking)
async def find_booking(id: int):
    if any(booking['id'] == id for booking in fake_booking_db):
        raise HTTPException(status_code=404, detail="Booking with given id not found")
    index = [i for i,x in enumerate(fake_booking_db) if x["id"] == id][0]
    return fake_booking_db[index]
        

@bookings.post('/', status_code=201)
async def add_booking(payload: BookingIn):
    booking = payload.dict()
    for movie_id in payload.movies:
        if not is_movie_present(movie_id):
            raise HTTPException(status_code=404, detail="Movie with given id not found")
    newId = [x["id"] for i,x in enumerate(fake_booking_db) if i == len(fake_booking_db)-1][0]
    fake_booking_db.append({'id': newId+1, **booking})
    return {'id': len(fake_booking_db)}

@bookings.put('/{id}')
async def update_booking(id: int, payload: BookingIn):
    booking = payload.dict()
    if any(booking['id'] == id for booking in fake_booking_db):
        raise HTTPException(status_code=404, detail="Booking with given id not found")
    index = [i for i,x in enumerate(fake_booking_db) if x["id"] == id][0]
    fake_booking_db[index] = {'id': id, **booking}
    return None

@bookings.delete('/{id}')
async def delete_booking(id: int):
    if any(booking['id'] == id for booking in fake_booking_db):
        raise HTTPException(status_code=404, detail="Booking with given id not found")
    index = [i for i,x in enumerate(fake_booking_db) if x["id"] == id][0]
    del fake_booking_db[index]
    return None