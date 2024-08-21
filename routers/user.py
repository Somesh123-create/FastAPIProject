from fastapi import APIRouter, Depends
from typing import List
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user

router = APIRouter(
    prefix='/user',
    tags=['user']
)

#get all users
@router.get('/all', response_model=List[UserDisplay])
def all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)

#get single user instance
@router.get('/{id}', response_model=UserDisplay)
def get_user(id:int, db: Session = Depends(get_db)):
    return db_user.get_user(db, id)


#create user instance
@router.post('/', response_model=UserDisplay)
def create_user(request:UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


#Update user instance
@router.post('/{id}/update')
def update_user(id:int, request:UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(db, id, request)


#delete user instance
@router.delete('/{id}/delete')
def delete_user(id:int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, id)
