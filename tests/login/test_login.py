def test_user_login(user_login_fixture):
    login_page = user_login_fixture
    login_page.enter_username("qa.ajax.app.automation@gmail.com")
    login_page.enter_password("qa_automation_password")
    login_page.click_login_button()
    assert login_page.is_element_present("com.ajaxsystems:id/homePageElement")


def test_invalid_user_login(user_login_fixture):
    login_page = user_login_fixture
    login_page.enter_username("incorrect_username")
    login_page.enter_password("incorrect_password")
    login_page.click_login_button()
    error_message = login_page.get_error_message()
    assert "error" in error_message.lower()
