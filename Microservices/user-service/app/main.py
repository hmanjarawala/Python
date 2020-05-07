# -*- coding: utf-8 -*-
"""
Created on Thu May  7 19:41:11 2020

@author: Himanshu.Manjarawala
"""

from fastapi import FastAPI

from app.api.users import users

app = FastAPI(openapi_url="/api/v1/users/openapi.json", docs_url="/api/v1/users/docs")

app.include_router(users, prefix='/api/v1/users', tags=['users'])