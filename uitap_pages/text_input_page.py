from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TextInputPage(BasePage):
    INPUT = (By.CSS_SELECTOR, 'input#newButtonName')
    BUTTON = (By.CSS_SELECTOR, 'button#updatingButton')

    def check_text_on_the_button(self):
        name = 'New Button'
        button_name_before = self.element_is_visible(self.BUTTON).text
        self.element_is_visible(self.INPUT).send_keys(f'{name}')
        self.element_is_visible(self.BUTTON).click()
        button_name_after = self.element_is_visible(self.BUTTON).text
        return button_name_before, button_name_after
