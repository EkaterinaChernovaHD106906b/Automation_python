from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class NestedFramesPage(BasePage):
    FRAME1 = (By.CSS_SELECTOR, 'iframe#frame1')
    FRAME2 = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    TEXT1 = (By.CSS_SELECTOR, 'body')
    TEXT2 = (By.CSS_SELECTOR, 'p')

    def check_nested_frame(self):
        frame1 = self.element_is_present(self.FRAME1)
        self.driver.switch_to.frame(frame1)
        frame1_text = self.element_is_present(self.TEXT1).text
        frame2 = self.element_is_present(self.FRAME2)
        self.driver.switch_to.frame(frame2)
        frame2_text = self.element_is_present(self.TEXT2).text
        return frame1_text, frame2_text
