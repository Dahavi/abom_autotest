import pytest
from selene.api import browser
from .pages.users import Users as u
from .pages.products import Products as p
from .pages.pages import Pages


link ='http://test14.tk-alpha.ru'


@pytest.mark.sel3
def test_DD_basket():
    page = Pages(browser)
    page.open(link)
    page.enter(u.test2)
    page.main_page().open_catalog()
    page.catalog_page().find_product_by_article(p.MD1)
