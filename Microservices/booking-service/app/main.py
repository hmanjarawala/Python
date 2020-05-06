# -*- coding: utf-8 -*-
"""
Created on Tue May  5 16:27:47 2020

@author: Himanshu.Manjarawala
"""

from fastapi import FastAPI

from app.api.bookings import bookings

app = FastAPI(openapi_url="/api/v1/bookings/openapi.json", docs_url="/api/v1/bookings/docs")

app.include_router(bookings, prefix='/api/v1/bookings', tags=['bookings'])