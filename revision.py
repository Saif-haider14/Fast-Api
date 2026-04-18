from fastapi import FastAPI , HTTPException , Path , Query
import json

app = FastAPI()


# function to load the data 
def load_data():
    with open("richest_people.json" , "r") as f :
        data = json.load(f)
        return data 


# Reterive operation

@app.get("/view")
def view_all():
    data =load_data()
    return data 



@app.get("/view/{richest_person_code}")
def view_specific(richest_person_code: str = Path(..., description=" here you enter the code of the client" ,Example = "R001")):
    
    data = load_data()

    # Convert input to uppercase
    richest_person_code = richest_person_code.upper()

    if richest_person_code in data:
        return data[richest_person_code]

    raise HTTPException(status_code=404, detail="Invalid code")



# We make our code better with these two techniques
# Path method / path function 
# HTTP  Exception Request    (use for handle the exception , )



# optimize code 

# from fastapi import FastAPI, HTTPException, Path
# import json

# app = FastAPI()


# # Function to load the data
# def load_data():
#     with open("richest_people.json", "r", encoding="utf-8") as f:
#         return json.load(f)


# # Retrieve all records
# @app.get("/view")
# def view_all():
#     return load_data()


# # Retrieve a specific record
# @app.get("/view/{richest_person_code}")
# def view_specific(
#     richest_person_code: str = Path(
#         ...,
#         description="Here you enter the code of the client",
#         example="R001"
#     )
# ):
#     data = load_data()

#     # Convert input to uppercase for case-insensitive search
#     richest_person_code = richest_person_code.upper()

#     if richest_person_code in data:
#         return data[richest_person_code]

#     raise HTTPException(status_code=404, detail="Invalid code")


@app.get('/sort')
def sort_richestpeople(sortby : str = Query(..., "sort on the bases of networth") , order : str = Query('asc' , description = "order in asc")):
    if sortby != "networth" :
        raise HTTPException(status_code=400 , description = "invalid field selected")
    
    if order not in ['asc' , 'dsc']:
        raise HTTPException(status_code=400 , description = "invalid field selected")



    
         


         
          
          
