from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routes import user

# Database ki tables create karega
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user.router, prefix="/users", tags=["Users"])

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Travel Planner 🚀"
    }