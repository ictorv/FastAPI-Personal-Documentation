from fastapi import FastAPI,BackgroundTasks
import time
app=FastAPI()

def process_notification(email,message:str):
    time.sleep(10)
    print(f"Sending Email to {email},message: {message}")


@app.post('/send-notification/{email}')
async def send_notification(email:str, background_tasks:BackgroundTasks):
    msg="hello what's up.."
    # process_notification(email,msg)
    background_tasks.add_task(process_notification,email,msg)
    return {'message','notification sent in background_task'}