# 🔹 3. Combining Annotated + Field (Best Practice)
from pydantic import BaseModel, Field
from typing import Annotated, List

class Student(BaseModel):
    name: Annotated[str, Field(min_length=3)]
    age: Annotated[int, Field(gt=5, lt=100)]
    marks: Annotated[List[int], Field(min_length=1)]

student = Student(name="Ali", age=20, marks=[80, 90, 85])
print(student)



