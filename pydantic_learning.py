from pydantic_learning import BaseModel

class Patient(BaseModel):
                                    # Type Validation
    name : str
    age  : int 


def patient_details():
    pass 


patient_dict = {'name' : 'saif' , 'age' : 30}

patient1 = Patient(**patient_dict)
