"""
To characterise ver 1 & ver 2
"""

from fastapi import FastAPI,APIRouter

version_v1=APIRouter()
version_v2=APIRouter()

app=FastAPI()

@version_v1.get('/task',description='Description for API task having version 1') #Description
async def buy1():
    return {'message':'version 1'}

@version_v2.get('/task')
async def buy2():
    return {'message':'version 2'}

@version_v1.get('/work')
async def sell1():
    return {'message':'version 1'}

@version_v2.get('/work')
async def sell2():
    return {'message':'version 2'}


"""Including routes"""
app.include_router(version_v1, prefix='/v1',tags=['Version 1 API']) # Tagging
app.include_router(version_v2, prefix='/v2',tags=['Version 2 API'])