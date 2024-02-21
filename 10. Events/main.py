from fastapi import FastAPI, Request, Response

app=FastAPI()


#Event Handler for startup
@app.on_event("startup")
async def startup_event():
    print("Event started")
    # Add Functionality


#Event Handler for shutdown
@app.on_event("shutdown")
async def shutdown_event():
    print("Event Turned Off")
    # Add Functionality


@app.get('/')
async def read_root():
    return {'messsage':'Fast API Event'}