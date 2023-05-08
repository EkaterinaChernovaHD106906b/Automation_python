import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from generator.generator import generated_date
from pages.base_page import BasePage


class DatePickerPage(BasePage):
    DATE_INPUT = (By.CSS_SELECTOR, 'input#datePickerMonthYearInput')
    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, 'input#dateAndTimePickerInput')
    SELECT_MONTH = (By.CSS_SELECTOR, 'select.react-datepicker__month-select')
    SELECT_YEAR = (By.CSS_SELECTOR, 'select.react-datepicker__year-select')
    SELECT_DATE_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')
    DATE_TIME_MONTH_INPUT = (By.CSS_SELECTOR, 'div.react-datepicker__month-read-view')
    DATE_TIME_YEAR_INPUT = (By.CSS_SELECTOR, 'div.react-datepicker__year-read-view')
    DATE_TIME_TIME = (By.CSS_SELECTOR, 'li.react-datepicker__time-list-item')
    DATE_TIME_MONTH_LIST = (By.CSS_SELECTOR, 'div.react-datepicker__month-option')
    DATE_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div.react-datepicker__year-option')

    @allure.step('Select date')
    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        with allure.step('select month, year, date'):
            self.select_date_by_text(self.SELECT_MONTH, date.month)
            self.select_date_by_text(self.SELECT_YEAR, date.year)
            self.select_date_item_from_list(self.SELECT_DATE_LIST, date.day)
            value_date_after = input_date.get_attribute('value')
            return value_date_before, value_date_after

    def select_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def select_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break

    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_visible(self.DATE_TIME_MONTH_INPUT).click()
        self.select_date_item_from_list(self.DATE_TIME_MONTH_LIST, date.month)
        self.element_is_visible(self.DATE_TIME_YEAR_INPUT).click()
        self.select_date_item_from_list(self.DATE_TIME_YEAR_LIST, '2020')
        self.select_date_item_from_list(self.SELECT_DATE_LIST, date.day)
        self.select_date_item_from_list(self.DATE_TIME_TIME, date.time)
        input_date_after = self.element_is_visible(self.DATE_AND_TIME_INPUT)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after
