from pathlib import Path
from os import path, makedirs
from shutil import rmtree
from urllib.parse import urljoin

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait as WD_Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException

import modules.chrome_options as chr_opts


class RobotSpareBinBuyer:
    BASE_URL = 'https://robotsparebinindustries.com/'
    ORDER_URL = urljoin(BASE_URL, '/#/robot-order')
    OUTPUT_PATH = f'{Path(".main.py").parent.resolve()}/output/'
    wait_time = 1

    def __init__(self):
        self.driver: Chrome | None = None

    def order_placer(self, head, body, legs, address):
        self.close_popup()
        self.select_head(head_number=head)
        self.select_body(body_number=body)
        self.input_legs(legs_number=legs)
        self.input_address(address=address)
        self.make_preview()
        self.confirm_order()
        self.get_photo_robot()

    def open_order_page(self):
        self.driver.get(self.ORDER_URL)

    def close_popup(self):
        css_selector = 'button.btn.btn-dark'
        self.wait_for(css_selector)
        popup_ok_button = self.driver.find_element(by=By.CSS_SELECTOR,
                                                   value=css_selector)
        popup_ok_button.click()

    def select_head(self, head_number):
        id_selector = 'head'
        self.wait_for(selector=id_selector, by=By.ID)
        head_select = self.driver.find_element(by=By.ID, value=id_selector)
        Select(head_select).select_by_index(head_number)

    def select_body(self, body_number):
        id_selector = f'id-body-{body_number}'
        self.wait_for(selector=id_selector, by=By.ID)
        body_select = self.driver.find_element(by=By.ID, value=id_selector)
        body_select.click()

    def input_legs(self, legs_number):
        css_selector = 'input[placeholder="Enter the part number for the legs"]'
        self.wait_for(css_selector)
        legs_select = self.driver.find_element(by=By.CSS_SELECTOR,
                                               value=css_selector)
        legs_select.clear()
        legs_select.send_keys(legs_number)

    def input_address(self, address):
        id_selector = 'address'
        self.wait_for(selector=id_selector, by=By.ID)
        address_fill = self.driver.find_element(by=By.ID, value=id_selector)
        address_fill.clear()
        address_fill.send_keys(address)

    def make_preview(self):
        self.driver.find_element(by=By.ID, value='preview').click()

    def confirm_order(self):
        """Click to 'ORDER' button and check for alert. If yes, try again"""
        confirm_button = self.driver.find_element(by=By.ID, value='order')
        confirm_button.click()
        if self.check_alert():
            self.confirm_order()

    def check_alert(self):
        """Check if alert, if yes returned True"""
        condition = EC.visibility_of_element_located((By.CLASS_NAME,
                                                      'alert-danger'))
        try:
            WD_Wait(self.driver, timeout=1).until(condition)
        except TimeoutException:
            return False
        else:
            return True

    def get_photo_robot(self):
        receipt_id = self.get_receipt_id()
        robot_preview = self.driver.find_element(by=By.ID,
                                                 value='robot-preview-image')
        robot_preview.screenshot(f'{self.OUTPUT_PATH}{receipt_id}_robot.png')

    def get_receipt_id(self):
        return self.driver.find_element(by=By.CSS_SELECTOR, value='.badge').text

    def output_folder(self):
        """Create output folder, and clear it if exists"""
        if path.exists(self.OUTPUT_PATH):
            rmtree(self.OUTPUT_PATH)
        makedirs(self.OUTPUT_PATH)

    def order_another(self):
        self.driver.find_element(by=By.ID, value='order-another').click()

    def wait_for(self, selector, by: By = By.CSS_SELECTOR,
                 time=wait_time) -> WebElement:
        condition = EC.element_to_be_clickable((by, selector))
        return WD_Wait(driver=self.driver, timeout=time).until(condition)

    def __enter__(self):
        self.driver = self.__init_driver()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()

    @staticmethod
    def __init_driver() -> Chrome:
        service = Service(ChromeDriverManager().install())
        options = ChromeOptions()
        for argument in chr_opts.launch_options:
            options.add_argument(argument)
        options.add_experimental_option(chr_opts.non_automation[0],
                                        chr_opts.non_automation[1])
        options.add_experimental_option(chr_opts.disable_notifications[0],
                                        chr_opts.disable_notifications[1])
        driver = Chrome(service=service, options=options)
        driver.maximize_window()
        return driver
