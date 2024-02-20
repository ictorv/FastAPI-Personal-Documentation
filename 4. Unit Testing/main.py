from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Creating Get Endpoint

@app.get("/get_info")
async def get_fun():
    return {"message": "Hello World"}

#Creating Post Endpoint
class mod(BaseModel):
    name:str
    cls:str
    roll:int

@app.post("/post_info")
async def post_fun(item:mod):
    return item