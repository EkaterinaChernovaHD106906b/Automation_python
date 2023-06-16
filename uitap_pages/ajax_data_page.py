from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AJAXDataPage(BasePage):
    BUTTON = (By.CSS_SELECTOR, 'button#ajaxButton')
    MASSAGE = (By.CSS_SELECTOR, 'p.bg-success')

    def wait_element_ajax(self):
        self.element_is_visible(self.BUTTON).click()
        el = self.wait_ajax_request(self.MASSAGE).text
        return el


