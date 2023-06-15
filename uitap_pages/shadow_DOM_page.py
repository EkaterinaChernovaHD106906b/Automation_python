import time

import pyperclip
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ShadowDomPage(BasePage):
    BUTTON_GENERATE = (By.CSS_SELECTOR, 'button#buttonGenerate')
    COPY = (By.CSS_SELECTOR, 'button#buttonCopy')

    def get_guid(self):
        css_el = self.driver.find_element(By.XPATH, '//guid-generator')
        shadow_root = css_el.shadow_root
        shadow_root.find_element(By.CSS_SELECTOR, 'button#buttonGenerate').click()
        shadow_root.find_element(By.CSS_SELECTOR, 'button#buttonCopy').click()
        # guid = pyperclip.paste()


