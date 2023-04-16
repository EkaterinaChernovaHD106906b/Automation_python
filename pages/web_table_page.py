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
