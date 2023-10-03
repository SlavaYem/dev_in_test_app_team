import pytest

from framework.login_page import LoginPage


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    login_page = LoginPage(driver)
    yield login_page
