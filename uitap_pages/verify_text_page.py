from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class VerifyTextPage(BasePage):
    TEXT = (By.XPATH, '//span[normalize-space(.)="Welcome UserName!"]')

    def find_text(self):
        text = self.element_is_visible(self.TEXT).text
        return text
