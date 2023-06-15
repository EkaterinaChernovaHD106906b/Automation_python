from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HiddenLayersPage(BasePage):
    GREEN_BUTTON = (By.CSS_SELECTOR, 'button#greenButton')

    def click_on_green_button(self):
        self.element_is_visible(self.GREEN_BUTTON).click()
        try:
            self.element_is_visible(self.GREEN_BUTTON).click()
        except:
            massage = 'Button is not clickable'
            print(massage)
            return massage
