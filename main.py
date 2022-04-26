import sys
import os, sys
from dotenv import load_dotenv, dotenv_values
from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import FastAPI

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))
sys.path.append(BASE_DIR)

class UserBase(SQLModel):
    username: str = Field(index=True)
    password: str

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class UserCreate(UserBase):
    pass

connect_args = {"check_same_thread": False}
engine = create_engine(os.environ["DATABASE_URL"], echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@app.on_event("startup")
def on_startup():
    print("hola")
    create_db_and_tables()

@app.get("/")
async def root():
    print(os.environ["DATABASE_URL"])
    return {"root": "hello"}