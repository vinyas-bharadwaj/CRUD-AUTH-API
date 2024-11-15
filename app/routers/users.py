import io
import os
from uuid import uuid4
from PIL import Image as PILImage
from fastapi import APIRouter, File, Response, UploadFile, status, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import schemas, database, utils, models

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=schemas.ResponseUser)
async def create_user(
    user: schemas.CreateUser, 
    db: Session = Depends(database.get_db), 
    profile_image: UploadFile = File(...)
):
    # Hash the password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    # Extracting and processing the profile picture
    image_bytes = await profile_image.read()
    try:
        # Load the image to check if it's valid
        img = PILImage.open(io.BytesIO(image_bytes))
        img.verify()  # Verify that the image is valid
        
        # Resize and save the image
        img = img.resize((70, 70))
        unique_filename = f"{uuid4().hex}.jpg"
        file_path = os.path.join("media", unique_filename)
        img.convert("RGB").save(file_path, format="JPEG")
        
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid image file")

    # Create the new user and associate the profile image URL
    new_user = models.User(
        username=user.username,
        email=user.email,
        password=user.password,  # already hashed
        profile_pic=file_path  # Save the image path to the profile_pic field
    )

    # Add to the database session and commit
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Return a response without the password
    return {
        "username": new_user.username,
        "email": new_user.email,
        "profile_pic": new_user.profile_pic  # Return the path to the profile image
    }

@router.get("/{id}", response_model=schemas.ResponseUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")
        
    return user