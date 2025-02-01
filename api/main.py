from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# with open("q-vercel-python.json", "r") as f:
#     data = json.load(f)

# name_marks = {item["name"]: item["marks"] for item in data}


students_df = pd.read_csv("q-fastapi.csv")
students_data = students_df.to_dict(orient="records")

@app.get("/api")
async def get_students(class_: list[str] = Query(None, alias="class")):
    if class_:
        filtered_students = [student for student in students_data if student["class"] in class_]
        return filtered_students
    return students_data

# @app.get("/api")
# async def get_marks(name: list[str] = Query(..., description="List of name to get marks for")):
#     try:
#         marks = [name_marks[name_val] for name_val in name]
#     except KeyError as e:
#         raise HTTPException(
#             status_code=404,
#             detail=f"Name '{e.args[0]}' not found in database"
#         )
#     return {"marks": marks}

@app.get("/")
async def read_root():
    return {"Hello": "World", "Build Number": "6"}
