# -*- coding: utf-8 -*-
"""
Created on Thu May  7 19:10:25 2020

@author: Himanshu.Manjarawala
"""

from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import User, UserIn
from app.api import db_manager

users = APIRouter()

@users.get('/', response_model=List[User])
async def index():
    return await db_manager.get_all_users()

@users.get('/{id}', response_model=User)
async def find_user(id: int):
    user = await db_manager.get_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User with given id not found")
    return await db_manager.get_user(id)

@users.post('/', response_model=User, status_code=201)
async def add_user(payload: UserIn):
    newId = await db_manager.add_user(payload)
    return {"id": newId, **payload.dict()}

@users.put('/{id}', response_model=User)
async def update_user(id: int, payload: UserIn):
    user = await db_manager.get_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="Movie with given id not found")
    return await db_manager.update_user(id, payload)

@users.delete('/{id}', response_model=None)
async def delete_user(id: int):
    user = await db_manager.get_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="Movie with given id not found")
    return await db_manager.delete_user(id)