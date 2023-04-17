import time

from selenium.webdriver.common.by import By

from generator.generator import generated_person
from pages.base_page import BasePage


class WebTablePage(BasePage):
    # add person form
    ADD_BUTTON = (By.CSS_SELECTOR, '#addNewRecordButton')
    FIRST_NAME = (By.CSS_SELECTOR, 'input#firstName')
    LAST_NAME = (By.CSS_SELECTOR, 'input#lastName')
    EMAIL = (By.CSS_SELECTOR, 'input#userEmail')
    AGE = (By.CSS_SELECTOR, 'input#age')
    SALARY = (By.CSS_SELECTOR, 'input#salary')
    DEPARTMENT = (By.CSS_SELECTOR, 'input#department')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button#submit')

    # table
    LIST = (By.CSS_SELECTOR, 'div.rt-tr-group')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input#searchBox')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = (By.XPATH, './/ancestor::div[@class="rt-tr-group"]')

    # update
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')
    INPUT_AGE = (By.CSS_SELECTOR, 'input#age')
    NO_ROWS_FOUND = (By.CSS_SELECTOR, 'div.rt-noData')
    COUNT_ROWS = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')

    def add_new_person(self):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.ADD_BUTTON).click()
            self.element_is_visible(self.FIRST_NAME).send_keys(first_name)
            self.element_is_visible(self.LAST_NAME).send_keys(last_name)
            self.element_is_visible(self.EMAIL).send_keys(email)
            self.element_is_visible(self.AGE).send_keys(age)
            self.element_is_visible(self.SALARY).send_keys(salary)
            self.element_is_visible(self.DEPARTMENT).send_keys(department)
            self.element_is_visible(self.SUBMIT_BUTTON).click()
            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]

    def check_new_added_person(self):
        people_list = self.elements_are_present(self.LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
            # splitlines() delete \n
        return data

    def search_some_person(self, key_word):
        self.element_is_visible(self.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.element_is_present(self.DELETE_BUTTON)
        row = delete_button.find_element('xpath', './/ancestor::div[@class="rt-tr-group"]')
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.UPDATE_BUTTON).click()
        self.element_is_visible(self.INPUT_AGE).clear()
        self.element_is_visible(self.INPUT_AGE).send_keys(age)
        self.element_is_visible(self.SUBMIT_BUTTON).click()
        return str(age)

    def delete_some_person(self):
        self.element_is_visible(self.DELETE_BUTTON).click()
        return self.element_is_present(self.NO_ROWS_FOUND).text

    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.COUNT_ROWS)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{x}"]')).click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        list_rows = self.elements_are_present(self.LIST)
        return len(list_rows)
