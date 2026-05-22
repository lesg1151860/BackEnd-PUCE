from enum import Enum
from typing import Optional
from sqlmodel import SQLModel, Field


class Role(str, Enum):
    admin = "admin"
    lider = "lider"


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    email: str = Field(index=True)
    hashed_password: str
    role: Role = Field(sa_column_kwargs={"default": Role.lider})
