from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ModalDialogsPage(BasePage):

    SMALL_MODAL = (By.CSS_SELECTOR, 'button#showSmallModal')
    LARGE_MODAL = (By.CSS_SELECTOR, 'button#showLargeModal')
    SMALL_TEXT = (By.CSS_SELECTOR, 'div.modal-content div.modal-body')
    CLOSE_SMALL_BUTTON = (By.CSS_SELECTOR, 'button#closeSmallModal')
    LARGE_TEXT = (By.CSS_SELECTOR, 'div.modal-content p')
    CLOSE_LARGE_BUTTON = (By.CSS_SELECTOR, 'button#closeLargeModal')
    SMALL_TITLE = (By.CSS_SELECTOR, 'div#example-modal-sizes-title-sm')
    LARGE_TITLE = (By.CSS_SELECTOR, 'div#example-modal-sizes-title-lg')

    def check_modal(self):
        self.element_is_visible(self.SMALL_MODAL).click()
        title_small = self.element_is_visible(self.SMALL_TITLE).text
        text_small = self.element_is_present(self.SMALL_TEXT).text
        self.element_is_visible(self.CLOSE_SMALL_BUTTON).click()
        self.element_is_visible(self.LARGE_MODAL).click()
        title_large = self.element_is_visible(self.LARGE_TITLE).text
        text_large = self.element_is_present(self.LARGE_TEXT).text
        self.element_is_visible(self.CLOSE_LARGE_BUTTON).click()
        return [title_small, len(text_small)], [title_large, len(text_large)]


