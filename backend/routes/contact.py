from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from database import get_db


router = APIRouter(prefix="/contact", tags=["Contact"])

class Contact(BaseModel):
    name: str
    email: str
    phone: int
    message: str

@router.post("/")
def send_message(contact: Contact):
    try:
        db = get_db()
        cursor = db.cursor()
        query = """
            INSERT INTO queries (name, email, phone, message)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (contact.name, contact.email, contact.phone, contact.message))
        db.commit()
        cursor.close()
        db.close()
        return {"message": "Contact message sent successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
