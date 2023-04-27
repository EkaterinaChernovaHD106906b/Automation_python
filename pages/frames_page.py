from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FramesPage(BasePage):
    FRAME1 = (By.CSS_SELECTOR, 'iframe#frame1')
    FRAME2 = (By.CSS_SELECTOR, 'iframe#frame2')
    FRAME_TEXT = (By.CSS_SELECTOR, 'h1#sampleHeading')

    def check_frame(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.FRAME1)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.FRAME_TEXT).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_num == 'frame2':
            frame = self.element_is_present(self.FRAME2)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.FRAME_TEXT).text
            return [text, width, height]
