from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserRead(BaseModel):
    username: str
    email: EmailStr
    created_at: datetime

    model_config = {
        "from_attributes": True
    }
