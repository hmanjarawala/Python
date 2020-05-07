# -*- coding: utf-8 -*-
"""
Created on Thu May  7 18:59:02 2020

@author: Himanshu.Manjarawala
"""

import os
import json

from app.api.models import MovieIn

root_dir = os.path.dirname(os.path.realpath(__file__ + '/..'))

with open("{}\\db\\movies.json".format(root_dir), "r") as f:
    fake_movie_db = json.load(f)

async def get_all_movies():
    return fake_movie_db

async def get_movie(id: int):
    if not is_movie_exists(id):
        return None
    index = [i for i,x in enumerate(fake_movie_db) if x["id"] == id][0]
    return fake_movie_db[index]

async def add_movie(movieIn: MovieIn):
    newId = [x["id"] for i,x in enumerate(fake_movie_db) if i == len(fake_movie_db)-1][0] + 1
    fake_movie_db.append({**movieIn.dict(),"id": id})
    return newId

async def update_movie(id: int, movieIn: MovieIn):
    index = [i for i,x in enumerate(fake_movie_db) if x["id"] == id][0]
    response = {**movieIn.dict(),"id": id}
    fake_movie_db[index] = response
    return response

async def delete_movie(id: int):
    index = [i for i,x in enumerate(fake_movie_db) if x["id"] == id][0]
    del fake_movie_db[index]
    return None

def is_movie_exists(id: int):
    return any(movie['id'] == id for movie in fake_movie_db)