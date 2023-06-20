import random

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MouseOverPage(BasePage):
    LINK = (By.XPATH, '//section//div[@class="container"][1]//div[1]//a')
    CLICK_COUNT = (By.CSS_SELECTOR, 'span#clickCount')

    def check_click_count(self):
        count_before = self.element_is_visible(self.CLICK_COUNT).text
        x = random.randint(4, 10)
        while x != 0:
            self.element_is_visible(self.LINK).click()
            x -= 1
        count_after = self.element_is_visible(self.CLICK_COUNT).text
        return count_before, count_after
