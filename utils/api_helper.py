# from api.api_client import APIClient

# def create_test_user():

#     client = APIClient("https://jsonplaceholder.typicode.com")

#     payload = {
#         "username": "testuser",
#         "password": "Password123"
#     }

#     response = client.post("/users", payload)

#     return payload


# #----------------------After implement step 9 environment and config for api

# from utils.config_reader import load_config
# from api.api_client import APIClient

# def create_test_user():

#     config = load_config()

#     client = APIClient(config["api"]["base_url"])

#     payload = {
#         "username": "testuser",
#         "password": "Password123"
#     }

#     response = client.post("/users", payload)

#     return payload


#----------------------After implement step 10 environment management---------------------


from api.api_client import APIClient
from utils.config_reader import load_config

def create_test_user():

    config = load_config()

    client = APIClient(config["api_base_url"])

    payload = {
        "username": "testuser",
        "password": "Password123"
    }

    response = client.post("/users", payload)

    return payload