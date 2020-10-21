from selene.browser import open_url, driver
from selene.core.exceptions import TimeoutException
from selene.support.conditions import not_, be
from .locators import LoginPageLocators as LPL
from .locators import MainPageLocators as MPL
from selenium.webdriver import Chrome


class BasePage():
    def __init__(self, browser, timeout=6):
        self.timeout = timeout
        self.browser = browser

    # Проверка отсутствия элемента на странице
    def shuld_be_visible(self, element):
        try:
            element.should(be.visible)
        except TimeoutException:
            return False
        return True

    def refresh_page(self):
        driver().refresh()

    # Проверка наличия элемента на странице
    def shuld_not_be_visible(self, element):
        try:
            element.should(not_.visible, timeout=6)
        except TimeoutException:
            return False
        return True

    # Открыть страницу
    def open(self, link):
        open_url(link)

    # Вход в портал
    def enter(self, user):
        # if LPL.CLEAR_LOGIN_FIELD.should(be.in_dom):
        #     LPL.CLEAR_LOGIN_FIELD.click()
        LPL.LOGIN_FIELD.type(user[0])
        # if LPL.CLEAR_PASSWORD_FIELD.should(be.visible):
        #     LPL.CLEAR_PASSWORD_FIELD.click()
        LPL.PASSWORD_FIELD.type(user[1])
        LPL.LOGIN_BUTTON.click()
        assert self.shuld_not_be_visible(LPL.LOGIN_HI), 'Вход не выполнен'

    # Выход из портала
    def logout(self):
        MPL.USER_BUTTON.click()
        MPL.LOGOUT.click()
        assert self.shuld_be_visible(LPL.LOGIN_HI), 'Выход не выполнен'
