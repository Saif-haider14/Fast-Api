import json
from typing import Annotated, Literal
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field

app = FastAPI()

# --- Utility Functions for Data Persistence --- [1, 2]

def load_data():
    """Loads existing patient data from the JSON file database."""
    with open("patients.json", "r") as f:
        return json.load(f)

def save_data(data):
    """Saves the updated dictionary back to the JSON file."""
    with open("patients.json", "w") as f:
        json.dump(data, f)

# --- Pydantic Model for Data Validation --- [3-8]

class Patient(BaseModel):
    # Core fields with validation and metadata [4-6]
    id: Annotated[str, Field(description="ID of the patient", examples=["P001"])]
    name: Annotated[str, Field(description="Name of the patient")]
    city: Annotated[str, Field(description="City where the patient is living")]
    age: Annotated[int, Field(gt=0, lt=120, description="Age of the patient")]
    gender: Annotated[Literal["male", "female", "others"], Field(description="Gender of the patient")]
    height: Annotated[float, Field(gt=0, description="Height of the patient in meters")]
    weight: Annotated[float, Field(gt=0, description="Weight of the patient in kg")]

    # Computed fields for dynamic data [7, 8]
    @computed_field
    @property
    def bmi(self) -> float:
        """Calculates BMI automatically based on height and weight."""
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    @property
    def verdict(self) -> str:
        """Calculates health verdict based on the computed BMI."""
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Normal"  # Source text mentions 'normal' again for < 30 [8]
        else:
            return "Obese"

# --- FastAPI App and Endpoint --- [9, 10]

app = FastAPI()

@app.post("/create")
def create_patient(patient: Patient):
    """
    Endpoint to create a new patient. 
    The 'patient' parameter automatically captures and validates the Request Body. [11]
    """
    # 1. Load existing database [1]
    data = load_data()

    # 2. Check for duplicate patient IDs [1, 12]
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")

    # 3. Add new patient to the dictionary [12, 13]
    # Convert Pydantic object to dict and exclude 'id' as it's the key
    patient_dict = patient.model_dump(exclude={"id"})
    data[patient.id] = patient_dict

    # 4. Save updated data back to JSON file [2]
    save_data(data)

    # 5. Return success response to the client [10]
    return JSONResponse(
        status_code=201, 
        content={"message": "Patient created successfully"}
    ) 