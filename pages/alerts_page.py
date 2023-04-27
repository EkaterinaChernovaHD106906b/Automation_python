import random

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AlertsPage(BasePage):
    ALERT_BUTTON = (By.CSS_SELECTOR, 'button#alertButton')
    TIMER_ALERT_BUTTON = (By.CSS_SELECTOR, 'button#timerAlertButton')
    CONFIRM_BUTTON = (By.CSS_SELECTOR, 'button#confirmButton')
    PROMPT_BUTTON = (By.CSS_SELECTOR, 'button#promtButton')
    CONFIRM_RESULT = (By.CSS_SELECTOR, 'span#confirmResult')
    PROMPT_RESULT = (By.CSS_SELECTOR, 'span#promptResult')

    def see_alert(self):
        self.element_is_visible(self.ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def see_alert_after_5sec(self):
        self.element_is_visible(self.TIMER_ALERT_BUTTON).click()
        alert_window = self.alert_is_present(self.TIMER_ALERT_BUTTON)
        return alert_window.text

    def confirm_alert(self):
        self.element_is_visible(self.CONFIRM_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        result = self.element_is_visible(self.CONFIRM_RESULT)
        return result.text

    def prompt_alert(self):
        text = f'user{random.randint(0,100)}'
        self.element_is_visible(self.PROMPT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        prompt_result = self.element_is_present(self.PROMPT_RESULT).text
        return text, prompt_result

