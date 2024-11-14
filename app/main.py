from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .routers import auth, users, doctors, predict
from . import models
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(doctors.router)
app.include_router(predict.router)

@app.get("/")
def home():
    return {"data": "hello world"}

@app.get("/sqlalchemy")
def test(db: Session = Depends(get_db)):
  posts = db.query(models.User).all()
  return posts