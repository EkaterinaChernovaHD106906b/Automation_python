import requests
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LinkPage(BasePage):
    SIMPLE_LINK = (By.CSS_SELECTOR, '#simpleLink')
    DYNAMIC_LINK = (By.CSS_SELECTOR, '#dynamicLink')
    CREATED_LINK = (By.CSS_SELECTOR, '#created')
    NO_CONTENT_LINK = (By.CSS_SELECTOR, '#no-content')
    MOVED_LINK = (By.CSS_SELECTOR, '#moved')
    BAD_REQUEST_LINK = (By.CSS_SELECTOR, '#bad-request')
    UNAUTHORIZED_LINK = (By.CSS_SELECTOR, '#unauthorized')
    FORBIDDEN_LINK = (By.CSS_SELECTOR, '#forbidden')
    NOT_FOUND_LINK = (By.CSS_SELECTOR, '#invalid-url')

    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    def check_broken_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.BAD_REQUEST_LINK).click()
        else:
            return request.status_code




