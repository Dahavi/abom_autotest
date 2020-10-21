import time

from selene import have
from selene.bys import parent, by
from selene.support.shared.jquery_style import s

from .base_page import BasePage
from .locators import MainPageLocators

# ============================================
# Обсудить, как будем разделять админа и контрагента (локаторы для проверки разные)
# Вариант 1. На странице маин паге сделать 2 класса админ_маин_паге и контрактор_маин_паге
# Вариант 2. Оставить 1 класс маин_паге и разделять методы, например опен_админ_инкоминг_ордер
# Вариант 3. Добавить в методах проверку на тип юзера, и на последнем шаге выбирать действие в зависимости от типа юзера (плохо предстовляю как это сделать)
# ============================================


def is_opened(element):
    # Проверяет что раздел свёрнут/развёрнут
    parent_element = element.s('../..')
    x = parent_element.get_attribute('class')
    y = parent_element.s('..').tag_name
    if not "m-active" in x:
        if y == 'div':
            parent_element.s('../..').click()
        else:
            parent_element.s('..').first_child.click()


class MainPage(BasePage):

    def open_catalog(self):
        # нет проверки is_opened так-как каталог сам по себе раздел
        element = MainPageLocators.CATALOG.s('../..')
        element.click()
        assert self.shuld_be_visible(MainPageLocators.CATOLOG_PAGE), 'Страница каталога не открылась'

    def open_basket(self):
        element = MainPageLocators.BASKET.s('../..')
        element.click()
        # ================================================
        # доработать, так-как метод сработает только если корзина пустая
        # ================================================
        assert self.shuld_be_visible(MainPageLocators.BASKET_PAGE), 'Корзина не открылась'

    def open_deferred(self):
        element = MainPageLocators.DEFERRED.s('../..')
        element.click()
        assert self.shuld_be_visible(MainPageLocators.DEFERRED_PAGE), 'Страница "Отложенные товары" не открылась'

    def open_add_request(self):
        element = MainPageLocators.ADD_REQUEST
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.ADD_REQUEST_PAGE), 'Страница "Загрузить заказ" не открылась'


    def open_incoming_orders(self):
        element = MainPageLocators.INCOMING_ORDERS
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.INCOMING_ORDERS_LIST), 'Журнал входящих заказов не открылся'

    def open_outgoing_orders(self):
        element = MainPageLocators.OUTGOING_ORDERS
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.OUTGOING_ORDERS_LIST), 'Журнал исходящих заказов не открылся'

    def open_shipments(self):
        element = MainPageLocators.SHIPMENTS
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.SHIPMENTS_LIST), 'Журнал загрузок не открылся'

    def open_acceptances(self):
        element = MainPageLocators.ACCEPTANCES
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.ACCEPTANCES_LIST), 'Журнал приёмок не открылся'

    def open_incoming_claims(self):
        element = MainPageLocators.INCOMING_CLAIMS
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.INCOMING_CLAIM_LIST), 'Журнал входящих претензий не открылся'

    def open_outgoing_claims(self):
        element = MainPageLocators.OUTGOING_CLAIMS
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.OUTGOING_CLAIMS_LIST), 'Журнал исходящих претензий не открылся'

    def open_incoming_refusals(self):
        element = MainPageLocators.INCOMING_REFUSALS
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.INCOMING_REFUSALS_LIST), 'Журнал входящих отказов не открылся'

    def open_outgoing_refusals(self):
        element = MainPageLocators.OUTGOING_REFUSALS
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.OUTGOING_REFUSALS_LIST), 'Журнал исходящих отказов не открылся'

    def open_storages(self):
        element = MainPageLocators.STORAGES
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.STORAGES_LIST), 'Журнал складов не открылся'

    def open_contractors(self):
        element = MainPageLocators.CONTRACTORS
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.CONTRACTORS_LIST), 'Журнал контрагентов не открылся'

    def open_price_lists(self):
        element = MainPageLocators.PRICE_LISTS
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.PRICE_LISTS_LIST), 'Журнал прайс-листов не открылся'

    def open_contracts(self):
        element = MainPageLocators.CONTRACTS
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.CONTRACTS_LIST), 'Журнал договоров не открылся'

    def open_report_import(self):
        element = MainPageLocators.REPORT_IMPORT
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.REPORT_IMPORT_LIST), 'Журнал загрузок не открылся'

    def open_products(self):
        element = MainPageLocators.PRODUCTS
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.PRODUCTS_LIST), 'Журнал номенклатуры не открылся'

    def open_sales_report(self):
        element = MainPageLocators.SALES
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.SALES_REPORT), 'Отчёт по продажам не открылся'

    def open_agential_markups_report(self):
        element = MainPageLocators.AGENTIAL_MARKUPS
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.AGENTIAL_MATKUPS_REPORT), 'Отчёт по агентскому вознагрождению не открылся'

    def open_accrued_agential_markups_report(self):
        element = MainPageLocators.ACCRUED_AGENTIAL_MARKUPS
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.ACCURED_AGENTIAL_MARKUPS_REPORT), 'Отчёт по агентской наценке не открылся'

    def open_reserve_cost_report(self):
        element = MainPageLocators.RESERVE_COST
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.RESERVE_COST_REPORT), 'Отчёт по стоимости запаса не открылся'

    def open_product_load_report(self):
        element = MainPageLocators.PRODUCT_LOAD
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.PRODUCT_LOAD_REPORT), 'Отчёт по загруженной номенклатуры не открылся'

    def open_logistic_routes_report(self):
        element = MainPageLocators.LOGISTIC_ROUTES
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.LOGISTIC_ROUTES_REPORT), 'Отчёт по лог.маршрутам не открылся'

    def open_available_price_list_item_report(self):
        element = MainPageLocators.AVAILABLE_PRICE_LIST_ITEM
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.AVAILABLE_PRICE_LIST_ITEM_REPORT), 'Отчёт по наличию позиций в прайс-листах не открылся'

    def open_users(self):
        element = MainPageLocators.USERS
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.USERS_LIST), 'Журнал пользователей не открылся'

    def open_roles(self):
        element = MainPageLocators.ROLES
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.ROLES_LIST), 'Журнал ролей не открылся'

    def open_portal_settings(self):
        element = MainPageLocators.PORTAL_SETTINGS
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.PORTAL_SETTINGS_PAGE), 'Настройки портала не открылись'

    def open_password_change_settings(self):
        element = MainPageLocators.PASSWORD_CHANGE
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.PASSWORD_CHANGE_SETTINGS), 'Настройки изменения пароля не открылись'

    def open_regulation_discount(self):
        element = MainPageLocators.REGULATION_DISCOUNT
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.REGULATION_DISCOUNT_SETTINGS), 'Скидки в РЗ не открылись'

    def open_news(self):
        element = MainPageLocators.NEWS
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.NEWS_SETTINGS), 'Новости не открылись'

    def open_organization(self):
        element = MainPageLocators.ORGANIZATION
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.ORGANIZATION_SETTING), 'Настройки организации не открылись'

    def open_integration(self):
        element = MainPageLocators.INTEGRATION
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.INTEGRATION_SETTING), 'Настройки интеграции не открылись'

    def open_notification(self):
        element = MainPageLocators.NOTIFICATION
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.NOTIFICATION_SETTING), 'Настройки оповещений не открылись'

    def open_quantity_norm(self):
        element = MainPageLocators.QUANTITY_NORM
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.QUANTITY_NORM_SETTING), 'Нормы количества не открылись'

    def open_contractor_id(self):
        element = MainPageLocators.CONTRACTOR_ID
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.CONTRACTOR_ID_SETTING), 'ID контрагентов не открылись'

    def open_storage_id(self):
        element = MainPageLocators.STORAGE_ID
        is_opened(element)
        element.click()
        assert self.shuld_be_visible(MainPageLocators.STORAGE_ID_SETTING), 'ID складов не открылись'





