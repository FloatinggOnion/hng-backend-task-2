# HNG Backend Stage Two Task

### About
This is a RESTFul API for displaying data from a MongoDB database. It supports URL parameters, for which the API will query the database and retrieve results. It's endpoints support GET, POST, PUT and DELETE requests on all database items.

### Endpoints


### Setup
- To setup, run `pip install requirements.txt`


### Request - Response Formats
- CREATE: Adding a new person.  =>/api
- READ: Fetching details of a person.  => /api/user_id
- UPDATE: Modifying details of an existing person => /api/user_id
- DELETE: Removing a person => /api/user_id


### Tasks
- [x] Setup FastAPI
- [x] Define schema
- [ ] Connect MongoDB
- [ ] 