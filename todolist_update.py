#In this short script we will update our first items which was buying groceries. We finished shopping so we'll update it#to 'completed'.
import requests

url = "http://localhost:8000/todos/1"

updated_item={
        "task": "Buy groceries",
        "id" : 1,
        "completed": True
        }
response=requests.put(url,json=updated_item)
print(response.json())
