# Using Pydantic. This is a Python library used to perofrm data validation. We can declared the shape of our data as classes with attributes
from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum

class Gender(str, Enum):
    male = 'male'
    female = 'female'

class Role:
    admin = 'admin'
    user = 'user'
    student = 'student'

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    middle_name: Optional[str]
    last_name: str
    email: Optional[str]
    gender: Gender
    #roles: Optional[List[Role]]

    class Config:
        arbitrary_types_allowed = True

class UserUpdateRequest(BaseModel):
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]