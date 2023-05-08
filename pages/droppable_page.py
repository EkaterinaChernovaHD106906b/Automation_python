import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DroppablePage(BasePage):
    # Simple
    SIMPLE_TAB = (By.CSS_SELECTOR, 'a#droppableExample-tab-simple')
    SIMPLE_DRAG_ME = (By.CSS_SELECTOR, 'div#draggable')
    SIMPLE_DROPPED = (By.CSS_SELECTOR, 'div.simple-drop-container div#droppable')
    SIMPLE_DROPPED_TEXT = (By.CSS_SELECTOR, "div#droppable[class='drop-box ui-droppable ui-state-highlight'] p")
    # Accept
    ACCEPT_TAB = (By.CSS_SELECTOR, 'a#droppableExample-tab-accept')
    ACCEPTABLE = (By.CSS_SELECTOR, 'div#acceptable')
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, 'div#notAcceptable')
    ACCEPT_DROPPED = (By.XPATH, '//div[@id="droppableExample-tabpane-accept"]//div[@id="droppable"]')
    ACCEPT_DROPPED_TEXT = (By.XPATH, '//div[@id="droppableExample-tabpane-accept"]//div[@id="droppable"]/p')
    # Prevent
    PREVENT_TAB = (By.CSS_SELECTOR, 'a#droppableExample-tab-preventPropogation')
    PREVENT_PROPOGATION_DRAG_ME = (By.CSS_SELECTOR, 'div#dragBox')
    PREVENT_PROPOGATION_OUTER_TEXT = (By.CSS_SELECTOR, 'div#notGreedyDropBox p')
    PREVENT_PROPOGATION_INNER = (By.CSS_SELECTOR, 'div#notGreedyInnerDropBox')
    PREVENT_PROPOGATION_INNER_TEXT = (By.CSS_SELECTOR, 'div#notGreedyInnerDropBox p')
    PREVENT_PROPOGATION_OUTER_TEXT_2 = (By.CSS_SELECTOR, 'div#greedyDropBox p')
    PREVENT_PROPOGATION_INNER_2 = (By.CSS_SELECTOR, 'div#greedyDropBoxInner')
    PREVENT_PROPOGATION_INNER_TEXT_2 = (By.CSS_SELECTOR, 'div#greedyDropBoxInner p')
    # Revert
    REVERT_TAB = (By.CSS_SELECTOR, 'a#droppableExample-tab-revertable')
    WILL_REVERT = (By.CSS_SELECTOR, 'div#revertable')
    NOT_REVERT = (By.CSS_SELECTOR, 'div#notRevertable')
    REVERT_DROP_HERE = (By.CSS_SELECTOR, 'div.revertable-drop-container div#droppable')
    REVERT_TEXT = (By.CSS_SELECTOR, 'div.revertable-drop-container div#droppable p')

    def drop_simple(self):
        drag_element = self.element_is_visible(self.SIMPLE_DRAG_ME)
        drop_element = self.element_is_visible(self.SIMPLE_DROPPED)
        self.action_drag_and_drop_to_element(drag_element, drop_element)
        text = self.element_is_visible(self.SIMPLE_DROPPED_TEXT).text
        color = self.element_is_present(self.SIMPLE_DROPPED)
        new_color = color.value_of_css_property('background-color')
        return text, new_color

    def drop_accept(self):
        tab = self.element_is_visible(self.ACCEPT_TAB)
        tab.click()
        acceptable = self.element_is_visible(self.ACCEPTABLE)
        position_before = acceptable.get_attribute('style')
        dropped = self.element_is_visible(self.ACCEPT_DROPPED)
        self.action_drag_and_drop_to_element(acceptable, dropped)
        text_accept = self.element_is_visible(self.ACCEPT_DROPPED_TEXT).text
        position_after = acceptable.get_attribute('style')
        return text_accept, position_before, position_after

    def drop_not_accept(self):
        tab = self.element_is_visible(self.ACCEPT_TAB)
        tab.click()
        not_acceptable = self.element_is_visible(self.NOT_ACCEPTABLE)
        dropped = self.element_is_visible(self.ACCEPT_DROPPED)
        position_before = not_acceptable.get_attribute('style')
        self.action_drag_and_drop_to_element(not_acceptable, dropped)
        text_not_acceptable = self.element_is_visible(self.ACCEPT_DROPPED_TEXT).text
        position_after = not_acceptable.get_attribute('style')
        return text_not_acceptable, position_before, position_after

    def drop_not_greedy(self):
        tab = self.element_is_visible(self.PREVENT_TAB)
        tab.click()
        drag_me = self.element_is_visible(self.PREVENT_PROPOGATION_DRAG_ME)
        inner = self.element_is_visible(self.PREVENT_PROPOGATION_INNER)
        text_before_inner = self.element_is_visible(self.PREVENT_PROPOGATION_INNER_TEXT).text
        text_before_outer = self.element_is_visible(self.PREVENT_PROPOGATION_OUTER_TEXT).text
        self.action_drag_and_drop_to_element(drag_me, inner)
        text_after_inner = self.element_is_visible(self.PREVENT_PROPOGATION_INNER_TEXT).text
        text_after_outer = self.element_is_visible(self.PREVENT_PROPOGATION_OUTER_TEXT).text
        return text_before_inner, text_before_outer, text_after_inner, text_after_outer

    def drop_greedy(self):
        tab = self.element_is_visible(self.PREVENT_TAB)
        tab.click()
        drag_me = self.element_is_visible(self.PREVENT_PROPOGATION_DRAG_ME)
        inner = self.element_is_visible(self.PREVENT_PROPOGATION_INNER_2)
        text_before_inner = self.element_is_visible(self.PREVENT_PROPOGATION_INNER_TEXT_2).text
        text_before_outer = self.element_is_visible(self.PREVENT_PROPOGATION_OUTER_TEXT_2).text
        self.action_drag_and_drop_to_element(drag_me, inner)
        text_after_inner = self.element_is_visible(self.PREVENT_PROPOGATION_INNER_TEXT_2).text
        text_after_outer = self.element_is_visible(self.PREVENT_PROPOGATION_OUTER_TEXT_2).text
        return text_before_inner, text_before_outer, text_after_inner, text_after_outer

    def drop_revert(self):
        tab = self.element_is_visible(self.REVERT_TAB)
        tab.click()
        revert = self.element_is_visible(self.WILL_REVERT)
        drop = self.element_is_visible(self.REVERT_DROP_HERE)
        text_before = self.element_is_visible(self.REVERT_TEXT).text
        position_before = self.element_is_visible(self.WILL_REVERT).get_attribute('style')
        self.action_drag_and_drop_to_element(revert, drop)
        time.sleep(5)
        text_after = self.element_is_visible(self.REVERT_TEXT).text
        position_after = self.element_is_visible(self.WILL_REVERT).get_attribute('style')
        print(text_before)
        print(position_before)
        print(text_after)
        print(position_after)
        return text_before, text_after, position_before, position_after

    def drop_not_revert(self):
        tap = self.element_is_visible(self.REVERT_TAB)
        tap.click()
        not_revert = self.element_is_visible(self.NOT_REVERT)
        drop = self.element_is_visible(self.REVERT_DROP_HERE)
        text_before = self.element_is_visible(self.REVERT_TEXT).text
        position_before = self.element_is_visible(self.NOT_REVERT).get_attribute('style')
        self.action_drag_and_drop_to_element(not_revert, drop)
        text_after = self.element_is_visible(self.REVERT_TEXT).text
        position_after = self.element_is_visible(self.NOT_REVERT).get_attribute('style')
        return text_before, text_after, position_before, position_after
