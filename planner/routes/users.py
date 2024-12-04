from pydantic import BaseModel, EmailStr
from typing import Optional, List
from planner.models.events import Event

class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Config:
        Schema_extra = {'Example': {
            'email': 'fastapi@packt.com',
            'username': 'Yevhen',
            'password': 'strong!!!',
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
