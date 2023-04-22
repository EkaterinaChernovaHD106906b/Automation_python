import os
import time

from selenium.webdriver.common.by import By

from generator.generator import generated_file
from pages.base_page import BasePage


class UploadDownloadPage(BasePage):
    DOWNLOAD = (By.CSS_SELECTOR, 'a[id="downloadButton"]')
    UPLOAD_PATH = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')
    UPLOAD_BUTTON = (By.CSS_SELECTOR, 'input[id="uploadFile"]')

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.UPLOAD_BUTTON).send_keys(path)
        os.remove(path)
        uploaded_file = self.element_is_present(self.UPLOAD_PATH).text
        return file_name.split('\\')[-1], uploaded_file.split('\\')[-1]
