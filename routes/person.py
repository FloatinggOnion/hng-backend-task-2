from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder


from database import add_person, delete_person, retrieve_people, retrieve_person, update_person

from models.person import error_response_model, response_model, PersonSchema, UpdatePersonModel



router = APIRouter()