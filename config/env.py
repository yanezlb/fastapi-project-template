import os
from tokenize import String
import databases
from starlette.config import Config

config = Config("../.env")

DATABASE_URL = config("DATABASE_URL", cast=databases.DatabaseURL)
VERSION = config("VERSION", cast=str, default="0.0.1")
TITLE =  config("TITLE", cast=str, default="template")
ROOT_DIR = config("ROOT_DIR", cast=str, default="/api/v1")