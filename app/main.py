from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app import models, schemas, auth
from app.database import engine, get_db
from app.schemas import ApplicationResponse
from app.auth import verify_password, create_access_token, verify_token

from typing import List
from pydantic import BaseModel

app = FastAPI() 

models.Base.metadata.create_all(bind=engine)

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    payload = verify_token(token)

    return payload["user_id"]

@app.get("/")
def root():
    return {"message" : "Internship Tracker API is running"}

@app.get("/applications", response_model=List[ApplicationResponse])
def get_applications(status: str | None = None, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    query = db.query(models.Application).filter(models.Application.user_id == current_user["user_id"])

    if status:
        query = query.filter(models.Application.status == status)

    return query.all()

@app.post("/applications", response_model=ApplicationResponse)
def create_application(app_data: schemas.ApplicationCreate,db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    new_app = models.Application(**app_data.dict(), user_id=user_id)
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    return new_app

@app.get("/applications/{id}", response_model=schemas.ApplicationResponse)
def get_application(id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    app_entry = db.query(models.Application).filter(models.Application.id == id, models.Application.user_id == current_user["user_id"]).first()

    if not app_entry:
        raise HTTPException(status_code=404, detail="Application not found")
    
    return app_entry

@app.put("/applications/{id}", response_model=schemas.ApplicationResponse)
def update_application(id: int, updated_data: schemas.ApplicationUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    app_entry = db.query(models.Application).filter(models.Application.id == id, models.Application.user_id == current_user["user_id"]).first()

    if not app_entry:
        raise HTTPException(status_code=404, detail="Application not found")
    
    if updated_data.company is not None:
        app_entry.company = updated_data.company
    if updated_data.position is not None:
        app_entry.position = updated_data.position
    if updated_data.status is not None:
        app_entry.status = updated_data.status

    db.commit()
    db.refresh(app_entry)

    return app_entry

@app.delete("/applications/{id}")
def delete_application(id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    app_entry = db.query(models.Application).filter(models.Application.id == id, models.Application.user_id == current_user["user_id"]).first()

    if not app_entry:
        raise HTTPException(status_code=404, detail="Application not found")
    
    db.delete(app_entry)
    db.commit()

    return {"message": "Application deleted successfully"}

@app.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_pw = auth.hash_password(user.password)

    new_user = models.User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    
    token = create_access_token({"user_id": db_user.id})

    return{
        "access_token": token,
        "token_type": "bearer"
    }
