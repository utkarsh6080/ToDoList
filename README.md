# ToDoList
This is a simple to-do list application built using FastAPI.

The features are:
Create a new to-do item with an ID, task description, and completion status.
Retrieve the list of all to-do items.
Update the details of an existing to-do item.
Delete a to-do item from the list.

To test the application:
First run utkarsh_todolist.py (I used uvicorn to run it). Then access the endpoints. See the empty list. 
Then, run todolist_additems.py to add two items to the list. Check the updated list by refreshing the browser.
Then, run todolist_update.py to assign the first item as completed. Check the updated list by refreshing the browser.
Then, run todolist_delete.py to delete the first item. Check the updated list by refreshing the browser.
