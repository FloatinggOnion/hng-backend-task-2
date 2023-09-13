from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# Create tests
def test_create_person():
    response = client.post(
        '/api',
        json={
            'first_name': 'James',
            'last_name': 'Bond',
            'email': 'jamesbond@fight.com',
            'age': 32
        }
    )
    assert response.status_code == 200
    # assert response.json() == {
    #     'first_name': 'James',
    #     'last_name': 'Bond',
    #     'email': 'jamesbond@fight.com',
    #     'age': 32
    # }


# Read tests
def test_read_people():
    response = client.get(
        '/api'
    )
    assert response.status_code == 200
    

def test_read_person():
    response = client.get('/api/James')
    assert response.status_code == 200
    # assert response.json() == {
    #     #"id": "65019c95dde3e2bb83d8e8c3", 
    #     "first_name": "John", 
    #     "name": "Doe", 
    #     "email": "johndoe@gmail.com",
    #     "age": 32
    # }


def test_read_inexistent_person():
    response = client.get(
        '/100'
    )
    assert response.status_code == 404
    # assert response.json() == {
    #     "error": "An error occurred",
    #     "code": 404,
    #     "message": "Person doesn't exist"
    # }


# Update tests
def test_update_person():
    response = client.put(
        '/api/James',
        json={
            'first_name': 'John',
            'last_name': 'Allen',
            'email': 'johnallen@gmail.com',
            'age': 32,
        }
    )
    assert response.status_code == 200
    # assert response.json() == {
    #     "data": "Person with name update is successful",
    #     "message": "Person name updated successfully"
    # }


# Delete tests
def test_delete_person():
    response = client.delete(
        '/api/James'
    )
    assert response.status_code == 200
    # assert response.json() == {
    #     "data": "Person removed",
    #     "message": "Person deleted successfully"
    # }