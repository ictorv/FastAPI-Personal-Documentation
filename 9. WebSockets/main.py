from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
app = FastAPI()

template=Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get(request:Request):
    return template.TemplateResponse("chat.html",{"request":request})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message: {data}")