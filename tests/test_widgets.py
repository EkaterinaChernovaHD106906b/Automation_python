import time

from pages.accordian_page import AccordianPage
from pages.auto_complete_page import AutoCompletePage
from pages.date_picker_page import DatePickerPage
from pages.progress_bar_page import ProgressBarPage
from pages.slider_page import SliderPage
from pages.tabs_page import TabsPage
from pages.tool_tips_page import ToolTipsPage


class TestWidgets:

    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_first_accordian('first')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0

    class TestAutoComplete:

        def test_fill_multi_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            colors = auto_complete_page.fill_input_multi()
            colors_result = auto_complete_page.check_color_in_multi()
            assert colors == colors_result
            time.sleep(5)

        def test_remove_value(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            auto_complete_page.fill_input_multi()
            count_value_before, count_value_after = auto_complete_page.remove_value_from_multi()
            assert count_value_before != count_value_after

        def test_fill_single_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            color = auto_complete_page.fill_single_input()
            color_result = auto_complete_page.check_color_in_single()
            assert color == color_result

    class TestDataPicker:

        def test_select_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after

        def test_select_date_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            print(value_date_before)
            print(value_date_after)

        def test_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            value_before, value_after = slider_page.change_slider_value()
            assert value_before != value_after
            print(value_before)
            print(value_after)

        def test_bar_progress(self, driver):
            bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            bar_page.open()
            value_before, value_after = bar_page.change_bar_progress()
            assert value_before != value_after

    class TestTabsPage:

        def test_tabs_page(self, driver):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            button_text, tab_text = tabs_page.click_on_tab('use')
            print(button_text)
            print(tab_text)
            assert button_text == 'Use'
            assert tab_text != 0

    class TestToolTipsPage:

        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            button_text, input_text, first_href, second_href = tool_tips_page.check_tool_tips()
            time.sleep(5)
            assert button_text == 'You hovered over the Button'
            assert input_text == 'You hovered over the text field'
            assert first_href == 'You hovered over the Contrary'
            assert second_href == 'You hovered over the 1.10.32'








