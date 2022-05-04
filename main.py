import os, sys, databases

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users)