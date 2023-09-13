# HNG Backend Stage Two Task

### About
This is a RESTFul API for displaying data from a MongoDB database. It supports URL parameters, for which the API will query the database and retrieve results. It's endpoints support GET, POST, PUT and DELETE requests on all database items.

### Endpoints
- POST (Create) `localhost:port/api/`: Add a new person to the database
- GET (Read) `localhost:port/api/user_id`: Fetching the details of a person
- PUT (Update) `localhost:port/api/user_id`: Modifying the details of an existing person
- DELETE `localhost:port/api/user_id`: Removing a person

### Setup
- To setup, run `pip install requirements.txt`


### Request - Response Formats
- CREATE: Adding a new person.  =>/api
  - Below is an example of the payload that is expected
  - ```json
    {
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com",
    "age": 32,
    }
    ```
- READ: Fetching details of all people in database.  => /api
- READ: Fetching details of a person.  => /api/user_id
- UPDATE: Modifying details of an existing person => /api/user_id
- DELETE: Removing a person => /api/user_id


### Tasks
- [x] Setup FastAPI
- [x] Define schema
- [x] Integrate database (mongodb)
- [x] CRUD
- [x] Add 'person' resource
- [ ] Retrieve person by 'name' query resource
- [ ] Add UML diagrams for system design and db structure
- [x] List API endpoints in Readme
- [x] For dynamic parameters...type validation
- [x] Create testing script for all CRUD operations. 