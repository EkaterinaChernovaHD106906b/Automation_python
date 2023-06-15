import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ClassAttributePage(BasePage):
    BLUE_BUTTON = (By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')][@type='button']")

    def check_button_class(self):
        self.scroll_by(500)
        self.element_is_visible(self.BLUE_BUTTON).click()
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text
