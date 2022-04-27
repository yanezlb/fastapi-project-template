from typing import Optional
from sqlmodel import SQLModel, Field

class UserBase(SQLModel):
    username: str = Field(index=True)
    password: str

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserRead(UserBase):
    id: int
    pass