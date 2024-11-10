from fastapi import APIRouter, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import schemas, database, utils, models

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=schemas.ResponseUser)
def create_user(user: schemas.CreateUser, db: Session = Depends(database.get_db)):
    
    # We need to hash the password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    new_user = models.User(**user.dict())
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    print("--------------------")
    print("User data:", user.dict())
    print("Hashed password:", hashed_password)
    print("New user instance:", new_user)
    
    return new_user

@router.get("/{id}", response_model=schemas.ResponseUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")
        
    return user