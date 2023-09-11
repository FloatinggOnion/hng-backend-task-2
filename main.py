from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()
# Integrate database (mongodb)
# CRUD
# Add 'person' resource
# Retrieve person by 'name' query resource
# Add UML diagrams for system design and db structure
# List API endpoints
# CREATE: Adding a new person.  =>/api
# READ: Fetching details of a person.  => /api/user_id
# UPDATE: Modifying details of an existing person => /api/user_id
# DELETE: Removing a person => /api/user_id
# For dynamic parameters...type validation
# Create testing script for all CRUD operations. Probably just make a Postman collection