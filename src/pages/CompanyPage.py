from selenium.webdriver.common.by import By

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumpagefactory import PageFactory


class CompanyPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'label_hq': ('XPATH', '//section//span[contains(text(), "San Francisco")]'),
        'label_founded': ('XPATH', '//section//span[contains(text(), "2007")]'),
        'label_size': ('XPATH', '//section//span[contains(text(), "650+")]'),
        'label_clients': ('XPATH', '//section//span[contains(text(), "200+")]')
    }

    def get_consulting_office(self, office):
        locator = (By.XPATH,
                   f'//strong[contains(text(),"Consulting Offices")]/following-sibling::div//span[contains(text(),"{office}")]')
        try:
            # Wait for the element to be present before attempting to find it
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except (NoSuchElementException, TimeoutException):
            return False

    def get_engineering_hub(self, hub):
        locator = (By.XPATH,
                   f'//strong[contains(text(),"Engineering Hubs")]/following-sibling::div//span[contains(text(),"{hub}")]')
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except (NoSuchElementException, TimeoutException):
            return False

    def get_certification_status(self, certification):
        locator = (By.XPATH,
                   f'//strong[contains(text(),"Certifications")]/following-sibling::div//span[contains(text(),"{certification}")]')
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except (NoSuchElementException, TimeoutException):
            return False
