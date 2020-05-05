# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:16:10 2020

@author: Himanshu.Manjarawala
"""
import os
import json
from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import Movie

root_dir = os.path.dirname(os.path.realpath(__file__ + '/..'))

with open("{}\\db\\movies.json".format(root_dir), "r") as f:
    fake_movie_db = json.load(f)

movies = APIRouter()

@movies.get('/', response_model=List[Movie])
async def index():
    return fake_movie_db

@movies.post('/', status_code=201)
async def add_movie(payload: Movie):
    movie = payload.dict()
    fake_movie_db.append(movie)
    return {'id': len(fake_movie_db) - 1}

@movies.put('/{id}')
async def update_movie(id: int, payload: Movie):
    movie = payload.dict()
    movies_length = len(fake_movie_db)
    if 0 <= id <= movies_length:
        raise HTTPException(status_code=404, detail="Movie with given id not found")
    fake_movie_db[id] = movie
    return None

@movies.delete('/{id}')
async def delete_movie(id: int):
    movies_length = len(fake_movie_db)
    if 0 <= id <= movies_length:
        raise HTTPException(status_code=404, detail="Movie with given id not found")
    del fake_movie_db[id]
    return None