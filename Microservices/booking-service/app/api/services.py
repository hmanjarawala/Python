# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:24:41 2020

@author: Himanshu.Manjarawala
"""

import os
import httpx

MOVIE_SERVICE_HOST_URL = 'http://localhost:8002/api/v1/movies/'
url = os.environ.get('MOVIE_SERVICE_HOST_URL') or MOVIE_SERVICE_HOST_URL

def is_movie_present(movie_id: int):
    r = httpx.get(f'{url}{movie_id}')
    return True if r.status_code == 200 else False

USER_SERVICE_HOST_URL = 'http://localhost:8003/api/v1/users/'
url1 = os.environ.get('USER_SERVICE_HOST_URL') or USER_SERVICE_HOST_URL

def is_user_present(user_id: int):
    r = httpx.get(f'{url1}{user_id}')
    return True if r.status_code == 200 else False