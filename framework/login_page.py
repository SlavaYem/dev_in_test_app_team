from .page import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):
    USERNAME_FIELD = (By.ID, 'com.ajaxsystems:id/usernameField')
    PASSWORD_FIELD = (By.ID, 'com.ajaxsystems:id/passwordField')
    LOGIN_BUTTON = (By.ID, 'com.ajaxsystems:id/loginButton')
    ERROR_MESSAGE = (By.ID, 'com.ajaxsystems:id/errorMessage')

    def enter_username(self, username):
        self.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.find_element(*self.ERROR_MESSAGE).text
