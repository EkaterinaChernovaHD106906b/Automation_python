from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ButtonsPage(BasePage):
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, '#doubleClickBtn')
    RIGHT_CLICK_ME_BUTTON = (By.CSS_SELECTOR, '#rightClickBtn')
    CLICK_ME_BUTTON = (By.XPATH, '//div [@class="mt-4"] [2]/button')

    # result
    RESULT_DOUBLE_CLICK = (By.CSS_SELECTOR, '#doubleClickMessage')
    RESULT_RIGHT_CLICK_ME = (By.CSS_SELECTOR, '#rightClickMessage')
    RESULT_CLICK_ME = (By.CSS_SELECTOR, '#dynamicClickMessage')

    def click_on_different_button(self, type_click):
        if type_click == 'double':
            self.action_double_click(self.element_is_visible(self.DOUBLE_CLICK_BUTTON))
            return self.check_clicked_on_the_button(self.RESULT_DOUBLE_CLICK)
        if type_click == 'right':
            self.action_right_click(self.element_is_visible(self.RIGHT_CLICK_ME_BUTTON))
            return self.check_clicked_on_the_button(self.RESULT_RIGHT_CLICK_ME)
        if type_click == 'click':
            self.element_is_visible(self.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(self.RESULT_CLICK_ME)

    def check_clicked_on_the_button(self, element):
        return self.element_is_present(element).text
