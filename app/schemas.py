import io
import os
from uuid import uuid4
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from datetime import datetime
from PIL import Image as PILImage


class CreateUser(BaseModel):
    username: str
    email: EmailStr
    password: str
    
    
class CreateDoctor(BaseModel):
    username: str
    email: EmailStr
    password: str

class ResponseUser(BaseModel):
  id: int
  email: EmailStr
  created_at: datetime
  profile_pic: str

  class Config:
    orm_mode = True
    
class ResponseDoctor(BaseModel):
  id: int
  email: EmailStr
  created_at: datetime

  class Config:
    orm_mode = True
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[int] = None
    
     