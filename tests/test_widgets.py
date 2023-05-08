import time

import allure

from pages.accordian_page import AccordianPage
from pages.auto_complete_page import AutoCompletePage
from pages.date_picker_page import DatePickerPage
from pages.dragabble_page import DragabblePage
from pages.droppable_page import DroppablePage
from pages.progress_bar_page import ProgressBarPage
from pages.slider_page import SliderPage
from pages.tabs_page import TabsPage
from pages.tool_tips_page import ToolTipsPage


@allure.suite("Widgets")
class TestWidgets:
    @allure.feature('Accordian')
    class TestAccordianPage:
        @allure.title('Check accordian')
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_first_accordian('first')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0

    @allure.feature('AutoComplete')
    class TestAutoComplete:
        @allure.title('Check autocomplete')
        def test_fill_multi_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            colors = auto_complete_page.fill_input_multi()
            colors_result = auto_complete_page.check_color_in_multi()
            assert colors == colors_result
            time.sleep(5)

        @allure.title('Check remove value')
        def test_remove_value(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            auto_complete_page.fill_input_multi()
            count_value_before, count_value_after = auto_complete_page.remove_value_from_multi()
            assert count_value_before != count_value_after

        @allure.title('Check single complete')
        def test_fill_single_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            color = auto_complete_page.fill_single_input()
            color_result = auto_complete_page.check_color_in_single()
            assert color == color_result

    @allure.feature('Data picker')
    class TestDataPicker:
        @allure.title('Check select date')
        def test_select_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after

        @allure.title('Check select date')
        def test_select_date_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            print(value_date_before)
            print(value_date_after)

        @allure.title('Check slider')
        def test_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            value_before, value_after = slider_page.change_slider_value()
            assert value_before != value_after
            print(value_before)
            print(value_after)

        @allure.title('Check bar progress')
        def test_bar_progress(self, driver):
            bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            bar_page.open()
            value_before, value_after = bar_page.change_bar_progress()
            assert value_before != value_after

    @allure.feature('Tabs page')
    class TestTabsPage:
        @allure.title('Check tabs page')
        def test_tabs_page(self, driver):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            button_text, tab_text = tabs_page.click_on_tab('use')
            print(button_text)
            print(tab_text)
            assert button_text == 'Use'
            assert tab_text != 0

    @allure.feature('Tool tips page')
    class TestToolTipsPage:
        @allure.title('Check tool tips')
        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            button_text, input_text, first_href, second_href = tool_tips_page.check_tool_tips()
            time.sleep(5)
            assert button_text == 'You hovered over the Button'
            assert input_text == 'You hovered over the text field'
            assert first_href == 'You hovered over the Contrary'
            assert second_href == 'You hovered over the 1.10.32'

    @allure.feature('Droppable page')
    class TestDroppablePage:
        @allure.title('Check droppable page')
        def test_droppable_page_simple(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text, color = droppable_page.drop_simple()
            assert text == 'Dropped!'
            assert color == 'RGBA( 70, 130, 180, 1 )'.lower().replace('( ', '(').replace(' )', ')')

        @allure.title('Check droppable accept')
        def test_droppable_accept(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text, position_before, position_after = droppable_page.drop_accept()
            assert text == 'Dropped!'
            assert position_before != position_after

        @allure.title('Check droppable_not_accept')
        def test_droppable_not_accept(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text, position_before, position_after = droppable_page.drop_not_accept()
            assert text == 'Drop here'
            assert position_before != position_after

        @allure.title('Check not greedy')
        def test_not_greedy(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text_before_inner, text_before_outer, text_after_inner, text_after_outer = droppable_page.drop_not_greedy()
            assert text_before_inner != text_after_inner
            assert text_before_outer != text_after_outer
            assert text_after_inner == 'Dropped!'
            assert text_after_outer == 'Dropped!'

        @allure.title('Check greedy')
        def test_greedy(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text_before_inner, text_before_outer, text_after_inner, text_after_outer = droppable_page.drop_greedy()
            assert text_before_inner != text_after_inner
            assert text_before_outer == text_after_outer
            assert text_after_inner == 'Dropped!'
            assert text_after_outer == 'Outer droppable'

        @allure.title('Check revert')
        def test_revert(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text_before, text_after, position_before, position_after = droppable_page.drop_revert()
            assert text_before == 'Drop here'
            assert text_after == 'Dropped!'

        @allure.title('Check not revert')
        def test_not_revert(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text_before, text_after, position_before, position_after = droppable_page.drop_not_revert()
            assert position_before != position_after
            assert text_before == 'Drop here'
            assert text_after == 'Dropped!'

    @allure.feature('Dragabble page')
    class TestDragabblePage:
        @allure.title('Check dragabble page')
        def test_dragabble_page(self, driver):
            dragabble_page = DragabblePage(driver, 'https://demoqa.com/dragabble')
            dragabble_page.open()
            position_before, position_after = dragabble_page.drag_me_simple()
            assert position_before != position_after

        @allure.title('Check dragabble x,y')
        def test_dragabble_x_y(self, driver):
            dragabble_page = DragabblePage(driver, 'https://demoqa.com/dragabble')
            dragabble_page.open()
            position_before_x, position_after_x, position_before_y, position_after_y = dragabble_page.drag_me_x_y()
            assert position_before_x != position_after_x
            assert position_before_y != position_after_y

        @allure.title('Check dragabble container')
        def test_dragabble_container(self, driver):
            dragabble_page = DragabblePage(driver, 'https://demoqa.com/dragabble')
            dragabble_page.open()
            position_before_within_the_box, position_after_within_the_box, position_before_within_my_parent, position_after_within_my_parent = dragabble_page.drag_me_container()
            assert position_before_within_the_box != position_after_within_the_box
            assert position_before_within_my_parent != position_after_within_my_parent
