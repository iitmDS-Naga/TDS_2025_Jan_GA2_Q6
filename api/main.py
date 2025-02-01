from fastapi import FastAPI, Query, HTTPException
import json

app = FastAPI()

# Load data from JSON file
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)

# Create a dictionary for quick lookups
name_marks = {item["name"]: item["marks"] for item in data}

@app.get("/api")
async def get_marks(name: list[str] = Query(..., description="List of name to get marks for")):
    try:
        marks = [name_marks[name_val] for name_val in name]
    except KeyError as e:
        raise HTTPException(
            status_code=404,
            detail=f"Name '{e.args[0]}' not found in database"
        )
    return {"marks": marks}

@app.get("/")
async def read_root():
    return {"Hello": "World"}
