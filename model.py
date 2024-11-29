from pydantic import BaseModel

class ToDo(BaseModel):
    id: int
    item: str

    class Config:
        Schema_extra = {"Example": {
            "id": 1,
            "item": "Example schema!"
            }
        }

class ToDoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {"example": {
            "item": "Read the next chapter of the book"
            }
        }

