from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import uuid
from datetime import datetime
from database import SessionLocal, UserData
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Database Session Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for user data
class UserDataModel(BaseModel):
    ip: str
    lat: float = None
    lng: float = None
    user_agent: str
    referrer: str
    first_name: str
    last_name: str
    education: str
    university: str
    country: str
    province: str
    city: str
    phone_number: str
    email: str


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, can be restricted to specific domain
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# HTML Page Serve Karne ka Endpoint
@app.get("/", response_class=HTMLResponse)
async def track_location(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# User Data Save Karne ka Endpoint
@app.post("/save-data")
async def save_data(data: UserDataModel, db: Session = Depends(get_db)):
    try:
        print("Received Data:", data.dict())  # Debugging ke liye print
        
        # Database Entry Banayein
        user_data = UserData(
            id=str(uuid.uuid4()),
            ip_address=data.ip,
            latitude=data.lat,
            longitude=data.lng,
            user_agent=data.user_agent,
            referrer=data.referrer,
            first_name=data.first_name,
            last_name=data.last_name,
            education=data.education,
            university=data.university,
            country=data.country,
            province=data.province,
            city=data.city,
            phone_number=data.phone_number,
            email=data.email,
            timestamp=datetime.now()
        )

        print("Saving to Database...")  # Debug message
        db.add(user_data)
        db.commit()
        print("Data Saved Successfully!")  # Success message
        
        return {"status": "success"}
    
    except Exception as e:
        print(f"Error: {e}")  # Print error log
        raise HTTPException(status_code=500, detail=str(e))
