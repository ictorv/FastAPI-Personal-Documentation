from fastapi import FastAPI,APIRouter

version_v1=APIRouter()
version_v2=APIRouter()

app=FastAPI()

@version_v1.get('/task')
async def ver1():
    return {'message':'version 1'}

@version_v2.get('/task')
async def ver2():
    return {'message':'version 2'}


"""Including routes"""
app.include_router(version_v1, prefix='/v1')
app.include_router(version_v2, prefix='/v2')