import time
from selene.support.conditions.be import visible, enabled, disabled, not_


from .base_page import BasePage
from .locators import OrganizationPageLocators as OPL


class OrganizationPage(BasePage):

    def change_full_name(self, new_name):
        old_value = OPL.FULL_NAME.get_attribute('value')
        OPL.FULL_NAME.clear()
        OPL.FULL_NAME.click().type(new_name)  # дополнительный клик для фокуса на элементе, что бы скрыть панель
        assert OPL.SAVE_BUTTON.wait_until(enabled), 'Кнопка не активна'
        OPL.SAVE_BUTTON.click()
        assert OPL.SAVE_BUTTON.wait_until(disabled), 'Кнопка не дактивировалась'
        self.refresh_page()
        assert OPL.FULL_NAME.get_attribute('value') == new_name, 'Значение не изменилось'
        OPL.FULL_NAME.click().type(old_value)
        OPL.SAVE_BUTTON.click()

    def change_short_name(self, new_name):
        old_value = OPL.SHORT_NAME.get_attribute('value')
        OPL.SHORT_NAME.clear()
        OPL.SHORT_NAME.click().type(new_name)
        assert OPL.SAVE_BUTTON.wait_until(enabled), 'Кнопка не активна'
        OPL.SAVE_BUTTON.click()
        assert OPL.SAVE_BUTTON.wait_until(disabled), 'Кнопка не дактивировалась'
        self.refresh_page()
        assert OPL.SHORT_NAME.get_attribute('value') == new_name, 'Значение не изменилось'
        OPL.SHORT_NAME.click().type(old_value)
        OPL.SAVE_BUTTON.click()

    def change_name(self, new_name):
        old_value = OPL.NAME.get_attribute('value')
        OPL.NAME.clear()
        OPL.NAME.click().type(new_name)
        assert OPL.SAVE_BUTTON.wait_until(enabled), 'Кнопка не активна'
        OPL.SAVE_BUTTON.click()
        assert OPL.SAVE_BUTTON.wait_until(disabled), 'Кнопка не деактивировалась'
        self.refresh_page()
        assert OPL.NAME.get_attribute('value') == new_name, 'Значение не изменилось'
        OPL.NAME.click().type(old_value)
        OPL.SAVE_BUTTON.click()

    def change_factial_adres(self, new_adres):
        old_value = OPL.FACTIAL_ADRES.get_attribute('value')
        OPL.FACTIAL_ADRES.clear()
        OPL.FACTIAL_ADRES.click().type(new_adres)
        assert OPL.SAVE_BUTTON.wait_until(enabled), 'Кнопка не активна'
        OPL.SAVE_BUTTON.click()
        assert OPL.SAVE_BUTTON.wait_until(disabled), 'Кнопка не деактивировалась'
        self.refresh_page()
        assert OPL.FACTIAL_ADRES.get_attribute('value') == new_adres, 'Значение не изменилось'
        OPL.FACTIAL_ADRES.click().type(old_value)
        OPL.SAVE_BUTTON.click()

    def change_juric_adres(self, new_adres):
        old_value = OPL.JURIC_ADRES.get_attribute('value')
        OPL.JURIC_ADRES.clear()
        OPL.JURIC_ADRES.click().type(new_adres)
        assert OPL.SAVE_BUTTON.wait_until(enabled), 'Кнопка не активна'
        OPL.SAVE_BUTTON.click()
        assert OPL.SAVE_BUTTON.wait_until(disabled), 'Кнопка не деактивировалась'
        self.refresh_page()
        assert OPL.JURIC_ADRES.get_attribute('value') == new_adres, 'Значение не изменилось'
        OPL.JURIC_ADRES.click().type(old_value)
        OPL.SAVE_BUTTON.click()

