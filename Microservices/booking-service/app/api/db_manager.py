# -*- coding: utf-8 -*-
"""
Created on Thu May  7 18:59:02 2020

@author: Himanshu.Manjarawala
"""

import os
import json

from app.api.models import BookingIn

root_dir = os.path.dirname(os.path.realpath(__file__ + '/..'))

with open("{}\\db\\bookings.json".format(root_dir), "r") as f:
    fake_booking_db = json.load(f)

async def get_all_bookings():
    return fake_booking_db

async def get_booking(id: int):
    if not is_booking_exists(id):
        return None
    index = [i for i,x in enumerate(fake_booking_db) if x["id"] == id][0]
    return fake_booking_db[index]

async def add_booking(bookingIn: BookingIn):
    newId = [x["id"] for i,x in enumerate(fake_booking_db) if i == len(fake_booking_db)-1][0] + 1
    fake_booking_db.append({"id": newId, **bookingIn.dict()})
    return newId

async def update_booking(id: int, bookingIn: BookingIn):
    index = [i for i,x in enumerate(fake_booking_db) if x["id"] == id][0]
    response = {"id": id,**bookingIn.dict()}
    fake_booking_db[index] = response
    return response

async def delete_booking(id: int):
    index = [i for i,x in enumerate(fake_booking_db) if x["id"] == id][0]
    del fake_booking_db[index]
    return None

def is_booking_exists(id: int):
    return any(booking['id'] == id for booking in fake_booking_db)