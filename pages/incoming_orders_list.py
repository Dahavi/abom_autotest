from .base_page import BasePage
from .locators import IncomingOrdersListLocators as IOL


class IncomingOrdersList(BasePage):

    def open_first_order(self):
        IOL.FIRST_ORDER.click()
        assert self.shuld_be_visible(IOL.ORDER_EDIT), 'Заказ не открылся'