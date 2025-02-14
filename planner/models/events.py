from beanie import Document
from typing import List, Optional
from pydantic import BaseModel

class Event(Document):
    # id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            'example': {
                'title': 'FastAPI Book Launch',
                'image': 'https: linktomyimage.com/image.png',
                'description': 'We will be discussing the contents of the FastAPI book in this event. '
                         'Ensure to come with your own copy to win gifts!',
                'tags': ["python", "fastapi", "book", "launch"],
                'location': 'Google meet'
            }
        }


    class Settings:
        name = 'events'

class EventUpdate(BaseModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https:linktomyimage.com / image.png",
                "description": "We will bediscussing the contents of the FastAPI book in this event."
                               "Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }
