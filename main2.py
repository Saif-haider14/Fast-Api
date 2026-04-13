from fastapi import FastAPI
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
def view():
   data = load_data()

   return data
   




@app.get("/view/{patients_id}")
def view(patients_id : str):
   data = load_data()

   mydata = data[patients_id]

   return mydata
   



# claude code 

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
#     mydata = data.get(patients_id)

#     if not mydata:
#         return {"error": f"Patient '{patients_id}' not found"}

#     return mydata