from pydantic import BaseModel, EmailStr
from typing import List, Optional

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        Schema_extra = {'Example': {
            'title': 'FastAPI Book Launch',
            'image': 'https: linktomyimage.com/image.png',
            'description': 'We will be discussing the contents of the FastAPI book in this event. '
                     'Ensure to come with your own copy to win gifts!',
            'tags': ["python", "fastapi", "book", "launch"],
            'location': 'Google meet'
            }
        }


