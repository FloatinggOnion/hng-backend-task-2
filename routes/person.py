from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder


from database import add_person, delete_person, retrieve_people, retrieve_person, update_person

from models.person import error_response_model, response_model, PersonSchema, UpdatePersonModel



router = APIRouter()


# Create
@router.post('/', response_description='Person data added into the database')
async def add_person_data(person: PersonSchema = Body(...)):
    person = jsonable_encoder(person)
    new_person = await add_person(person)
    return response_model(new_person, 'Person added successfully.')


# Read 
@router.get('/', response_description='People retrieved')
async def get_people():
    people = await retrieve_people()
    if people:
        return response_model(people, 'People data retrieved successfully')
    return response_model(people, 'No people in database')

@router.get('/{user_id}', response_description='Person retrieved')
async def get_person(user_id):
    person = await retrieve_person(id=user_id)
    if person:
        return response_model(person, 'Person data retrieved successfully')
    return error_response_model('An error occurred', 404, 'Person doesn\'t exist')


# Update
@router.put('/{user_id}', response_description='Update person\'s data')
async def update_person(user_id: str, req: UpdatePersonModel = Body(...)):
    # print(req)
    print(type(req))
    # print(dict(list(req)))
    req = {k: v for k, v in req.values() if v is not None}
    updated_person = await update_person(user_id, req)
    if updated_person:
        return response_model(
            f'Person with ID: {user_id} name update is successful', 
            'Person name updated successfully',
        )
    return error_response_model(
        'An error occurred',
        404,
        'There was an error updating person data',
    )


# Delete
@router.delete('/{user_id}', response_description='Delete person data')
async def delete_person(user_id: str):
    deleted_person = await delete_person(user_id)
    if deleted_person:
        return response_model(
            f'Person with ID: {user_id} removed',
            'Person deleted successfully'
        )
    return error_response_model(
        'An error occurred',
        404,
        f'Student with id {user_id} doesn\'t exist'
    )