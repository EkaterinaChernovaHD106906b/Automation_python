from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button#tabButton')
    NEW_WINDOW = (By.CSS_SELECTOR, 'button#windowButton')
    TEXT_NEW_TAB = (By.CSS_SELECTOR, 'h1#sampleHeading')

    def open_new_tab(self):
        self.element_is_visible(self.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text = self.element_is_present(self.TEXT_NEW_TAB).text
        return text

    def open_new_window(self):
        self.element_is_visible(self.NEW_WINDOW).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text = self.element_is_visible(self.TEXT_NEW_TAB).text
        return text

