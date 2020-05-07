# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:16:10 2020

@author: Himanshu.Manjarawala
"""
import os
import json
from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import Movie, MovieIn

root_dir = os.path.dirname(os.path.realpath(__file__ + '/..'))

with open("{}\\db\\movies.json".format(root_dir), "r") as f:
    fake_movie_db = json.load(f)

movies = APIRouter()

@movies.get('/', response_model=List[Movie])
async def index():
    return fake_movie_db

@movies.get('/{id}', response_model=Movie)
async def find_movie(id: int):
    if not any(movie['id'] == id for movie in fake_movie_db):
        raise HTTPException(status_code=404, detail="Movie with given id not found")
    index = [i for i,x in enumerate(fake_movie_db) if x["id"] == id][0]
    return fake_movie_db[index]

@movies.post('/', response_model=Movie, status_code=201)
async def add_movie(payload: MovieIn):
    movie = payload.dict()
    newId = [x["id"] for i,x in enumerate(fake_movie_db) if i == len(fake_movie_db)-1][0]
    response = {**movie, "id":newId+1}
    fake_movie_db.append(response)
    return response

@movies.put('/{id}', response_model=Movie)
async def update_movie(id: int, payload: MovieIn):
    movie = payload.dict()
    if not any(movie['id'] == id for movie in fake_movie_db):
        raise HTTPException(status_code=404, detail="Movie with given id not found")
    index = [i for i,x in enumerate(fake_movie_db) if x["id"] == id][0]
    response = {**movie, "id": id}
    fake_movie_db[index] = response
    return response

@movies.delete('/{id}', response_model=None)
async def delete_movie(id: int):
    if not any(movie['id'] == id for movie in fake_movie_db):
        raise HTTPException(status_code=404, detail="Movie with given id not found")
    index = [i for i,x in enumerate(fake_movie_db) if x["id"] == id][0]
    del fake_movie_db[index]
    return None