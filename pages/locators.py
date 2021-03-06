from selene import by
from selene.support.shared.jquery_style import s, ss


class MainPageLocators:
    MAIN_PAGE = s(by.text('Главная страница'))
    LOGOUT = s('div .headerPerson__exit')
    # ============"Справочники"==========
    CONTRACTORS = s('a[href="/contractors"]')
    STORAGES = s('a[href="/storages/"]')
    USER_BUTTON = s('span.headerActions__name')
    REPORT_IMPORT = s('a[href="/journal"]')
    REPORT_IMPORT_LIST = s("//h1[contains(.,'Журнал загрузок')]")
    CONTRACTS_LIST = s("//h1[contains(.,'Договоры')]")
    CONTRACTS = s('a[href="/contracts"]')
    PRICE_LISTS_LIST = s("//h1[contains(.,'Прайс-листы')]")
    PRICE_LISTS = s('a[href="/prices"]')
    CONTRACTORS_LIST = s("//h1[contains(.,'Контрагенты')]")
    STORAGES_LIST = s("//h1[contains(.,'Склады')]")
    PRODUCTS_LIST = s("//h1[contains(.,'Номенклатура')]")
    PRODUCTS = s('a[href="/nomenclature"]')
    # ==============="Заказы"=============
    OUTGOING_REFUSALS_LIST = s("//h1[contains(.,'Исходящие отказы')]")
    OUTGOING_REFUSALS = s('a[href="/outgoing-refusals"]')
    INCOMING_REFUSALS_LIST = s("//h1[contains(.,'Входящие отказы')]")
    INCOMING_REFUSALS = s('a[href="/inbox-refusals"]')
    OUTGOING_CLAIMS_LIST = s("//span[text() = 'Исходящие претензии']")
    OUTGOING_CLAIMS = s('a[href="/claims-made"]')
    INCOMING_CLAIM_LIST = s("//li/span[text() = 'Входящие претензии']")
    INCOMING_CLAIMS = s('a[href="/claim-received"]')
    ACCEPTANCES_LIST = s("//h1[contains(.,'Приемки')]")
    ACCEPTANCES = s('a[href="/acceptances"]')
    SHIPMENTS_LIST = s("//h1[contains(.,'Отгрузки')]")
    SHIPMENTS = s('a[href="/shipment"]')
    OUTGOING_ORDERS_LIST = s("//h1[contains(.,'Исходящие заказы')]")
    OUTGOING_ORDERS = s('a[href="/outgoing"]')
    INCOMING_ORDERS_LIST = s("//h1[contains(.,'Входящие заказы')]")
    INCOMING_ORDERS = s('a[href="/inbox"]')
    # ==============="Отчёты"=============
    AVAILABLE_PRICE_LIST_ITEM_REPORT = s("//h1[text()='Отчёт по наличию позиций в прайс-листах']")
    AVAILABLE_PRICE_LIST_ITEM = s('a[href="/reports/available-price-list-item"]')
    PRODUCT_LOAD_REPORT = s("//h1[text()='Отчёт по загруженной номенклатуре']")
    PRODUCT_LOAD = s('a[href="/reports/load-nomenclature"]')
    RESERVE_COST_REPORT = s("//h1[text()='Отчёт по стоимости запаса']")
    RESERVE_COST = s('a[href="/reports/reserves-cost"]')
    ACCURED_AGENTIAL_MARKUPS_REPORT = s("//h1[text()='Отчёт по агентской наценке']")
    ACCRUED_AGENTIAL_MARKUPS = s('a[href="/reports/accrued-agential-markups"]')
    AGENTIAL_MATKUPS_REPORT = s("//h1[text()='Агентское вознаграждение портала']")
    AGENTIAL_MARKUPS = s('a[href="/reports/agential-markups"]')
    SALES_REPORT = s("//h1[text()='Отчет по продажам']")
    SALES = s('a[href="/reports/sales"]')
    LOGISTIC_ROUTES = s('a[href="/reports/logistic-routes"]')
    LOGISTIC_ROUTES_REPORT = s("//h1[text()='Логистические маршруты']")
    # =============="Роли"================
    ROLES_LIST = s("//h1[contains(., 'Роли')]")
    ROLES = s('a[href="/roles"]')
    USERS_LIST = s("//h1[contains(., 'Пользователи')]")
    USERS = s('a[href="/users"]')
    # ============"Настройки"============
    NEWS_SETTINGS = s("//h1[text()='Новости']")
    NEWS = s('a[href="/settings/news"]')
    REGULATION_DISCOUNT_SETTINGS = s("//h1[text()='Скидки в РЗ']")
    REGULATION_DISCOUNT = s('a[href="/settings/regulation-discount"]')
    PASSWORD_CHANGE_SETTINGS = s("//h1[text()='Изменение пароля']")
    PASSWORD_CHANGE = s('a[href="/settings/password"]')
    PORTAL_SETTINGS_PAGE = s("//h1[text()='Настройка портала']")
    PORTAL_SETTINGS = s('a[href="/settings/portal"]')
    STORAGE_ID_SETTING = s("//li/span[text()='ID складов']")
    STORAGE_ID = s('a[href="/settings/storage"]')
    CONTRACTOR_ID_SETTING = s("//li/span[text()='ID контрагентов']")
    CONTRACTOR_ID = s('a[href="/settings/contractor"]')
    QUANTITY_NORM_SETTING = s("//h1[text()='Настройка нормы количества в заявке']")
    QUANTITY_NORM = s('a[href="/settings/norm"]')
    NOTIFICATION_SETTING = s("//h1[contains(., 'Настройка оповещений')]")
    NOTIFICATION = s('a[href="/settings/notifications"]')
    INTEGRATION_SETTING = s("//h1[contains(., 'Изменение настроек интеграции')]")
    INTEGRATION = s('a[href="/settings/integration"]')
    ORGANIZATION_SETTING = s("//li/span[text()='Настройки организации']")
    ORGANIZATION = s('a[href="/settings/organization"]')
    # =="Прочее доступное только контрикам"===
    DEFERRED_PAGE = s("//li/span[text()='Отложенные товары']")
    DEFERRED = s("//span[text()='Отложенные товары']")
    BASKET_PAGE = s("//h1[text()='В корзине нет товаров']")
    BASKET = s("//span[text()='Корзина']")
    ADD_REQUEST_PAGE = s("//div[text()='Куда доставить?']")
    ADD_REQUEST = s('a[href="/request/add"]')
    CATOLOG_PAGE = s("//h1[contains(., 'Каталог автозапчастей')]")
    CATALOG = s("//span[text()='Каталог']")
    # ====================================


# class ContractorMainPageLocators:
#     # ==================================
#     # Переписать все локаторы list
#     # ================================
#     # ============"Справочники"==========
#     CONTRACTORS = s('a[href="/contractors"]')
#     STORAGES = s('a[href="/storages/"]')
#     USER_BUTTON = s('span.headerActions__name')
#     LOGOUT = s('div .headerPerson__exit')
#     REPORT_IMPORT = s('a[href="/journal"]')
#     REPORT_IMPORT_LIST = s("//li/span[text()='Журнал загрузок']")
#     CONTRACTS_LIST = s("//li/span[text()='Договоры']")
#     CONTRACTS = s('a[href="/contracts"]')
#     PRICE_LISTS_LIST = s("//li/span[text()='Прайс-листы']")
#     PRICE_LISTS = s('a[href="/prices"]')
#     CONTRACTORS_LIST = s("//li/span[text()='Контрагенты']")
#     STORAGES_LIST = s("//li/span[text()='Склады']")
#     MAIN_PAGE = s(by.text('Главная страница'))
#     PRODUCTS_LIST = s("//h1[text()='Номенклатура']")
#     PRODUCTS = s('a[href="/nomenclature"]')
#     # ==============="Заказы"=============
#     OUTGOING_REFUSALS_LIST = s("//li/span[text() = 'Исходящие отказы']")
#     OUTGOING_REFUSALS = s('a[href="/outgoing-refusals"]')
#     INCOMING_REFUSALS_LIST = s("//li/span[text() = 'Входящие отказы']")
#     INCOMING_REFUSALS = s('a[href="/inbox-refusals"]')
#     OUTGOING_CLAIMS_LIST = s("//div[text() = 'Претензии']")
#     OUTGOING_CLAIMS = s('a[href="/claims"]')
#     INCOMING_CLAIM_LIST = s("//li/span[text() = 'Входящие претензии']")
#     INCOMING_CLAIMS = s('a[href="/claim-received"]')
#     ACCEPTANCES_LIST = s("//h1[contains(.,'Приемки')]")
#     ACCEPTANCES = s('a[href="/acceptances"]')
#     SHIPMENTS_LIST = s("//h1[contains(.,'Отгрузки')]")
#     SHIPMENTS = s('a[href="/shipment"]')
#     OUTGOING_ORDERS_LIST = s("//h1[contains(.,'Исходящие заказы')]")
#     OUTGOING_ORDERS = s('a[href="/outgoing"]')
#     INCOMING_ORDERS_LIST = s("//h1[contains(.,'Входящие заказы')]")
#     INCOMING_ORDERS = s('a[href="/inbox"]')
#     # ==============="Отчёты"=============
#     AVAILABLE_PRICE_LIST_ITEM_REPORT = s("//h1[text()= 'Отчёт по наличию позиции в прайс-листах']")
#     AVAILABLE_PRICE_LIST_ITEM = s('a[href="/reports/available-price-list-item"]')
#     PRODUCT_LOAD_REPORT = s("//h1[text()='Отчёт по загруженной номенклатуре']")
#     PRODUCT_LOAD = s('a[href="/reports/load-nomenclature"]')
#     RESERVE_COST_REPORT = s("//h1[text()='Отчёт по стоимости запаса']")
#     RESERVE_COST = s('a[href="/reports/reserves-cost"]')
#     ACCURED_AGENTIAL_MARKUPS_REPORT = s("//h1[text()='Отчёт по агентской наценке']")
#     ACCRUED_AGENTIAL_MARKUPS = s('a[href="/reports/accrued-agential-markups"]')
#     AGENTIAL_MATKUPS_REPORT = s("//h1[text()='Агентское вознаграждение портала']")
#     AGENTIAL_MARKUPS = s('a[href="/reports/agential-markups"]')
#     SALES_REPORT = s("//h1[text()='Отчет по продажам']")
#     SALES = s('a[href="/reports"]')
#     # =============="Роли"================
#     ROLES_LIST = s("//h1[text()='Роли']")
#     ROLES = s('a[href="/roles"]')
#     USERS_LIST = s("//h1[text()='Пользователи']")
#     USERS = s('a[href="/users"]')
#     # ============"Настройки"============
#     NEWS_SETTINGS = s("//h1[text()='Новости']")
#     NEWS = s('a[href="/settings/news"]')
#     REGULATION_DISCOUNT_SETTINGS = s("//h1[text()='Скидки в РЗ']")
#     REGULATION_DISCOUNT = s('a[href="/settings/regulation-discount"]')
#     PASSWORD_CHANGE_SETTINGS = s("//h1[text()='Изменение пароля']")
#     PASSWORD_CHANGE = s('a[href="/settings/password"]')
#     PORTAL_SETTINGS_PAGE = s("//h1[text()='Настройка портала']")
#     PORTAL_SETTINGS = s('a[href="/settings/portal"]')
#     STORAGE_ID_SETTING = s("//li/span[text()='ID складов']")
#     STORAGE_ID = s('a[href="/settings/storage"]')
#     CONTRACTOR_ID_SETTING = s("//li/span[text()='ID контрагентов']")
#     CONTRACTOR_ID = s('a[href="/settings/contractor"]')
#     QUANTITY_NORM_SETTING = s("//h1[text()='Настройка нормы количества в заявке']")
#     QUANTITY_NORM = s('a[href="/settings/norm"]')
#     NOTIFICATION_SETTING = s("//h1[text()='Настройка оповещений']")
#     NOTIFICATION = s('a[href="/settings/notifications"]')
#     INTEGRATION_SETTING = s("//h1[text()='Изменение настроек интеграции']")
#     INTEGRATION = s('a[href="/settings/integration"]')
#     ORGANIZATION_SETTING = s("//li/span[text()='Настройки организации']")
#     ORGANIZATION = s('a[href="/settings/organization"]')
#     # =="Прочее доступное только контрикам"===
#     DEFERRED_PAGE = s("//li/span[text()='Отложенные товары']")
#     DEFERRED = s("//span[text()='Отложенные товары']")
#     BASKET_PAGE = s("//h1[text()='В корзине нет товаров']")
#     BASKET = s("//span[text()='Корзина']")
#     ADD_REQUEST_PAGE = s("//div[text()='Куда доставить?']")
#     ADD_REQUEST = s('a[href="/request/add"]')
#     CATOLOG_PAGE = s("//h1[contains(., 'Каталог автозапчастей')]")
#     CATALOG = s("//span[text()='Каталог']")
#     # ====================================


class LoginPageLocators:
    LOGIN_FIELD = s('div:nth-child(1) > span > div > div.formInput__body> input')
    CLEAR_LOGIN_FIELD = s('div:nth-child(1) > span > div > div.formInput__body > div > button')
    PASSWORD_FIELD = s('div:nth-child(2) > span > div > div.formInput__body> input')
    CLEAR_PASSWORD_FIELD = s('div:nth-child(2) > span > div > div.formInput__body > div > button')
    LOGIN_BUTTON = s(by.text("Войти"))
    LOGIN_HI = s("//span[contains(text(), 'Авторизация')]")


class OrganizationPageLocators:
    JURIC_ADRES = s('input[placeholder="Юридический адрес"]')
    FACTIAL_ADRES = s('input[placeholder="Фактический адрес"]')
    NAME = s('input[placeholder="Введите название"]')
    SHORT_NAME = s('input[placeholder="Краткое наименование"]')
    FULL_NAME = s('input[placeholder="Полное наименование"]')
    SAVE_BUTTON = s('//button[text()="Сохранить"]')


class IntegrationLocators:
    RETURN_LOD_KEY = s("//div[contains(@class, 'settingsKey__button')]//button[contains(@class, 'm-grey')]")
    SAVE_BUTTON = s("//button[contains(text(), 'Сохранить')]")
    CHANGE_KEY_BUTTON = s("//div[contains(@class, 'settingsKey__button')]//button[contains(@class, 'm-blue')]")
    KEY = s("//div[text()='Ключ авторизации по API']/../div[2]//input")


class NotificationLocators:
    INCOMING_ORDER_CHECKBOX = s("//div[text()='Новые входящие заказы']/../div/label/input")
    NEW_ACCEPTANCES_CHECKBOX = s("//div[text()='Новые приемки']/../div/label/input")
    REFUSALS_CHECKBOX = s("//div[text()='Новые отказы']/../div/label/input")
    ORDER_STATUS_CHECKBOX = s("//div[text()='Информация о состоянии заказа']/../div/label/input")
    OVERDUE_ACCEPTANCES_CHECKBOX = s("//div[text()='Информация о просроченных приемках']/../div/label/input")
    INCOMING_ORDER_ADD_EMAIL_BUTTON = s("//div[text()='Новые входящие заказы']/../../../div/button")
    NEW_ACCEPTANCES_ADD_EMAIL_BUTTON = s("//div[text()='Новые приемки']/../../../div/button")
    REFUSALS_ADD_EMAIL_BUTTON = s("//div[text()='Новые отказы']/../../../div/button")
    ORDER_STATUS_ADD_EMAIL_BUTTON = s("//div[text()='Информация о состоянии заказа']/../../../div/button")
    OVERDUE_ACCEPTANCES_ADD_EMAIL_BUTTON = s("//div[text()='Информация о просроченных приемках']/../../../div/button")
    SAVE_BUTTON = s("//button[text()='Сохранить']")


class ChangePassword:
    PASSWORD_FIELD = s("//div[text()='Пароль']/../span/div/div/input")
    CONFIRM_PASSWORD_FIELD = s("//div[text()='Подтверждение пароля']/../span/div/div/input")
    SAVE_BUTTON = s("//button[text()='Сохранить']")


class Catalog:
    DELIVERY_DAYS = s("//div[contains(@class, 'table-body')]/table/tbody/tr/td[3]/span")
    PRODUCT_PRISE = s("//div[contains(@class, 'table-body')]/table/tbody/tr/td[6]/span")
    ORDER_CREATED = s("//h1[contains(text(), 'Ваш заказ оформлен')]")
    BY_VIN_SEARCH_TOGGLE = s("//div[contains(text(), 'по VIN')]")
    BY_PARTS_SEARCH_TOGGLE = s("//div[contains(text(), 'детали')]")
    PARTS_BY_ARTICLE_BUTTON = s("//div[contains(text(), 'Номер')]")
    PARTS_BY_NAME_BUTTON = s("//div[contains(text(), 'Название')]")
    SEARCH_FIELD = s("//div/input[contains(@class, 'search__input')]")
    SEARCH_BUTTON = s("//button[contains(text(), 'Поиск')]")
    CAR_MARK_FIELD = s('input[placeholder="Марка"]')
    CAR_MODEL_FIELD = s('input[placeholder="Модель"]')
    CAR_CATALOG_FIELD = s('input[placeholder="Каталог"]')
    CAR_SPECIAL_VERSION_FIELD = s('input[placeholder="Специальная версия"]')
    CAR_ENGINE_TYPE_FIELD = s('input[placeholder="Тип двигателя"]')
    CAR_VERSION_FIELD = s('input[placeholder="Вариант"]')
    SEARCH_RESULT = s("//div[contains(@class, 'table-body')]/table/tbody/tr")
    ADD_TO_BASKET = s("//div[contains(@class, 'table-body')]/table/tbody/tr/td[8]/button/span")
    GO_TO_ORDER_CREATE_BUTTON = s("//button[contains(text(), 'Перейти к оформлению')]")
    ORDER_CREATE_BUTTON = s("//button[contains(text(), 'Оформить заказ')]")


class IncomingOrdersListLocators:
    FIRST_ORDER = s("//table/tbody/tr[1]")
    ORDER_EDIT = s('//h1[contains(., "Изменение заказа ")]')

class IncomingOrderLocators:
    CREATE_SHIPMENT_BUTTON = s('//div[contains(@class, "tableNav")]/div/div/div[1]/span/button')
    CHECK_ALL = s("//table/thead/tr/th[1]/div/label")
    UPD_FIELD = s('input[placeholder="Номер ТОРГ-12/УПД"]')
    INVOIS_NUMBER_FIELD = s('input[placeholder="Номер счет-фактуры"]')
    DATE_FIELD = s('input[placeholder="Дата отгрузки"]')
    # CHECK_ALL_IN_SHIPMENT_CREATE = s("//table/thead/tr/th[1]/div/label")
    SHIPMENT_BUTTON = s("//div[contains(@class, 'tableNav')]/div/div/div/span/button")
    PRODUCT_IS_SHIPPED = s("//span[contains(., 'Отгружено')]")
