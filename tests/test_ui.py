import time

from uitap_pages.class_attribute_page import ClassAttributePage
from uitap_pages.dynamic_id_page import DynamicIdPage
from uitap_pages.hidden_layers_page import HiddenLayersPage
from uitap_pages.load_page import LoadPage
from uitap_pages.shadow_DOM_page import ShadowDomPage


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


