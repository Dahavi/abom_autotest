import pytest
from selene.api import browser
from .pages.main_page import MainPage
from .pages.users import Users as u
from .pages.products import Products as p
from .pages.pages import Pages
from time import sleep

link = 'http://test12.tk-alpha.ru/'

@pytest.mark.sel2
def test_logout():
    page = Pages(browser)
    page.open(link)
    page.enter(u.test1)
    page.logout()

@pytest.mark.sel3
def test_pages():
    page = Pages(browser)
    page.open(link)
    page.enter(u.test1)
    page.main_page().open_catalog()
    page.logout()
    page.enter(u.test2)
    page.main_page().open_incoming_orders()

@pytest.mark.sel
@pytest.mark.parametrize("user", [u.admin, u.test1, u.test2])
def test_user_logins(user):
    page = Pages(browser)
    page.open(link)
    page.enter(user)


@pytest.mark.hell
def test_admin_page_clicking():
    page = Pages(browser)
    page.open(link)
    page.enter(u.admin)
    page.main_page().open_products()
    page.main_page().open_storages()
    page.main_page().open_contractors()
    page.main_page().open_price_lists()
    page.main_page().open_contracts()
    page.main_page().open_report_import()
    page.main_page().open_incoming_orders()
    page.main_page().open_outgoing_orders()
    page.main_page().open_shipments()
    page.main_page().open_acceptances()
    page.main_page().open_incoming_claims()
    page.main_page().open_outgoing_claims()
    page.main_page().open_incoming_refusals()
    page.main_page().open_outgoing_refusals()
    page.main_page().open_sales_report()
    page.main_page().open_agential_markups_report()
    page.main_page().open_accrued_agential_markups_report()
    page.main_page().open_reserve_cost_report()
    page.main_page().open_product_load_report()
    page.main_page().open_available_price_list_item_report()
    page.main_page().open_users()
    page.main_page().open_roles()
    page.main_page().open_portal_settings()
    page.main_page().open_password_change_settings()
    page.main_page().open_regulation_discount()
    page.main_page().open_news()

@pytest.mark.hell2
def test_distrib_page_clicking():
    page = Pages(browser)
    page.open(link)
    page.enter(u.test2)
    # page.main_page().open_catalog()
    page.main_page().open_products()
    page.main_page().open_storages()
    page.main_page().open_contractors()
    page.main_page().open_price_lists()
    page.main_page().open_contracts()
    page.main_page().open_report_import()
    page.main_page().open_incoming_orders()
    page.main_page().open_outgoing_orders()
    page.main_page().open_shipments()
    page.main_page().open_acceptances()
    page.main_page().open_incoming_claims()
    page.main_page().open_outgoing_claims()
    page.main_page().open_incoming_refusals()
    page.main_page().open_outgoing_refusals()
    page.main_page().open_sales_report()
    # page.main_page().open_available_price_list_item_report()
    page.main_page().open_users()
    page.main_page().open_roles()
    page.main_page().open_basket()
    page.main_page().open_deferred()
    page.main_page().open_organization()
    page.main_page().open_integration()
    page.main_page().open_notification()
    page.main_page().open_quantity_norm()
    page.main_page().open_password_change_settings()
    page.main_page().open_contractor_id()
    page.main_page().open_storage_id()

@pytest.mark.hell3
def test_change_organization_name():
    page = Pages(browser)
    page.open(link)
    page.enter(u.test2)
    page.main_page().open_organization()
    page.organization_page().change_full_name("new_name1")
    page.organization_page().change_short_name("new_short_name1")
    page.organization_page().change_factial_adres('новый адрес')
    page.organization_page().change_juric_adres('новый адрес')

@pytest.mark.hell4
def test_change_integration():
    page = Pages(browser)
    page.open(link)
    page.enter(u.test2)
    page.main_page().open_integration()
    page.integration_page().change_key()
    page.integration_page().return_old_key()

@pytest.mark.hell5
def test_notification_settings():
    page = Pages(browser)
    page.open(link)
    page.enter(u.test2)
    page.main_page().open_notification()
    page.notification_page().something()

@pytest.mark.hell6
def test_DD_basket():
    page = Pages(browser)
    page.open(link)
    page.enter(u.test2)
    page.main_page().open_catalog()
    page.catalog_page().find_product_by_article(p.MD1)


