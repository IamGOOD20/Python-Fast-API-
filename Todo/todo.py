from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from Todo.model import ToDo, ToDoItem, ToDoItems
from fastapi.templating import Jinja2Templates

todo_router = APIRouter()

todo_list = []

templates = Jinja2Templates(directory='templates/')

@todo_router.post('')
async def add_todo(request: Request, todo: ToDo = Depends(ToDo.as_form)):
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse('home.html',
                                      {
                                          'request': request,
                                          'todos': todo_list
                                      })

@todo_router.get('', response_model=ToDoItems)
async def retrieve_todo(request: Request):
    return templates.TemplateResponse('home.html',
                                      {
                                          'request': request,
                                          'todos': todo_list
                                      })
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(request: Request, todo_id: int = Path(..., title="The ID of the todo to retrieve.")):
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse("home.html",
                                        {
                                            'request': request,
                                            'todo': todo
                                        })

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=r'Todo with supplied ID doesn\'t exist'
    )

@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: ToDoItem, todo_id: int = Path(..., title="The ID of the todo to be updated")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
        return {"message": "Todo updated successfully."}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=r'Todo with supplied ID doesn\'t exist'
    )

@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                'message': 'Todo deleted successfully '
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=r'Todo with supplied ID doesn\'t exist'
    )

@todo_router.delete('')
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {'message': 'TOdo list successfully deleted'}
