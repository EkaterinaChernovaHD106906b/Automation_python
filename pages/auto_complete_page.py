import random

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from generator.generator import generated_color
from pages.base_page import BasePage


class AutoCompletePage(BasePage):
    MULTIPLE_INPUT = (By.CSS_SELECTOR, 'input#autoCompleteMultipleInput')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input#autoCompleteSingleInput')
    MULTI_VALUE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    VALUE_REMOVE = (By.CSS_SELECTOR, 'div[class="css-xb97g8 auto-complete__multi-value__remove"] svg path')
    SINGLE_CONTAINER = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')

    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(1, 4))
        # k- number of colors/elements
        for color in colors:
            input_multi = self.element_is_clickable(self.MULTIPLE_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_visible(self.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_visible(self.MULTI_VALUE))
        return count_value_before, count_value_after

    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_single_input(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self):
        color = self.element_is_visible(self.SINGLE_CONTAINER)
        return color.text
