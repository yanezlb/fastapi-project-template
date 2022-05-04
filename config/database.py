import os, sys, databases
from dotenv import load_dotenv
from starlette.config import Config

from sqlmodel import Field, Session, SQLModel, create_engine, select


BASE_DIR = "/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1])
load_dotenv(os.path.join(BASE_DIR, ".env"))
sys.path.append(BASE_DIR)

engine = create_engine(os.environ["DATABASE_URL"], echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)