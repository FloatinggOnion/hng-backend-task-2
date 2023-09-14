# HNG Backend Stage Two Task

### About
This is a RESTFul API for displaying data from an SQLite database. It supports URL parameters, for which the API will query the database and retrieve results. It's endpoints support GET, POST, PUT and DELETE requests on all database items.

### Database
- I interfaced with the SQLite database using the [SQLAlchemy](https://www.sqlalchemy.org/) package

### Endpoints
- POST (Create) `localhost:port/api/`: Add a new person to the database
- GET (Read) `localhost:port/api/{person_name}`: Fetching the details of a person
- PUT (Update) `localhost:port/api/{person_name}`: Modifying the details of an existing person
- DELETE `localhost:port/api/{person_name}`: Removing a person

### Setup
- To setup, run `pip install requirements.txt`


### Request - Response Formats
**NOTE**: `person_name` is the user's `name`
- CREATE: Adding a new person.  =>/api
  - Below is an example of the payload that is expected
  - ```json
    {
    "name": "John Doe",
    "age": 32,
    }
    ```
- READ: Fetching details of all people in database.  => /api
- READ: Fetching details of a person.  => /api/person_name
- UPDATE: Modifying details of an existing person => /api/person_name
- DELETE: Removing a person => /api/person_name


### Tasks
- [x] Setup FastAPI
- [x] Define schema
- [x] Integrate database (sqlalchemy)
- [x] CRUD
- [x] Add 'person' resource
- [x] Retrieve person by 'name' query resource
- [ ] Add UML diagrams for system design and db structure
- [x] List API endpoints in Readme
- [x] For dynamic parameters...type validation
- [x] Create testing script for all CRUD operations. 
- [x] Create requirements file