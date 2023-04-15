import random

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckBoxPage(BasePage):

    BUTTON_EXPAND_ALL = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    ITEM_LIST = (By.CSS_SELECTOR, 'span[class="rct-title"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    TITLE_ITEM = (By.XPATH, './/ancestor::span[@class="rct-text"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span.text-success')

    def open_full_list(self):
        self.element_is_visible(self.BUTTON_EXPAND_ALL).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.ITEM_LIST)
        count = 5
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element("xpath", './/ancestor::span[@class="rct-text"]')
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


