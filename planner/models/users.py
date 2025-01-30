from pydantic import BaseModel, EmailStr
from beanie import Document



class User(Document):
    email: EmailStr
    password: str

    class Settings:
        name = 'users'


    class Config:
        schema_extra = {
            'Example': {
                    'email': 'fastapi@packt.com',
                    'password': 'strong!!!',
                }
            }

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

'''
    class Config:
        schema_extra = {
            'Example':
                {
                    "email": 'fastapi@packt.com',
                    "password": "strong!!!",
                    # "events": [],

                }
            }
'''