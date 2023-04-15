import random

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RadioButtonPage(BasePage):
    YES_RADIO_BUTTON = (By.CSS_SELECTOR, 'label[for="yesRadio"]')
    IMPRESSIVE_RADIO_BUTTON = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    NO_RADIO_BUTTON = (By.CSS_SELECTOR, "label[for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')

    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.YES_RADIO_BUTTON,
                   'impressive': self.IMPRESSIVE_RADIO_BUTTON,
                   'no': self.NO_RADIO_BUTTON}
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.OUTPUT_RESULT).text
