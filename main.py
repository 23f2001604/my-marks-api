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

marks_data = {f"Student{i}": i for i in range(1, 101)}

@app.get("/api")
def get_marks(name: List[str] = Query([])):
    marks = []
    for student_name in name:
        mark = marks_data.get(student_name, 0)
        marks.append(mark)
    return {"marks": marks}

@app.get("/")
def read_root():
    return {"message": "Marks API is running!"}
