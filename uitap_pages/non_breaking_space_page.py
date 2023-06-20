from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class NonBreakingSpacePage(BasePage):
    BUTTON = (By.XPATH, '//button[text()="My\u00a0Button"]')  # use unicode for &nbsp

    def find_button_by_text(self):
        self.element_is_visible(self.BUTTON).click()
