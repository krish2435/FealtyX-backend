from models.student import Student
from typing import Optional, Dict
from fastapi import HTTPException, APIRouter
import requests
import json 

app = APIRouter()

students = {}

def create_student(student: Student) -> Student:
    if student.id in students:
        raise HTTPException(status_code=400, detail="Student with this ID already exists.")
    students[student.id] = student
    return student

def get_student() -> Dict[int, Student]:
    if not students:
        raise HTTPException(status_code=404, detail="No students found.")
    return students

def get_by_id(student_id: int) -> Optional[Student]:
    student = students.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
    return student

def update_student(student_id: int, student_update: Student) -> Student:
    if student_id in students:
        students[student_id] = student_update
        return students[student_id]
    else:
        raise HTTPException(status_code=404, detail="Student not found")
    
def delete_student(student_id: int) -> bool:
    if student_id in students:
        del students[student_id]
        return {"status": "success", "message": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found.")

url = "http://localhost:11434/api/generate"
headers = {
    'Content-Type': "application/json"
}

def generate_student_summary(student_id: int) -> Optional[str]:
    student = students.get(student_id)
    if student:
        data = {
            "model": "llama3.2",
            "prompt": f"Generate a brief summary of this student's data in a single sentence: {student}.",
            "stream": False
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            data = response.json()
            summary = data['response'].rsplit("\n", 1)[-1].strip()
            return summary
    raise HTTPException(status_code=404, detail="Student not found or summary generation failed.")
