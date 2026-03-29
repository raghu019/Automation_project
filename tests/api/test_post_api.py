# from api.api_client import APIClient

# def test_create_post():

#     client = APIClient("https://jsonplaceholder.typicode.com")

#     payload = {
#         "title": "Test Title",
#         "body": "Test Body",
#         "userId": 1
#     }

#     response = client.post("/posts", payload)

#     print(response.json())   # 👈 ADD THIS

#     assert response.status_code == 201

#     data = response.json()

#     assert data["title"] == "Test Title"





#----------------------After implement step 9 environment and config for api----------------------


from api.api_client import APIClient
from utils.config_reader import load_config

def test_create_post():

    config = load_config()

    client = APIClient(config["api"]["base_url"])

    payload = {
        "title": "Test Title",
        "body": "Test Body",
        "userId": 1
    }

    response = client.post("/posts", payload)

    print(response.json())   # 👈 ADD THIS

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Test Title"




#----------------------After implement step 10 environment management----------------------


from api.api_client import APIClient
from utils.config_reader import load_config

def test_create_post():

    config = load_config()

    client = APIClient(config["api_base_url"])

    payload = {
        "title": "Test Title",
        "body": "Test Body",
        "userId": 1
    }

    response = client.post("/posts", payload)

    print(response.json())

    assert response.status_code == 201

    data = response.json()

    assert "title" in data