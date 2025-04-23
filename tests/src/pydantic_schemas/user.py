from pydantic import BaseModel, field_validator

from src.enums.user_enums import Gender, Status, UserErrors

class User(BaseModel):
    id: int 
    name: str
    email: str
    gender: Gender
    status: Status

    @field_validator("email")
    def check_email(cls, v):
        if "@" not in v:
            raise ValueError(UserErrors.WRONG_EMAIL.value)
        return v

    

