from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TabsPage(BasePage):
    WHAT = (By.CSS_SELECTOR, 'a#demo-tab-what')
    ORIGIN = (By.CSS_SELECTOR, 'a#demo-tab-origin')
    USE = (By.CSS_SELECTOR, 'a#demo-tab-use')
    WHAT_TEXT = (By.CSS_SELECTOR, 'div#demo-tabpane-what')
    ORIGIN_TEXT = (By.CSS_SELECTOR, 'div#demo-tabpane-origin')
    USE_TEXT = (By.CSS_SELECTOR, 'div#demo-tabpane-use')

    def click_on_tab(self, name_tab):
        tabs = {'what':
                    {'title': self.WHAT,
                     'content': self.WHAT_TEXT},
                'origin': {
                    'title': self.ORIGIN,
                    'content': self.ORIGIN_TEXT},
                'use':
                    {'title': self.USE,
                     'content': self.USE_TEXT}
                }
        button = self.element_is_visible(tabs[name_tab]['title'])
        button.click()
        text_tab = self.element_is_present(tabs[name_tab]['content']).text
        return [button.text, len(text_tab)]



