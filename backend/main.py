from fastapi import FastAPI
from routes import register, contact
from database import get_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Bajrang School API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(register.router)
app.include_router(contact.router)

@app.get("/")
def home():
    return {"status": "School Backend Running"}
