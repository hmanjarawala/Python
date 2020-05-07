# -*- coding: utf-8 -*-
"""
Created on Thu May  7 18:59:02 2020

@author: Himanshu.Manjarawala
"""

import os
import json

from app.api.models import UserIn

root_dir = os.path.dirname(os.path.realpath(__file__ + '/..'))
print(root_dir)

with open("{}\\db\\users.json".format(root_dir), "r") as f:
    fake_user_db = json.load(f)
    print(fake_user_db)

async def get_all_users():
    return fake_user_db

async def get_user(id: int):
    if not is_user_exists(id):
        return None
    index = [i for i,x in enumerate(fake_user_db) if x["id"] == id][0]
    return fake_user_db[index]

async def add_user(userIn: UserIn):
    newId = [x["id"] for i,x in enumerate(fake_user_db) if i == len(fake_user_db)-1][0] + 1
    fake_user_db.append({"id": newId, **userIn.dict()})
    return newId

async def update_user(id: int, userIn: UserIn):
    index = [i for i,x in enumerate(fake_user_db) if x["id"] == id][0]
    response = {"id": id,**userIn.dict()}
    fake_user_db[index] = response
    return response

async def delete_user(id: int):
    index = [i for i,x in enumerate(fake_user_db) if x["id"] == id][0]
    del fake_user_db[index]
    return None

def is_user_exists(id: int):
    return any(user['id'] == id for user in fake_user_db)