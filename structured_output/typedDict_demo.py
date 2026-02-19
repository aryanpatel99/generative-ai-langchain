from typing import TypedDict

class User(TypedDict):
    name:str
    age:int 


user1:User = {
    "name":"Aryan",
    "age": "22" # This will still work because TypedDict does not enforce type checking at runtime, but it will raise a type checker warning since 'age' is expected to be an int, not a str.
}

print(user1)