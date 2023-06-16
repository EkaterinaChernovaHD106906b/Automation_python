import time

from uitap_pages.ajax_data_page import AJAXDataPage
from uitap_pages.class_attribute_page import ClassAttributePage
from uitap_pages.dynamic_id_page import DynamicIdPage
from uitap_pages.dynamic_table_page import DynamicTablePage
from uitap_pages.hidden_layers_page import HiddenLayersPage
from uitap_pages.load_page import LoadPage
from uitap_pages.scrollbars_page import ScrollBarsPage
from uitap_pages.shadow_DOM_page import ShadowDomPage
from uitap_pages.text_input_page import TextInputPage


class TestPages:
    class TestUI:

        def test_get_guid(self, driver):
            guid_page = ShadowDomPage(driver, 'http://uitestingplayground.com/shadowdom')
            guid_page.open()
            guid_page.get_guid()
            time.sleep(5)

        def test_dynamic_id_page(self, driver):
            dynamic_id_page = DynamicIdPage(driver, 'http://uitestingplayground.com/dynamicid')
            dynamic_id_page.open()
            button_id_before, button_id_after = dynamic_id_page.click_on_the_button()
            assert button_id_before != button_id_after

        def test_class_attribute_page(self, driver):
            class_page = ClassAttributePage(driver, 'http://uitestingplayground.com/classattr')
            class_page.open()
            alert_text = class_page.check_button_class()
            time.sleep(5)
            assert alert_text == 'Primary button pressed'

        def test_hidden_layers_page(self, driver):
            hidden_layers_page = HiddenLayersPage(driver, 'http://uitestingplayground.com/hiddenlayers')
            hidden_layers_page.open()
            massage = hidden_layers_page.click_on_green_button()
            time.sleep(5)
            assert massage == 'Button is not clickable'

        def test_load_page(self, driver):
            load_page = LoadPage(driver, 'http://uitestingplayground.com/loaddelay')
            load_page.open()
            text = load_page.loading_page()
            time.sleep(5)
            assert text == 'Button Appearing After Delay'

        def test_ajax_page(self, driver):
            ajax_page = AJAXDataPage(driver, 'http://uitestingplayground.com/ajax')
            ajax_page.open()
            result = ajax_page.wait_element_ajax()
            assert result == 'Data loaded with AJAX get request.'

        def test_input_page(self, driver):
            input_page = TextInputPage(driver, 'http://uitestingplayground.com/textinput')
            input_page.open()
            button_name_before, button_name_after = input_page.check_text_on_the_button()
            time.sleep(5)
            assert button_name_before != button_name_after

        def test_scrollbar_page(self, driver):
            scrollbar_page = ScrollBarsPage(driver, 'http://uitestingplayground.com/scrollbars')
            scrollbar_page.open()
            scrollbar_page.use_scrollbar()
            time.sleep(5)

        def test_dynamic_table_page(self, driver):
            dynamic_table_page = DynamicTablePage(driver, 'http://uitestingplayground.com/dynamictable')
            dynamic_table_page.open()
            value, label_cpu = dynamic_table_page.get_value_of_cpu()
            time.sleep(5)
            assert value == label_cpu





