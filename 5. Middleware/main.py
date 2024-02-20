from fastapi import FastAPI,Request, HTTPException

app=FastAPI()

@app.middleware("http")
async def custom_middleware(request:Request,call_next):
    print("Before Request")

    if "query_args" not in request.query_params:
        raise HTTPException(status_code=400, detail='required parameter {query_args} is missing')
    
    response=await call_next(request)
    print("After request")
    return response

@app.get("/")
async def home():
    return {'message':'Hello'}