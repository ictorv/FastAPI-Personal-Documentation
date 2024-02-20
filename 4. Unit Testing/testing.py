from fastapi.testclient import TestClient
from fastapi import status
from main import app

client=TestClient(app=app)


"""Testing get request"""
def test1():
    response=client.get('/get_info')
    assert response.status_code==status.HTTP_200_OK
    assert response.json()=={"message": "Hello World"}


"""Testing post request"""
def test2():
    test_data={"name":"Victor","cls":"12","roll":12}
    response =client.post('/post_info',json=test_data)
    assert response.status_code==status.HTTP_200_OK
    assert response.json()==test_data