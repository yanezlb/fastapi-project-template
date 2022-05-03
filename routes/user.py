from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from config.database import get_session
from models.user import User, UserBase, UserCreate, UserRead, UserUpdate
from config.env import VERSION, TITLE, ROOT_DIR

users = APIRouter()

@users.post(f"{ROOT_DIR}/users", response_model=UserRead, tags=["Admin User"])
async def create_user(*, session: Session = Depends(get_session), user: UserCreate):
    db_user = User.from_orm(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@users.get(f"{ROOT_DIR}/users", response_model=List[UserRead], tags=["Admin User"])
def list_users(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    heroes = session.exec(select(User).offset(offset).limit(limit)).all()
    return heroes


@users.patch(ROOT_DIR+"/users/{user_id}", response_model=UserRead, tags=["Admin User"])
def update_user(
    *, session: Session = Depends(get_session), user_id: int, user: UserUpdate
):
    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Hero not found")
    user_data = user.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@users.delete(ROOT_DIR+"/users/{user_id}", tags=["Admin User"])
def delete_user(*, session: Session = Depends(get_session), user_id: int):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"ok": True}

@users.get(ROOT_DIR+"/user/test", tags=["Admin User"])
def delete_user():
    return {"ok": True}