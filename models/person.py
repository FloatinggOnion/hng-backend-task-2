from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class PersonSchema(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)
    age: int = Field(...)

    class Config:
        schema_extra = {
            'example': {
                'first_name': 'John',
                'last_name': 'Doe',
                'email': 'johndoe@example.com',
                'age': 32,
            }
        }


class UpdatePersonModel(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    age: Optional[int]

    class Config:
        schema_extra = {
            'example': {
                'first_name': 'Jane',
                'last_name': 'Deer',
                'email': 'janedeer@example.com',
                'age': 26,
            }
        }


def response_model(data, message):
    return {
        'data': [data],
        'code': 200,
        'message': message,
    }


def error_response_model(error, code, message):
    return {
        'error': error,
        'code': code,
        'message': message,
    }