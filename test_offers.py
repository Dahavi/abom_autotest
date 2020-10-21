import pytest
from selene import browser
from .pages.users import Users as u
from .pages.pages import Pages

link = 'http://test.tk-alpha.ru'

@pytest.mark.offers
def test_MD_offer():
    page = Pages(browser)
    page.open(link)
    page.enter(u.test2)

