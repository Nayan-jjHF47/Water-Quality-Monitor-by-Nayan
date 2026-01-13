from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, Session, create_engine, select
from models import User
import jwt
from pydantic import BaseModel

app = FastAPI()

DATABASE_URL = "mysql+mysqlconnector://root:Nayan%40123@localhost/fastapi_db"
engine = create_engine(DATABASE_URL, echo=True)

# Create tables
SQLModel.metadata.create_all(engine)

SECRET_KEY = "JdHcLJgiX52GQ_-60xoTvBUsLR55lN-qH-MdSwQRLtU"
ALGORITHM = "HS256"

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

@app.post("/register")
def register(user: UserCreate):
    with Session(engine) as session:
        db_user = session.exec(select(User).where(User.username == user.username)).first()
        if db_user:
            raise HTTPException(status_code=400, detail="Username already exists")
        new_user = User(username=user.username, email=user.email, password=user.password)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return {"id": new_user.id, "username": new_user.username, "email": new_user.email}

@app.post("/login")
def login(user: UserLogin):
    with Session(engine) as session:
        db_user = session.exec(select(User).where(User.username == user.username)).first()
        if not db_user or db_user.password != user.password:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        token_data = {"sub": db_user.username, "id": db_user.id}
        token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token}

@app.post("/profile")
def profile(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        with Session(engine) as session:
            db_user = session.exec(select(User).where(User.username == username)).first()
            if not db_user:
                raise HTTPException(status_code=404, detail="User not found")
            return {"id": db_user.id, "username": db_user.username, "email": db_user.email}
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
