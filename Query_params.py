from fastapi import FastAPI, Query, HTTPException
import json

app = FastAPI()


# Load data from JSON
def load_data():
    with open("richest_people.json", "r", encoding="utf-8") as f:
        return json.load(f)


# Function to extract numeric net worth (your logic)
def extract_networth(person):
    value = person["Net Worth"]
    return float(value.replace("$", "").replace(" Billion", ""))


# Endpoint with query parameter
@app.get("/view")
def view_all(
    order: str = Query(
        "desc",
        description="Sorting order: 'asc' or 'desc'",
        example="asc"
    )
):
    data = load_data()

    if not data:
        raise HTTPException(status_code=404, detail="No data found")

    # Convert dictionary to list
    people_list = list(data.values())

    # Sorting using your logic
    sorted_people = sorted(
        people_list,
        key=extract_networth,
        reverse=True if order.lower() == "desc" else False
    )

    return sorted_people
