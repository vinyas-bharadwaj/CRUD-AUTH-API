from fastapi import APIRouter, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import schemas, database, utils, models

router = APIRouter(
    prefix="/predict",
    tags=["Prediction"]
)

@router.post('/')
def make_prediction(info: int):
    pass