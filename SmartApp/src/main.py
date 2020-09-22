# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:54:31 2020

@author: Himanshu.Manjarawala
"""
import uvicorn
from fastapi import FastAPI, Path, Request
from fastapi.responses import JSONResponse

import workflow_runner
from models import MyException, Configuration, Index

app = FastAPI(title='SMART Data Science Application',
              description='A Smart Data Science Application running on FastAPI + uvicorn',
              version='0.0.1')

@app.get("/{index}")
async def get_result(index: Index = Path(..., title="The name of the Index")):
    
    config = Configuration(
        index=index
    )
    try:
        result = await workflow_runner.run(config)
        return JSONResponse(status_code=200, content=result)
    except Exception as e:
        raise MyException(e)

@app.exception_handler(MyException)
async def unicorn_exception_handler(request: Request, exc: MyException):
    return JSONResponse(
        status_code=418,
        content={"message": "Error occurred! Please contact the system admin."},
    )

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)