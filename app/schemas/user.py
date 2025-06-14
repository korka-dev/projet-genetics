from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    name: str
    password: str
    phone_number: str
    appartement: str  

class UserOut(BaseModel):
    id: UUID
    name: str
    phone_number: str
    appartement: str 
    created_at: datetime



class ChangePassword(BaseModel):
    phone_number: EmailStr
    old_password: str
    new_password: str


class ForgotPassword(BaseModel):
    phone_number: EmailStr
    new_password: str

    class Config:
       from_attributes = True


class UserUpdate(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[str] = None
    appartement: Optional[str] = None


