from .locators import IntegrationLocators as IL
from .base_page import BasePage
from time import sleep


class IntegrationPage(BasePage):

    def change_key(self):
        old_value = IL.KEY.click().get_attribute('value')
        IL.CHANGE_KEY_BUTTON.click()
        sleep(1)
        IL.SAVE_BUTTON.click()
        self.refresh_page()
        new_value = IL.KEY.get_attribute('value')
        assert old_value != new_value, 'Ключ не изменился'

    def return_old_key(self):
        old_value = IL.KEY.get_attribute('value')
        IL.CHANGE_KEY_BUTTON.click()
        sleep(1)
        IL.RETURN_LOD_KEY.click()
        sleep(1)
        IL.SAVE_BUTTON.click()
        self.refresh_page()
        new_value = IL.KEY.get_attribute('value')
        assert old_value == new_value, 'Старой ключь не вернулся'
