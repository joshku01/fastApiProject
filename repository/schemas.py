from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


# 新增User定義地方
class UserCreate(UserBase):
    password: str
    is_active: bool


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
