import random

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SliderPage(BasePage):
    INPUT_SLIDER = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')

    def change_slider_value(self):
        value_before = self.element_is_visible(self.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(self.SLIDER_VALUE).get_attribute('value')

        return value_before, value_after
