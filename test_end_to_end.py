import requests
import json

def test_list_users():
    BASE_URL = "https://reqres.in"
    EXT = "/api/users?page=2"
    URL = BASE_URL + EXT

    response = requests.get(URL)
    print(response.status_code)
    assert response.status_code == 200
    resp = response.json()
    total = resp['total']
    print(total)
    assert total == 12

    print("\n")

def test_create_update_delete():
    BASE_URL = "https://reqres.in"
    EXT = "/api/users"
    URL = BASE_URL + EXT

    data = {
        "name": "Jerry",
        "job": "Testing",
        "movie": "Tokyo Drift"
    }

    response = requests.post(URL, data=data)
    resp = response.json()
    id = '/' + resp['id']
    movie = resp["movie"]
    print(response.status_code)
    assert response.status_code == 201
    print(response.json())
    assert movie == "Tokyo Drift"

    data = {
        "name": "Jerry Tom",
        "job": "QA Testing",
        "movie": "Avengers: Endgame"
    }

    response = requests.put(URL + id, data=data)
    print(response.status_code)
    assert response.status_code == 200
    print(response.json())

    response = requests.delete(URL + id)
    print(response.status_code)
    assert response.status_code == 204

    print("\n")

def test_register_login_():
    BASE_URL = "https://reqres.in"
    EXT = "/api/register"
    URL = BASE_URL + EXT

    data = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
    }

    response = requests.post(URL, data=data)
    print(response.status_code)
    assert response.status_code == 200
    print(response.json())


    EXT = "/api/login"
    URL = BASE_URL + EXT

    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    response = requests.post(URL, data=data)
    print(response.status_code)
    assert response.status_code == 200
    print(response.json())

    print("\n")

def test_unsuccessful_register_login():
    BASE_URL = "https://reqres.in"
    EXT = "/api/register"
    URL = BASE_URL + EXT

    data = {
        "email": "eve.holt@reqres.in"
    }

    response = requests.post(URL, data=data)
    print(response.status_code)
    assert response.status_code == 400
    resp = response.json()
    error = resp['error']
    print(error)
    assert error == "Missing password"


    EXT = "/api/login"
    URL = BASE_URL + EXT

    data = {
        "email": "eve.holt@reqres.in"
    }

    response = requests.post(URL, data=data)
    print(response.status_code)
    assert response.status_code == 400
    resp = response.json()
    error = resp['error']
    print(error)
    assert error == "Missing password"

    print("\n")

test_list_users()
test_create_update_delete()
test_register_login_()
test_unsuccessful_register_login()

