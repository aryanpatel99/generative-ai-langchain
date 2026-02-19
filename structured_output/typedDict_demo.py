from typing import TypedDict

class User(TypedDict):
    name:str
    age:int 


user1:User = {
    "name":"Aryan",
    "age": "22"
}

print(user1)