# from api.api_client import APIClient

# def test_get_users():

#     client = APIClient("https://jsonplaceholder.typicode.com") #we are creating an object of the APIClient class and passing

#     response = client.get("/users") 

#     assert response.status_code == 200

#     data = response.json()

#     assert len(data) > 0



# --------------After implement step 9 environment and config for api----------------------


# from api.api_client import APIClient
# from utils.config_reader import load_config

# def test_get_users():

#     config = load_config()

#     client = APIClient(config["api"]["base_url"])  #we are creating an object of the APIClient class and passing the base URL from the config file

#     response = client.get("/users")

#     assert response.status_code == 200

    
#     data = response.json()

#     assert len(data) > 0

#     print(response.json())



#----------------------After implement step 10 environment management----------------------

from api.api_client import APIClient
from utils.config_reader import load_config

def test_get_users():

    config = load_config()

    client = APIClient(config["api_base_url"]) #we are creating an object of the APIClient class and passing the base URL from the config file

    response = client.get("/users")

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0