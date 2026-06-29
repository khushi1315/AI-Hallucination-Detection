from fastapi import FastAPI
from database.db import engine
from database.models import Base
from routes.chat import router as chat_router
from routes.verify import router as verify_router
from routes.history import router as history_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(chat_router)
app.include_router(verify_router)
app.include_router(history_router)

@app.get("/")
def home():
    return {"message": "Backend Running"}