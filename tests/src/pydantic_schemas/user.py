from pydantic import BaseModel, field_validator
from typing import Optional

from src.enums.user_enums import Gender, Status, UserErrors

class User(BaseModel):
    id: int 
    name: str
    email: str
    password: Optional[str] = None
    gender: Gender
    status: Status


    
    @field_validator("password")
    def check_email(cls, email):
        if "@" not in email:
            raise ValueError(UserErrors.WRONG_EMAIL.value)
        else:
            return email

    

