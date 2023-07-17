from pydantic import BaseModel, EmailStr


class Email(BaseModel):
    destination: EmailStr
    subject: str
    body: str
