#Lets add two items to our list

import requests

url = "http://localhost:8000/todos"

# New item data
new_item_1 = {
    "id": 1,
    "task": "Buy groceries",
    "completed": False
    }

new_item_2={
        "id": 2,
        "task": "Book a flight to NYC",
        "completed": False
        }

response_1 = requests.post(url, json=new_item_1)
response_2 = requests.post(url, json=new_item_2)
print(response_1.json())
print(response_2.json())
