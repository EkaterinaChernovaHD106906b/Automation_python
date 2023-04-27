import time

from pages.alertsPage import AlertsPage
from pages.browser_windows_page import BrowserWindowsPage


class TestAlertsFrameWindow:
    class TestBrowserWindowsPage:

        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            result_text = new_tab_page.open_new_tab()
            assert result_text == 'This is a sample page'

        def test_new_window(self, driver):
            new_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_window_page.open()
            result_text = new_window_page.open_new_window()
            assert result_text == 'This is a sample page'

    class TestAlerts:

        def test_alerts(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.see_alert()
            assert alert_text == 'You clicked a button'

        def test_alerts_timer(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            text_alert = alerts_page.see_alert_after_5sec()
            assert text_alert == 'This alert appeared after 5 seconds'

        def test_confirm_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            text_result = alerts_page.confirm_alert()
            assert text_result == 'You selected Ok'

        def test_prompt_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            text_result, text_result2 = alerts_page.prompt_alert()
            assert f'You entered {text_result}' == text_result2





