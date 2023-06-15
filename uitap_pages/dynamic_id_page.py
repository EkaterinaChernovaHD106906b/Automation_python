from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DynamicIdPage(BasePage):
    BUTTON = (By.CSS_SELECTOR, 'button[class="btn btn-primary"]')

    def click_on_the_button(self):
        button_id_before = self.element_is_visible(self.BUTTON).get_attribute('id')
        self.element_is_visible(self.BUTTON).click()
        self.driver.refresh()
        button_id_after = self.element_is_visible(self.BUTTON).get_attribute('id')
        return button_id_before, button_id_after
