import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ToolTipsPage(BasePage):
    TOOL_BUTTON = (By.CSS_SELECTOR, 'button#toolTipButton')
    HOVERED_BUTTON = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')
    TOOL_INPUT = (By.CSS_SELECTOR, 'input#toolTipTextField')
    HOVERED_INPUT = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')
    TOOL_CONTAINER_FIRST_HREF = (By.XPATH, '//div[@id="texToolTopContainer"]// a[1]')
    HOVERED_FIRST_HREF = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')
    TOOL_CONTAINER_SECOND_HREF = (By.XPATH, '//div[@id="texToolTopContainer"]// a[2]')
    HOVERED_SECOND_HREF = (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')
    TEXT = (By.CSS_SELECTOR, 'div.tooltip-inner')

    def get_text(self, hover_elem, wait_elem):
        element = self.element_is_present(hover_elem)
        self.move_to_element(element)
        time.sleep(3)
        self.element_is_visible(wait_elem)
        text = self.element_is_visible(self.TEXT).text
        return text

    def check_tool_tips(self):
        tool_button = self.get_text(self.TOOL_BUTTON, self.HOVERED_BUTTON)
        tool_input = self.get_text(self.TOOL_INPUT, self.HOVERED_INPUT)
        first_href = self.get_text(self.TOOL_CONTAINER_FIRST_HREF, self.HOVERED_FIRST_HREF)
        self.remove_footer()
        second_href = self.get_text(self.TOOL_CONTAINER_SECOND_HREF, self.HOVERED_SECOND_HREF)
        return tool_button, tool_input, first_href, second_href
