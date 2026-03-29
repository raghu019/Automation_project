# import pytest
# from playwright.sync_api import sync_playwright   # it will import required tools

# @pytest.fixture   # it is reusable code which can be used in multiple test cases
# def page():
#     with sync_playwright() as p:     # Starts Playwright engine

#         browser = p.chromium.launch(headless=False)  # it will launch the browser in non-headless mode, you can change it to True if you want to run in headless mode
#         page = browser.new_page() # it will create a new page in the browser
#         yield page              # it will execute the test case and after that it will close the browser
#         browser.close()





# #--------------------After implemneting step -7 cleaen frame work and utilities conftest.py file looke like below------------------

# import pytest
# from playwright.sync_api import sync_playwright   # it will import required tools
# from utils.config_reader import load_config


# @pytest.fixture(scope="function")   # it is reusable code which can be used in multiple test cases
# def page():
#     config=load_config()   # it will load the config file and return the config data as a dictionary which we can use in our test cases to get the base url and credentials

#     with sync_playwright() as p:     # Starts Playwright engine

#         browser = p.chromium.launch(headless=False)  # it will launch the browser in non-headless mode, you can change it to True if you want to run in headless mode

#         context=browser.new_context() # it will create new browser window with new context, so that we can run multiple test cases in parallel without any interference between them

#         page = browser.new_page() # it will create a new page in the browser

#         #comon step moved here
#         page.goto(config["base_url"])

#         yield page              # it will execute the test case and after that it will close the browser
#         browser.close()







# #----------------------------after implementing step 11: Logger and screenshots----------------------------

import pytest
import os
from playwright.sync_api import sync_playwright
from utils.config_reader import load_config


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    config = load_config()

    context = browser.new_context()
    page = context.new_page()

    page.goto(config["base_url"])

    yield page

    page.close()
    context.close()





# Screenshot saved + attached to report  with implementation of STEP 12: Advance report

import pytest
import os
from pytest_html import extras


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        page = item.funcargs.get("page", None)

        if report.failed and page:

            os.makedirs("reports/screenshots", exist_ok=True)

            file_name = f"screenshots/{item.name}.png"
            full_path = os.path.join("reports", file_name)

            page.screenshot(path=full_path)

            if hasattr(report, "extra"):
                report.extra.append(extras.image(file_name))
            else:
                report.extra = [extras.image(file_name)]