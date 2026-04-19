from pydantic import BaseModel
from typing import List , Dict , Optional

class Patient(BaseModel):
                                    # Type Validation          # 3 steps in pydantic 
                                                                # No1 Schema pydantic model
                                                                # No 2 Pydantic object 
                                                                # No3 used this object in you function to perform tasks 
    name : str    # these prameters are require 
                  # if user cant provide thse values raises the error 
    age  : int 
    weight : float 
    allergies : List[str]
    contact_details : Optional[Dict[str , str]] = None
    # if user cant provide the value of contact details , nothing goes wrong , the code works 


def patient_details(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("the data has been inserted")
    


patient_dict = { 'name' : 'saif', 'age' : 30 , 'allergies' : ['malice' , 'pimples' , 'diabetics']}

patient1 = Patient(**patient_dict)

patient_details(patient1)

 # 3 steps in pydantic 
                                                                # No1 Schema pydantic model
                                                                # No 2 Pydantic object 
                                                                # No3 used this object in you function to perform tasks 
 
