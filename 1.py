from fastapi import FastAPI,Query,Form,File,UploadFile,HTTPException
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/victor")
async def vic_root():
    return {"Warning": "Victor here"}


"""Path Parameter"""
@app.get("/victor/{item}")
async def path_func(item):
    var_name={"path_variable":item}
    return var_name

# Choice Filed
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    return model_name


"""Query Parameter"""
@app.get("/query")
async def query_func(name:str, roll_no:int | None=None):
    var_name={"name":name,"roll_no":roll_no}
    return var_name

"""Request Body""" #Json Data
class schema(BaseModel):
    name:str
    cls:str
    roll:int

@app.post("/post")
async def req_body(item:schema):
    return item

"""Query Validation"""
@app.get("/queryval")
async def query_val(name:str, roll_no:str=Query(default=None, min_length=5)):
    var_name={"name":name,"roll_no":roll_no}
    return var_name

"""Form Data""" #Form Data
@app.post("/form/data")
async def form_data(username:str=Form(),password:str=Form()):
    return {"username":username,"password":password}

"""File Upload"""
@app.post("/len")
async def file_len(file:bytes=File()):
    return {"length of file":len(file)}

@app.post("/file/details")
async def file_upload(file:UploadFile):
    return {"length of file":file} #extraxt details by .detail you want

"""Error Handling"""
@app.get("/errorhandle")
async def handle_error(item:int):
    if item==2:
        raise HTTPException(status_code=400,detail='Bad Request')
    return {"item":item}
