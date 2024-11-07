from fastapi import FastAPI, HTTPException, Path
from models.student import Student
from CRUD.crud import (
    create_student, get_student, get_by_id,
    update_student, delete_student, generate_student_summary)
from pydantic import BaseModel
from models.student import Student

class UpdateStudentResponse(BaseModel):
    status: str
    message: str
    data: Student

app = FastAPI()

@app.post("/students", response_model=Student)
def create(student: Student):
    return create_student(student)

@app.get("/students", response_model=dict[int, Student])
def get():
    return get_student()

@app.get("/students/{student_id}", response_model=Student)
def get__by__id(student_id: int = Path(..., description="The ID of the student you want to view")):
    student = get_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}", response_model=UpdateStudentResponse)
def update(student_id: int, student_update: Student):
    try:
        updated_student = update_student(student_id, student_update)
        return UpdateStudentResponse(
            status="success",
            message="Student updated successfully",
            data=updated_student
        )
    except HTTPException as e:
        raise e

@app.delete("/students/{student_id}")
def delete(student_id: int):
    if delete_student(student_id):
        return {"detail": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")

# API-6: Generate summary of student by ID using Ollama
@app.get("/students/{id}/summary")
async def student_summary(id: int):
    try:
        summary = generate_student_summary(id)
        return {
            "status": "success",
            "message": "Summary generated successfully",
            "data": {
                "id": id,
                "summary": summary
                }
        }
    except HTTPException as e:
        raise e