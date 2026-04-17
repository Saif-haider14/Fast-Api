# #claude code 

# from fastapi import FastAPI
# import json

# app = FastAPI()

# def load_data():
#     with open("patients.json", "r") as f:
#         return json.load(f)

# @app.get("/")
# def home():
#     return "Hello, Saif"

# @app.get("/view")
# def view_all():
#     data = load_data()
#     return data

# @app.get("/view/{patients_id}")
# def view_patient(patients_id: str):
#     data = load_data()
#     mydata = data.get(patients_id.upper())    


#    the get keyword searches the key in the dataset 
# if it found it it return true , otherwise , it returns false 




#     if not mydata:
#         return {"error": f"Patient '{patients_id}' not found"}

#     return mydata











# MY Code

from fastapi import FastAPI , HTTPException
import json

app = FastAPI()


def load_data():
    with open("patients.json" , "r") as f :
      
      data = json.load(f)
      return data 
    

    

@app.get("/")
def home():
    return "Hello , Saif"



@app.get("/view")
def view_all():
   data = load_data()

   return data
   




@app.get("/view/{patients_id}")
def view(patients_id : str):
   data = load_data()
   if patients_id  in data:
      return data[patients_id]
      
   raise HTTPException(status_code=404 , detail= "user not found")
#  return {"error" : f"The {patients_id} is not there"}


# 2 Methods to improve my code 
# Path function 
# HTTP Exception 
   



