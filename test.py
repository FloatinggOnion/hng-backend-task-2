from fastapi.testclient import TestClient
from main import app
import pytest


client = TestClient(app)

# Create tests
def test_create_person():
    response = client.post(
        '/api',
        json={
            'name': 'Jon Snow',
            'age': 32
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        'name': 'Jon Snow',
        'age': 32
    }


# Read tests
def test_read_people():
    response = client.get(
        '/api'
    )
    assert response.status_code == 200


def test_read_person():
    response = client.get('/api/{person_name}/', params={"person_name": "Jon Snow"})
    assert response.status_code == 200
    assert response.json() == {
        "name": "Jon Snow",
        "age": 32
    }


def test_read_inexistent_person():
    response = client.get(
        '/api/{person_name}/',
        params={"person_name": "Jon Rain"}
    )
    assert response.status_code == 404
    assert response.json() == {
        "detail": 
        {
            "error": "An error occurred",
            "code": 404,
            "message": "Person doesn't exist"
        }
    }


# Update tests
def test_update_person():
    response = client.put(
        '/api/Jon Snow/',
        params={"person_name": "Jon Snow"},
        json={
            "name": "Jon Bellion",
            "age": 44
        }
    )
    assert response.status_code == 200


# Delete tests
def test_delete_person():
    response = client.delete(
        '/api/Jon Bellion/',
        params={"person_name": "Jon Bellion"},
    )
    assert response.status_code == 200
    assert response.json() == "Record of Jon Bellion has been removed"