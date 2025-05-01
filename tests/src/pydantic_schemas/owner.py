from pydantic import BaseModel, EmailStr
from pydantic_extra_types.payment import PaymentCardNumber



class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr