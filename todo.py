from fastapi import APIRouter
from model import ToDo

todo_router = APIRouter()

todo_list = []

@todo_router.post('/todo')
async def add_todo(todo: ToDo) -> dict:
    todo_list.append(todo)
    return {'message': 'Todo added successfully'}

@todo_router.get('/todo')
async def retrieve_todo() -> dict:
    return {'todo_list': todo_list}

