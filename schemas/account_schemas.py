from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr



class AccountCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password: str
    birthdate: datetime
    phone_number: Optional[str]

    class Config:
        json_schema_extra = {
        "example":{
            "name": "Antanas",
            "surname": "Fontanas",
            "email": "NameError@Fontanas.lt",
            "password": "123",
            "birthdate": "2023-07-11T18:08:53.419Z",
            "phone_number": "+3706666666"
            }
        }
    