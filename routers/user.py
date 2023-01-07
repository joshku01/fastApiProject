from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from repository import database, schemas, crud

router = APIRouter()


# start db connection
def get_db_session():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 取得DB所有使用者
@router.get("/users/", response_model=list[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


# 取得指定user by ID
@router.get("/user/{user_id}", response_model=schemas.User)
async def get_user(user_id: int, db: Session = Depends(get_db_session)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    return user


@router.delete("/user/{user_id}", response_model=schemas.User)
async def delete_user(user_id: int, db: Session = Depends(get_db_session)):
    user = crud.delete_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    return user


# 新增使用者
@router.post("/users", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db_session)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)
