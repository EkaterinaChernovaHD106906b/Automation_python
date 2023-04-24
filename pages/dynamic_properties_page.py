import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DynamicPropertiesPage(BasePage):
    BUTTON_COLOR_CHANGE = (By.CSS_SELECTOR, 'button[id="colorChange"]')
    BUTTON_VISIBLE_AFTER = (By.CSS_SELECTOR, 'button[id="visibleAfter"]')
    BUTTON_ENABLE_5SEC = (By.CSS_SELECTOR, 'button[id="enableAfter"]')

    def check_enable_button(self):
        try:
            self.element_is_clickable(self.BUTTON_ENABLE_5SEC)
        except TimeoutException:
            return False
        return True


    def check_changed_of_color(self):
        color_button = self.element_is_present(self.BUTTON_COLOR_CHANGE)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after

    def check_appear_of_button(self):
        try:
            self.element_is_visible(self.BUTTON_VISIBLE_AFTER)
        except TimeoutException:
            return False
        return True
