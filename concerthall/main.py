import uvicorn 
from fastapi import FastAPI 
from src.server.router import router 
from settings import app_settings 

app = FastAPI() 
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host=app_settings.host, port=app_settings.port)