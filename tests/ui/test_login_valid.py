from pages.login_page import LoginPage
from utils.logger import get_logger

logger = get_logger(__name__)


def test_login_success(page):

    logger.info("Starting valid login test")

    login = LoginPage(page)

    login.login("student", "Password123")

    page.wait_for_load_state("networkidle")

    assert login.is_login_successful()