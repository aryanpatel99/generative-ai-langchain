from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name:str 
    age: Optional[int] = None
    email: EmailStr
    cgpa : float =  Field(gt=0, lt=4.0, default=0.0, description="CGPA must be between 0.0 and 4.0") 


newStudent = Student(name="Aryan", email="aryan@gmail.com", cgpa=3.5)

print(newStudent)
print(type(newStudent))