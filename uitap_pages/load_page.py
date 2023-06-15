from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoadPage(BasePage):
    HOME_LINK = (By.XPATH, '//li[@class="nav-item"][1]/a')
    LOAD_DELAY_LINK = (By.CSS_SELECTOR, 'a[href="/loaddelay"]')
    BUTTON = (By.CSS_SELECTOR, 'button[class="btn btn-primary"]')

    def loading_page(self):
        self.element_is_visible(self.HOME_LINK).click()
        self.element_is_visible(self.LOAD_DELAY_LINK).click()
        button = self.element_is_visible(self.BUTTON)
        text = button.text
        button.click()
        return text






