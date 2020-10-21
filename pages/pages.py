from .orgainzation_page import OrganizationPage
from .login_page import LoginPage
from .main_page import MainPage
from .base_page import BasePage
from selene.api import browser
from .integration_page import IntegrationPage
from .notification_page import NotificationPage
from .change_password_page import ChangePasswordPage
from .catalog_page import CatalogPage
from .incoming_order_page import IncomingOrderPage
from .incoming_orders_list import IncomingOrdersList

class Pages(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Главная страница
    def main_page(self):
        main_page = MainPage(browser)
        return main_page

    # Страница логина
    def login_page(self):
        login_page = LoginPage(browser)
        return login_page

    # Страница Настройки - Организация
    def organization_page(self):
        orgainzation_page = OrganizationPage(browser)
        return orgainzation_page

    # Страница Настройки - Интеграция
    def integration_page(self):
        integration_page = IntegrationPage(browser)
        return integration_page

    # Страница Настройки - Оповещения
    def notification_page(self):
        notification_page = NotificationPage(browser)
        return notification_page

    def change_password_page(self):
        change_password_page = ChangePasswordPage(browser)
        return change_password_page

    def catalog_page(self):
        catalog_page = CatalogPage(browser)
        return catalog_page

    def incoming_order_page(self):
        incoming_order_page = IncomingOrderPage(browser)
        return incoming_order_page

    def incoming_orders_list(self):
        incoming_orders_list = IncomingOrdersList(browser)
        return incoming_orders_list
