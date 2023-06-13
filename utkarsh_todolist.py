from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TodoItem(BaseModel):
    id: int
    task: str
    completed: bool


todo_items = []
'''
To get the list of all ToDo items.
'''
@app.get("/todos", response_model=List[TodoItem])
def get_todo_items():
    return todo_items
'''
To add a new item to our list. This method accepts an item of type TodoItem. 
'''
@app.post("/todos", response_model=TodoItem)
def create_todo_item(todo_item: TodoItem):
    todo_items.append(todo_item)
    return todo_item
'''
To update an item in the list. Accepts the item number and the new TodoItem. We can only change the name of the item or assign it as completed/not completed. 
'''
@app.put("/todos/{item_id}", response_model=TodoItem)
def update_todo_item(item_id: int, todo_item: TodoItem):
    for item in todo_items:
        if item.id == item_id:
            item.task = todo_item.task
            item.completed = todo_item.completed
            return item
    raise ValueError("Todo item not found")
'''
To delete an item from the list at the specified item number.
'''

@app.delete("/todos/{item_id}")
def delete_todo_item(item_id: int):
    for i, item in enumerate(todo_items):
        if item.id == item_id:
            del todo_items[i]
            return {"message": "Todo item deleted"}
    raise ValueError("Todo item not found")
