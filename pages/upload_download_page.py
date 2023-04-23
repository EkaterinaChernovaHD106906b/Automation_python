import base64
import os
import random
import time

from selenium.webdriver.common.by import By

from generator.generator import generated_file
from pages.base_page import BasePage


class UploadDownloadPage(BasePage):
    DOWNLOAD = (By.CSS_SELECTOR, 'a[id="downloadButton"]')
    UPLOAD_PATH = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')
    UPLOAD_BUTTON = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    HREF_DOWNLOAD = (By.CSS_SELECTOR, 'a[id="downloadButton"]')

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.UPLOAD_BUTTON).send_keys(path)
        os.remove(path)
        uploaded_file = self.element_is_present(self.UPLOAD_PATH).text
        return file_name.split('\\')[-1], uploaded_file.split('\\')[-1]

    def download_file(self):
        link = self.element_is_present(self.HREF_DOWNLOAD).get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = rf'C:\Users\user\PycharmProjects\Automation_python\filetest{random.randint(1, 100)}.jpeg'
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file)
        return check_file

