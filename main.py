from fastapi import FastAPI, APIRouter, Depends, HTTPException
from schemas import Person, UpdatePerson
import models
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session

#This will create our database if it doesen't already exists
Base.metadata.create_all(engine)
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


description = """
This API helps you to perform CRUD operations on a Person object. 🚀

## People

You will be able to:

* **Create people**.
* **Read people**.
* **Update people**
* **Delete people**

The link to this repository is https://github.com/FloatinggOnion/hng-backend-task-2/
"""


app = FastAPI(
    title="HNG Stage 2 Task",
    description=description,
    version="0.0.1",
    contact={
        "name": "Jesse-Paul Osemeke",
        "url": "https://github.com/FloatinggOnion",
        "email": "jesseosems123@gmail.com.com",
    },
)
prefix_router = APIRouter()

def get_user_by_identifier(identifier):
    db = SessionLocal()
    user = None
    if isinstance(identifier, int):
        user = db.query(models.Person).filter(models.Person.id == identifier).first()
    elif isinstance(identifier, str):
        user = db.query(models.Person).filter(models.Person.name == identifier).first()
    db.close()
    return user

# Create
@prefix_router.post("/")
async def create_person(data: Person, session = Depends(get_session)):
    person = models.Person(name = data.name, age = data.age)
    session.add(person)
    session.commit()
    session.refresh(person)

    return person


# Read
@prefix_router.get("/")
async def root(session: Session = Depends(get_session)):
    people = session.query(models.Person).all()
    
    return people

@prefix_router.get("/{identifier}")
async def read_person(person_name: str, session: Session = Depends(get_session)):
    person = session.query(models.Person).get(person_name)

    if person is None:
        raise HTTPException(
            status_code=404,
            detail={
                "error": "An error occurred",
                "code": 404,
                "message": "Person doesn't exist"
            }
        )
    
    return person
# async def read_person(identifier: str | int, session: Session = Depends(get_session)):
#     if type(identifier) == str:
#         person = get_user_by_identifier(identifier)
#     else:
#         person = session.query(models.Person).get(identifier)
#     return person


# Update
@prefix_router.put('/{person_name}')
async def update_person(person_name: str, data: Person, session = Depends(get_session)):
    person_obj = session.query(models.Person).get(person_name)
    person_obj.name = data.name
    person_obj.age = data.age
    session.commit()

    return person_obj
    


# Delete
@prefix_router.delete('/{person_name}')
async def delete_person(person_name: str, session = Depends(get_session)):
    person_obj = session.query(models.Person).get(person_name)
    session.delete(person_obj)
    session.commit()
    session.close()

    return f'Record of {person_name} has been removed'


# Setting router prefix to "/api/"
app.include_router(prefix_router, prefix='/api')
