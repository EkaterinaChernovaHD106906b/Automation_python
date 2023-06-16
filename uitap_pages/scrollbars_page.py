from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ScrollBarsPage(BasePage):
    SCROLLBAR = (By.CSS_SELECTOR, 'body > section > div > div')
    BUTTON = (By.CSS_SELECTOR, 'button#hidingButton')

    def use_scrollbar(self):
        hiding_button = self.element_is_present(self.BUTTON)
        self.move_to_element(hiding_button)
        button_name = self.element_is_visible(self.BUTTON).text
        if self.element_is_visible(self.BUTTON):
            print(f'{button_name} is visible')

