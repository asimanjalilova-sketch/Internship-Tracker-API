from pydantic import BaseModel

class ApplicationCreate(BaseModel):
    company: str
    position: str
    status: str = "Applied"

class ApplicationResponse(ApplicationCreate):
    id: int

    class Config:
        from_attributes = True

class ApplicationUpdate(BaseModel):
    company: str | None = None
    position: str | None = None
    status: str | None = None

class UserCreate(BaseModel):
    email: str
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    username: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: str
    password: str