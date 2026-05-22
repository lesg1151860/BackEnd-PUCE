from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Optional


class RoleEnum(str, Enum):
    admin = "admin"
    lider = "lider"


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: RoleEnum


class UserRead(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role: RoleEnum
