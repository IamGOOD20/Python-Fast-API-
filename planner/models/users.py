from pydantic import BaseModel, EmailStr
from typing import Optional, List
from .events import Event

class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Config:
        Schema_extra = {'Example': {
            'email': 'fastapi@packt.com',
            'username': 'strong!!!',
            'events': [],
            }
        }

class UserSignIn(BaseModel):
    email = EmailStr
    password = str

    class Config:
        Schema_extra = {
            'Example': {
                "email": 'fastapi@packt.com',
                "password": "strong!!!",
                "events": [],

            }
        }
