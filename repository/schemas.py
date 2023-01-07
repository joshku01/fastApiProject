from pydantic import BaseModel
from typing import Union


class UserBase(BaseModel):
    email: str


# 新增User定義地方
class UserCreate(UserBase):
    password: str
    is_active: Union[bool, None]


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
