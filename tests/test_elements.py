import time

from pages.base_page import BasePage
from pages.elements_page_locators import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.fill_all_fields()
            time.sleep(5)
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            print(output_name)
            print(output_email)
            print(output_cur_addr)
            print(output_per_addr)





