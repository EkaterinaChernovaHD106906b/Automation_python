import random
import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProgressBarPage(BasePage):
    START_STOP_BUTTON = (By.CSS_SELECTOR, 'button#startStopButton')
    BAR_PROGRESS = (By.CSS_SELECTOR, 'div[class="progress-bar bg-info"]')

    def change_bar_progress(self):
        value_before = self.element_is_present(self.BAR_PROGRESS).get_attribute('aria-valuenow')
        self.element_is_visible(self.START_STOP_BUTTON).click()
        time.sleep(random.randint(3, 10))
        self.element_is_visible(self.START_STOP_BUTTON).click()
        value_after = self.element_is_present(self.BAR_PROGRESS).get_attribute('aria-valuenow')
        return value_before, value_after
