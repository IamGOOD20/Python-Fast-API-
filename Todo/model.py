from fastapi import Form
from pydantic import BaseModel
from typing import List, Optional

class ToDo(BaseModel):
    id: int
    item: str

    @classmethod
    def as_form(cls, item: str = Form(...)
                ):
        return cls(item=item)

    class Config:
        Schema_extra = {"Example": {
            "id": 1,
            "item": "Example schema!"
            }
        }

class ToDoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Read the next chapter of the book"
            }
        }

class ToDoItems(BaseModel):
    todos: List[ToDoItem]

    class Config:
        schema_extra = {
            'example': {
                "todos": [
                    {
                        "item": "Example schema 1!"
                    },
                    {
                        "item": "Example schema 2!"
                    }
                ]
            }
        }
