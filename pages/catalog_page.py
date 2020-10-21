from selene.support.conditions.be import clickable

from .base_page import BasePage
from .locators import Catalog as CL

import time


class CatalogPage(BasePage):

    def find_product_by_article(self, atticle):
        CL.BY_PARTS_SEARCH_TOGGLE.click()
        CL.PARTS_BY_ARTICLE_BUTTON.click()
        CL.SEARCH_FIELD.type(atticle[0])
        CL.SEARCH_BUTTON.click()
        assert self.shuld_be_visible(CL.SEARCH_RESULT), 'Товар не найден'

    def bay_first_product(self):
        CL.ADD_TO_BASKET.click()
        CL.GO_TO_ORDER_CREATE_BUTTON.click()
        CL.ORDER_CREATE_BUTTON.click()
        assert self.shuld_be_visible(CL.ORDER_CREATED), 'Заказ не создан'

    def get_product_price(self):
        price = CL.PRODUCT_PRISE.text
        price = price.split(' ')
        price = price[0]
        return price

    def assert_prise(self, price):
        price_2 = self.get_product_price()
        assert price[2] == price_2, 'Цена расчитана не верно'

    def get_delivery_days(self):
        delivery = CL.DELIVERY_DAYS.text
        delivery = delivery.split(' ')
        delivery = delivery[0]
        return delivery

    def assert_delivery_days(self, days):
        days_2 = self.get_delivery_days()
        assert days[1] == days_2, 'Доставка расчитана не верно'
