import random
import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProgressBarPageUi(BasePage):
    START_BUTTON = (By.CSS_SELECTOR, 'button#startButton')
    STOP_BUTTON = (By.CSS_SELECTOR, 'button#stopButton')
    PROGRESS_BAR = (By.CSS_SELECTOR, 'div#progressBar')

    def check_bar_progress(self):
        value_before = self.element_is_visible(self.PROGRESS_BAR).get_attribute('aria-valuenow')
        self.element_is_visible(self.START_BUTTON).click()
        time.sleep(random.randint(3, 7))
        self.element_is_visible(self.STOP_BUTTON)
        value_after = self.element_is_visible(self.PROGRESS_BAR).get_attribute('aria-valuenow')
        print(f'Download progress: {value_after}')
        return value_before, value_after

