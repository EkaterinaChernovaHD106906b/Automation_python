import random
import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DragabblePage(BasePage):
    DRAG_ME = (By.CSS_SELECTOR, 'div#dragBox')
    AXIS_TAB = (By.CSS_SELECTOR, 'a#draggableExample-tab-axisRestriction')
    ONLY_X = (By.CSS_SELECTOR, 'div#restrictedX')
    ONLY_Y = (By.CSS_SELECTOR, 'div#restrictedY')
    CONTAINER_TAB = (By.CSS_SELECTOR, 'a#draggableExample-tab-containerRestriction')
    WITHIN_THE_BOX = (By.CSS_SELECTOR, 'div#containmentWrapper div[class*="draggable ui-widget"]')
    WITHIN_MY_PARENT = (By.CSS_SELECTOR, 'div[class="draggable ui-widget-content m-3"] span')

    def drag_me_simple(self):
        drag_me = self.element_is_visible(self.DRAG_ME)
        position_before = drag_me.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_me, 250, 0)
        position_after = drag_me.get_attribute('style')
        return position_before, position_after

    def drag_me_x_y(self):
        self.element_is_visible(self.AXIS_TAB).click()
        only_x = self.element_is_visible(self.ONLY_X)
        position_before_x = only_x.get_attribute('style')
        self.action_drag_and_drop_by_offset(only_x, random.randint(50, 100), 0)
        position_after_x = only_x.get_attribute('style')
        only_y = self.element_is_visible(self.ONLY_Y)
        position_before_y = only_y.get_attribute('style')
        self.action_drag_and_drop_by_offset(only_y, 0, random.randint(50, 150))
        position_after_y = only_y.get_attribute('style')
        return position_before_x, position_after_x, position_before_y, position_after_y

    def drag_me_container(self):
        self.element_is_visible(self.CONTAINER_TAB).click()
        within_the_box = self.element_is_visible(self.WITHIN_THE_BOX)
        position_before_within_the_box = within_the_box.get_attribute('style')
        count = 5
        while count != 0:
            self.action_drag_and_drop_by_offset(within_the_box, random.randint(50, 200), random.randint(90, 150))
            count -= 1
        position_after_within_the_box = within_the_box.get_attribute('style')
        within_my_parent = self.element_is_visible(self.WITHIN_MY_PARENT)
        position_before_within_my_parent = within_my_parent.get_attribute('style')
        self.scroll_by(150)
        count2 = 5
        while count2 != 0:
            self.action_drag_and_drop_by_offset(within_my_parent, random.randint(30, 70), random.randint(15, 30))
            count2 -= 1
        position_after_within_my_parent = within_my_parent.get_attribute('style')
        return position_before_within_the_box, position_after_within_the_box, position_before_within_my_parent, position_after_within_my_parent
