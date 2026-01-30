from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from database import get_db
from datetime import date

router = APIRouter(prefix="/register", tags=["Register"])

class Student(BaseModel):
    name: str
    dob: date
    class_name: str
    gender: str
    parent_name: str
    phone: str
    email: EmailStr
    address: str
    
@router.post("/")
def register_student(student: Student):
    db = get_db()
    cursor = db.cursor()

    sql = """
    INSERT INTO registrations 
    (student_name, dob, class, gender, parent_name, contact, email, address)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        student.name,
        student.dob,
        student.class_name,
        student.gender,
        student.parent_name,
        student.phone,
        student.email,
        student.address
    )

    cursor.execute(sql, values)
    db.commit()
    cursor.close()
    db.close()

    return {"status": "success"}

@router.get("/get_registrations")
def get_all():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM registrations")
    data = cursor.fetchall()
    conn.close()
    return data
