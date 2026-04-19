# 🔹 1. Using Field() (constraints + metadata)
from pydantic import BaseModel, Field
from typing import List, Optional

class Patient(BaseModel):
    name: str = Field(min_length=3, max_length=50, description="Patient full name")
    age: int = Field(gt=0, lt=120, description="Age must be between 1 and 119")
    weight: float = Field(gt=0, description="Weight must be positive")
    allergies: List[str] = Field(min_length=1, description="At least one allergy required")
    email: Optional[str] = Field(default=None, description="Optional email")

patient = Patient(
    name="Saif",
    age=25,
    weight=65.5,
    allergies=["dust"]
)

print(patient)



# 💡 What Field() does:
# Adds validation rules (gt, lt, min_length)
# Adds metadata (description, title)
# Helps in FastAPI docs (Swagger UI)


# 🔹 2. Using Annotated (modern style)

# 👉 In newer Pydantic (v2), Annotated is preferred.

from pydantic import BaseModel, Field
from typing import Annotated

class Product(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=20)]
    price: Annotated[float, Field(gt=0)]
    stock: Annotated[int, Field(ge=0)]

product = Product(name="Laptop", price=1000, stock=5)
print(product)


