import random
import time

from pages.base_page import BasePage
from pages.browser_windows_page import BrowserWindowsPage
from pages.button_page import ButtonsPage
from pages.check_box_page import CheckBoxPage
from pages.dynamic_properties_page import DynamicPropertiesPage
from pages.form_page import TextBoxPage
from pages.link_page import LinkPage
from pages.radio_button_page import RadioButtonPage
from pages.upload_download_page import UploadDownloadPage
from pages.web_table_page import WebTablePage


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

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, "Error"

    class TestRadioButton:

        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            assert output_no == 'No', "'No' have not been selected"
            time.sleep(5)

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            print(new_person)
            print(table_result)
            assert new_person in table_result
            time.sleep(5)

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_world = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_world)
            table_result = web_table_page.check_search_person()
            assert key_world in table_result, 'The person was not found in the table'

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            last_name = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(last_name)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, 'The person card has not been changed'
            time.sleep(5)

        def test_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            last_name = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(last_name)
            actual_rows = web_table_page.delete_some_person()
            expected_rows = 'No rows found'
            assert actual_rows == expected_rows

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            time.sleep(5)
            assert count == [5, 10, 20, 25, 50, 100], 'Error'

    class TestButtonsPage:

        def test_different_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            assert double == 'You have done a double click'
            assert right == 'You have done a right click'
            assert click == 'You have done a dynamic click'

    class TestLinksPage:

        def test_check_link(self, driver):
            page_link = LinkPage(driver, 'https://demoqa.com/links')
            page_link.open()
            print(page_link.check_new_tab_simple_link())
            response_code = page_link.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400

    class TestUploadDownload:

        def test_upload_file(self, driver):
            upload_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_page.open()
            file_name, result = upload_page.upload_file()
            assert file_name == result, "The file has not been uploaded"

        def test_download_file(self, driver):
            download_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            download_page.open()
            check = download_page.download_file()
            assert check is True, 'The file has not been downloaded'

    class TestDynamicPropertiesPage:

        def test_dynamic_properties(self, driver):
            dynamic_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_page.open()
            color_before, color_after = dynamic_page.check_changed_of_color()
            assert color_before != color_after


        def test_appear_button(self, driver):
            dynamic_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_page.open()
            appear = dynamic_page.check_appear_of_button()
            assert appear is True

        def test_enable_button(self, driver):
            dynamic_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_page.open()
            enable_button = dynamic_page.check_enable_button()
            assert enable_button is True

    