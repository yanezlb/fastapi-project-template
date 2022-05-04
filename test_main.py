from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine

from main import app
from config.database import get_session
from config.env import DATABASE_URL

# TODO: add more functions to test other endpoints

def test_create_user():
        client = TestClient(app)  # 

        response = client.get(  # 
            "/api/v1/users"
        )

        data = response.json()  # 

        assert response.status_code == 200  # 
        
        
# def test_create_user():

#     client = TestClient(app)

#     response = client.get(
#         "/api/v1/user/test"
#     )

#     assert response.status_code == 200
