from fastapi import FastAPI, Form

import pytz
import time
from PIL import Image
#from flask import Flask, request
#from face_recognition import preprocessing
#import joblib
#from pymongo import MongoClient
import datetime
#from flask_cors import CORS
import json
import base64
from io import BytesIO
#from werkzeug import serving
#import ssl
from pydantic import BaseModel

"""
#mongodb connection
myclient = MongoClient("mongodb://localhost:27017/")
#add db and collection
mydb = myclient["face_data"]
mycol = mydb["users"]
"""

#face_recogniser = joblib.load('model/face_recogniser.pkl')
#preprocess = preprocessing.ExifOrientationNormalize()

#facereco = APIRouter()
app = FastAPI()

class Item(BaseModel):
    file: str

@app.get("/test/{name}")
async def index(*, name:str):
    return {"Result":"Success"}
   

@app.post("/predict")
async def root(*, file:str = Form(...)):
    thresh = 0.6

    img = file
    f = open('test.png', 'w')
    f.write(img)
    f.close()
    f = open('test.png', 'rb').read()[22:]

    img =Image.open(BytesIO(base64.b64decode(f)))
    print("------------")
    print(img.size)
    print("hot1")
    print("--------")
    a = int(round(time.time() * 1000))
    img = preprocess(img)
    img = img.convert('RGB')
    faces = face_recogniser(img)
    #data = {}
    mapping = {"Abhijeet" : "EY101",
"Ashish_Banka" : "EY102",  
    "Jatin" : "EY103",
    "Jitender" : "EY104",
     "Mrunal_Lohia" : "EY105",
    "sai" : "EY106",
     "sindhu" : "EY107",
    "somendra" : "EY108",
    "sudarshan" : "EY109",
    "suman" : "EY110",
      "Vikas_Ahuja":"EY111",
    "Sumit_Gupta":"EY112",
    "Manoj_Kumar":"V114",
    "Amanpreet_Singh":"V115",
    "Kushagra_Verma":"V116"}
    results = {
            'faces': [
                {
                    'top_prediction': face.top_prediction._asdict(),
                    }
                for face in faces if face.top_prediction._asdict()['confidence']>=thresh
                ]
            }
    b = int(round(time.time() * 1000))
    tt = int((b-a)/10)
    print("hit 2")
    data = {'Employee_ID':'Unknown',
             'Name': "Unknown",
            'Score': 0,
            'Time': str(datetime.datetime.now(pytz.timezone('Asia/Kolkata'))).split()[1].split(".")[0],
            'Time_Taken': tt,
            'Day': str(datetime.datetime.now().day)}
    try:
        name = results['faces'][0]['top_prediction']['label']
        print(name)
        print("hot 2")
        print(mapping[name])
        data = {'Employee_ID':mapping[name],
            'Name': name,
            'Score': round(results['faces'][0]['top_prediction']['confidence'], 2)*100,
            'Time': str(datetime.datetime.now(pytz.timezone('Asia/Kolkata'))).split()[1].split(".")[0],
            'Time_Taken': tt,
            'Day': str(datetime.datetime.now())}
    except Exception as e:
        print(e)
    """
   # mycol.in
    try:
        mycol.insert_one(json.loads(json.dumps(data)))
    except Exception as e:
        print(e)
    """
    print(data)
    return data

