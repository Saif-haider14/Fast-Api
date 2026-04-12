from fastapi import FastAPI
app = FastAPI()

import json


def load_data():
    with open("patients.json"  , "r") as f:

        data  = json.load(f)


@app.get("/")
def home():
    return {"meassage" : "This is my home page "}


@app.get("/about")
def about():
    return {"meassage" : "This is my about page "}



@app.get("/view")

def view():
    data = load_data()
    return data 
