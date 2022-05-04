import os, sys, databases

from fastapi import FastAPI
from starlette.config import Config
from config.database import create_db_and_tables
from config.env import VERSION, TITLE, ROOT_DIR
from routes.user import users

app = FastAPI(
    title=TITLE,
    version=VERSION,
    description="This is a project template with FastAPI + Docker compose + SQLModel + Postgres",
    docs_url=f"{ROOT_DIR}/docs"
    )

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(users)