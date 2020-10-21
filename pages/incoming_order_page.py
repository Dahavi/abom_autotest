import random
import datetime

from selene.support.conditions import be
from selene.support.shared.jquery_style import s
from selenium.common.exceptions import NoSuchElementException

from .base_page import BasePage
from .locators import IncomingOrderLocators as IO


class IncomingOrderPage(BasePage):

    def check_all_box(self):
        checkbox = IO.CHECK_ALL.s('../input')
        if not checkbox.get_attribute('checked'):
            IO.CHECK_ALL.click()

    def create_shipment(self):
        IO.CREATE_SHIPMENT_BUTTON.click()
        upd = random.randint(100000, 9999999999)
        IO.UPD_FIELD.type(upd)
        IO.INVOIS_NUMBER_FIELD.type(upd)
        date = datetime.datetime.today().strftime("%d.%m.%Y")
        IO.DATE_FIELD.type(date)
        self.check_all_box()
        IO.SHIPMENT_BUTTON.click()
        assert self.shuld_be_visible(IO.PRODUCT_IS_SHIPPED), 'Товар не отгружен'

