#Lets now try deleting our first item since its already completed.

import requests

url="http://localhost:8000/todos/1"

response = requests.delete(url)
print(response.json())
