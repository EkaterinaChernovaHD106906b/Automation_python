from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AccordianPage(BasePage):
    FIRST_ACCORDIAN = (By.CSS_SELECTOR, 'div#section1Heading')
    SECOND_ACCORDIAN = (By.CSS_SELECTOR, 'div#section2Heading')
    THIRD_ACCORDIAN = (By.CSS_SELECTOR, 'section3Heading')
    FIRST_ACCORDIAN_TEXT = (By.CSS_SELECTOR, 'div#section1Content p')
    SECOND_ACCORDIAN_TEXT = (By.CSS_SELECTOR, 'div#section2Content p')
    THIRD_ACCORDIAN_TEXT = (By.CSS_SELECTOR, 'div#section3Content p')

    def check_first_accordian(self, accordian_num):
        accordian = {'first':
                         {'title': self.FIRST_ACCORDIAN,
                          'content': self.FIRST_ACCORDIAN_TEXT},
                     'second':
                         {'title': self.SECOND_ACCORDIAN,
                          'content': self.SECOND_ACCORDIAN_TEXT},
                     'third':
                         {'title': self.THIRD_ACCORDIAN,
                          'content': self.THIRD_ACCORDIAN_TEXT}
                     }
        base_accordian = self.element_is_visible(accordian[accordian_num]['title'])
        base_accordian.click()
        try:
            accordian_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            base_accordian.click()
            accordian_content = self.element_is_visible(accordian[accordian_num]['content']).text
            return [base_accordian.text, len(accordian_content)]
