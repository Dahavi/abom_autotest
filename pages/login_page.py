from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    # Ввод логина
    def enter_login(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD)
        login_link.click()

    # Ввод пароля
    def enter_password(self):
        password_field = self.browser.find_element
