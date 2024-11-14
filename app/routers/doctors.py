from fastapi import APIRouter, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import schemas, database, utils, models

router = APIRouter(
    prefix="/Doctor",
    tags=["Doctors"]
)

@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=schemas.ResponseDoctor)
def create_doctor(doc: schemas.CreateDoctor, db: Session = Depends(database.get_db)):
    
    # We need to hash the password
    hashed_password = utils.hash(doc.password)
    doc.password = hashed_password
    
    new_doctor = models.Doctor(**doc.dict())
    
    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)
    
    
    return new_doctor

@router.get("/{id}", response_model=schemas.ResponseDoctor)
def get_doctor(id: int, db: Session = Depends(database.get_db)):
    doctor = db.query(models.Doctor).filter(models.Doctor.id == id).first()
    
    if doctor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Doctor with id: {id} does not exist")
        
    return doctor