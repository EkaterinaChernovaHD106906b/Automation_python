import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TextBoxPage(BasePage):
    FULL_NAME = (By.CSS_SELECTOR, '#userName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#permanentAddress')
    SUBMIT = (By.CSS_SELECTOR, '#submit')
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')

    def fill_all_fields(self):
        self.remove_footer()
        self.element_is_visible(self.FULL_NAME).send_keys("Joe")
        self.element_is_visible(self.EMAIL).send_keys("Joe@mail.com")
        self.element_is_visible(self.CURRENT_ADDRESS).send_keys("LA, 67980")
        self.element_is_visible(self.PERMANENT_ADDRESS).send_keys("LA, 67589")
        self.driver.execute_script("window.scrollTo(0, 250);")
        self.element_is_clickable(self.SUBMIT).click()

    def check_filled_form(self):
        full_name = self.element_is_present(self.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address
