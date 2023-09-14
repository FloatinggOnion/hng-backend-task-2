from pydantic import BaseModel
from typing import Optional


class Person(BaseModel):
    name: str
    age: int


class UpdatePerson(BaseModel):
    name: Optional[str]
    age: Optional[int]