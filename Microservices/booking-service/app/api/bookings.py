# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:40:50 2020

@author: Himanshu.Manjarawala
"""

from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import Booking, BookingIn
from app.api.services import is_movie_present, is_user_present
from app.api import db_manager

bookings = APIRouter()

@bookings.get('/', response_model=List[Booking])
async def index():
    return await db_manager.get_all_bookings()

@bookings.get('/{id}', response_model=Booking)
async def find_booking(id: int):
    booking = await db_manager.get_booking(id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking with given id not found")
    return await db_manager.get_booking(id)
        

@bookings.post('/', response_model=Booking, status_code=201)
async def add_booking(payload: BookingIn):
    
    if not is_user_present(payload.user):
        raise HTTPException(status_code=404, detail="User with given id not found")
        
    for movie_id in payload.movies:
        if not is_movie_present(movie_id):
            raise HTTPException(status_code=404, detail="Movie with given id not found")
            
    newId = await db_manager.add_booking(payload)
    return {'id': newId, **payload.dict()}

@bookings.put('/{id}', response_model=Booking)
async def update_booking(id: int, payload: BookingIn):
    booking = await db_manager.get_booking(id)
    
    if not booking:
        raise HTTPException(status_code=404, detail="Booking with given id not found")
        
    return await db_manager.update_booking(id, payload)

@bookings.delete('/{id}', response_model=None)
async def delete_booking(id: int):
    booking = await db_manager.get_booking(id)
    
    if not booking:
        raise HTTPException(status_code=404, detail="Booking with given id not found")
        
    return await db_manager.delete_booking(id)