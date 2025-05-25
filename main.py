from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dummy data: 100 students
marks_data = {f"Student{i}": i for i in range(1, 101)}

@app.get("/api")
def get_marks(name: List[str] = Query([])) -> dict:
    marks = [marks_data.get(student_name, 0) for student_name in name]
    return {"marks": marks}

@app.get("/")
def read_root() -> dict:
    return {"message": "Marks API is running!"}
