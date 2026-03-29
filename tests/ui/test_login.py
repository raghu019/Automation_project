


# from pages.login_page import LoginPage

# def test_login_success(page):

#     page.goto("https://practicetestautomation.com/practice-test-login/")

#     login=LoginPage(page)     

#     login.login("student","Password123")

#     assert login.is_login_successful()


    
# #invalid test case to check the error message when the user enters invalid credentials

# def test_invalid_login(page):

#     page.goto("https://practicetestautomation.com/practice-test-login/")

#     login=LoginPage(page) #here login is the object of the LoginPage class which we have created in the pages/login_page.py file and we are passing the page fixture as an argument to the LoginPage class constructor which will be used to perform the actions on the login page

#     login.login("student","12345")

#     assert login.error_message() == "Your password is invalid!"



#Use Config in TESt for valid login

# from pages.login_page import LoginPage
# from utils.config_reader import load_config

# config = load_config()

# def test_login_success(page):

#     # page.goto(config["base_url"])  removing this hence we have move this to the fixture in conftest.py file so that it will be executed before every test case and we don't have to write this line in every test case

#     login = LoginPage(page)

#     login.login(
#         config["credentials"]["username"],
#         config["credentials"]["password"]
#     )

#     assert login.is_login_successful()




# #Use Config in TESt for in-valid login


# def test_invalid_login(page):

#     # page.goto(config["base_url"])  removing this hence we have move this to the fixture in conftest.py file so that it will be executed before every test case and we don't have to write this line in every test case

#     login = LoginPage(page)

#     login.login(
#         config["invalid_credentials"]["username"],
#         config["invalid_credentials"]["password"]
#     )

#     assert login.error_message() == "Your password is invalid!"




# #  USing Data driven Testing 

# import pytest
# from pages.login_page import LoginPage
# from utils.config_reader import load_config

# @pytest.mark.parametrize("username,password,expected_message",
                         
# [
#     ("student","wrong1","Your password is invalid!"),
#     ("Raghu","Password123","Your username is invalid!"),
#     (" "," ","Your username is invalid!")
# ])

# def test_invalid_login(page, username, password, expected_message):

#      # page.goto(config["base_url"])  removing this hence we have move this to the fixture in conftest.py file so that it will be executed before every test case and we don't have to write this line in every test case

#      login=LoginPage(page)

#      login.login(username, password)

#      actual_error=login.get_error_message() #this will return the error message text which we can use in our test case to assert the error message

#      assert actual_error == expected_message #this will compare the actual error message with the expected error message and if they are equal then the test case will pass otherwise it will fail




# #----------After implementing API on current project-----------------

# from utils.api_helper import create_test_user
# from pages.login_page import LoginPage

# import pytest

# @pytest.mark.xfail(reason="Dummy API does not create real users")
# def test_login_with_api_user(page):

#     user = create_test_user()

#     login = LoginPage(page)

#     login.login(user["username"], user["password"])

#     assert login.is_login_successful()






#------------------After implementing Step 11: Logger in the current project-----------------
import pytest
from pages.login_page import LoginPage
from utils.config_reader import load_config
from utils.api_helper import create_test_user
from utils.logger import get_logger

logger = get_logger(__name__)


# @pytest.mark.parametrize("username,password,expected_message",
# [
#     ("student","wrong1","Your password is invalid!"),
#     ("Raghu","Password123","Your username is invalid!"),
#     (" "," ","Your username is invalid!")
# ])
# def test_invalid_login(page, username, password, expected_message):

#     logger.info("Starting invalid login test")

#     login = LoginPage(page)

#     login.login(username, password)

#     actual_error = login.get_error_message()

#     logger.info(f"Actual error message: {actual_error}")

#     assert actual_error == expected_message


# def test_login_success(page):

#     logger.info("Starting valid login test")

#     config = load_config()

#     login = LoginPage(page)

#     login.login(config["username"], config["password"])

#     logger.info("Checking login success")

#     assert login.is_login_successful()


# @pytest.mark.xfail(reason="Dummy API does not create real users")
# def test_login_with_api_user(page):

#     logger.info("Starting API + UI integration test")

#     user = create_test_user()

#     login = LoginPage(page)

#     login.login(user["username"], user["password"])

#     logger.info("Checking login success for API user")

#     assert login.is_login_successful()






#--------------------after implementing step 13 :Advance test data management---------------
import pytest
from pages.login_page import LoginPage
from utils.data_reader import load_test_data
from utils.logger import get_logger

logger = get_logger(__name__)

data = load_test_data()["login_data"]


@pytest.mark.parametrize("test_data", data)
def test_invalid_login(page, test_data):

    logger.info("Starting invalid login test")

    login = LoginPage(page)

    login.login(test_data["username"], test_data["password"])

    actual_error = login.get_error_message()

    logger.info(f"Actual error: {actual_error}")

    assert actual_error == test_data["expected"]