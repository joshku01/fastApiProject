from sqlalchemy.orm import Session
from . import models, schemas


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


# get_user 取特定使用者資料
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "qwer1234"
    db_user = models.User(email=user.email, is_active=user.is_active, hashed_password=fake_hashed_password)
    db.add(db_user)  # 添加到會話
    db.commit()  # 提交到資料庫
    db.refresh(db_user)  # 刷新資料庫
    return db_user


def delete_user(db: Session, user_id: int):
    return db.query(models.User).filter_by(id=user_id).delete()
