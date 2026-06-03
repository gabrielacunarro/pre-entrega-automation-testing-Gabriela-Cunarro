import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from utils.data_reader import read_users_csv

@pytest.fixture(scope="function")
def driver():
 """Fixture que proporciona un WebDriver configurado."""
 chrome_options = Options()
 chrome_options.add_argument("--no-sandbox")
 chrome_options.add_argument("--disable-dev-shm-usage")
 service = Service()
 driver = webdriver.Chrome(service=service, options=chrome_options)
 driver.maximize_window()
 driver.implicitly_wait(5)
 yield driver
 time.sleep(1) 
 driver.quit()

 
@pytest.fixture
def driver_logged(driver):
    login_page = LoginPage(driver)

    user = read_users_csv()[0]

    login_page.login(user["username"],user["password"])

    return driver
