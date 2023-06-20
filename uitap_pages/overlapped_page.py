from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OverlappedPage(BasePage):
    INPUT_NAME = (By.CSS_SELECTOR, 'input#name')

    def name_input_field(self, name):
        input_name = self.element_is_present(self.INPUT_NAME)
        self.driver.execute_script("arguments[0].scrollIntoView();", input_name)
        input_name.send_keys(f'{name}')
        input_text = input_name.get_attribute('value')
        return input_text

