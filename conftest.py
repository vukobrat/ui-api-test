from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

from config.config import APP_URL
from tests.api.common.api import signup_user, login_user

button_agree_cookies = '//button[contains(text(), "Agree & Continue")]'


@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(APP_URL)
    driver.find_element(By.XPATH, button_agree_cookies).click()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def user():
    new_user = signup_user()
    logged_in_user = login_user(new_user)
    logged_in_user['user']['password'] = new_user['password']
    yield logged_in_user



