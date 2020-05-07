# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:16:10 2020

@author: Himanshu.Manjarawala
"""
from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import Movie, MovieIn
from app.api import db_manager

movies = APIRouter()

@movies.get('/', response_model=List[Movie])
async def index():
    return await db_manager.get_all_movies()

@movies.get('/{id}', response_model=Movie)
async def find_movie(id: int):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie with given id not found")
    return await db_manager.get_movie(id)

@movies.post('/', response_model=Movie, status_code=201)
async def add_movie(payload: MovieIn):
    newId = await db_manager.add_movie(payload)
    return {**payload.dict(), "id":newId}

@movies.put('/{id}', response_model=Movie)
async def update_movie(id: int, payload: MovieIn):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie with given id not found")
    return await db_manager.update_movie(id, payload)

@movies.delete('/{id}', response_model=None)
async def delete_movie(id: int):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie with given id not found")
    return await db_manager.delete_movie(id)