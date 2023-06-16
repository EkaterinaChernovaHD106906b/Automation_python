from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DynamicTablePage(BasePage):
    CHROME_ROW = (By.XPATH, '//div[./span[contains(text(),"Chrome")]]')
    CPU = (By.XPATH, '//div[./span[contains(text(),"Chrome")]]//span[contains(text(), "%")]')
    LABEL = (By.CSS_SELECTOR, 'p[class="bg-warning"]')

    def get_value_of_cpu(self):
        value = self.element_is_visible(self.CPU).text
        label_text = self.element_is_visible(self.LABEL).text
        label_split = label_text.split()
        label_cpu = label_split[2]
        return value, label_cpu
