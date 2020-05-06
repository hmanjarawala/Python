# -*- coding: utf-8 -*-
"""
Created on Tue May  5 16:27:47 2020

@author: Himanshu.Manjarawala
"""

from fastapi import FastAPI

from app.api.movies import movies

app = FastAPI(openapi_url="/api/v1/movies/openapi.json", docs_url="/api/v1/movies/docs")

app.include_router(movies, prefix='/api/v1/movies', tags=['movies'])